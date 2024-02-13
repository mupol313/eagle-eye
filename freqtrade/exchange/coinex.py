import logging
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple
import ccxt
import math
from freqtrade.constants import BuySell
from freqtrade.enums import CandleType, MarginMode, PriceType, TradingMode
from freqtrade.exceptions import DDosProtection, ExchangeError, OperationalException, TemporaryError
from freqtrade.exchange import Exchange
from freqtrade.exchange.common import retrier
from freqtrade.util.datetime_helpers import dt_now, dt_ts
from freqtrade.exchange.types import OHLCVResponse, OrderBook, Ticker, Tickers


logger = logging.getLogger(__name__)


class Coinex(Exchange):

    _ft_has: Dict = {
        "ohlcv_candle_limit": 1000,
        "ohlcv_has_history": True,
        "order_time_in_force": ["GTC", "FOK", "IOC"],
    }

    _ft_has_futures: Dict = {
        "ohlcv_has_history": True,
        "mark_ohlcv_timeframe": "4h",
        "funding_fee_timeframe": "8h",
        "stoploss_on_exchange": True,
        "stoploss_order_types": {"limit": "limit", "market": "market"},
        "stop_price_prop": "stopPrice",
        "stop_price_type_field": "triggerBy",
        "stop_price_type_value_mapping": {
            PriceType.LAST: "LastPrice",
            PriceType.MARK: "MarkPrice",
            PriceType.INDEX: "IndexPrice",
        },
    }

    _supported_trading_mode_margin_pairs: List[Tuple[TradingMode, MarginMode]] = [(TradingMode.FUTURES, MarginMode.ISOLATED)]


    @property
    def _ccxt_config(self) -> Dict:
        config = {}
        if self.trading_mode == TradingMode.SPOT:
            config.update({"options": {"defaultType": "spot"}})
        
        if self.trading_mode == TradingMode.MARGIN:
            config.update({"options": {"defaultType": "margin"}})

        if self.trading_mode == TradingMode.FUTURES:
            config.update({"options": {"defaultType": "swap"}})

        config.update(super()._ccxt_config)
        return config


    def ohlcv_candle_limit(self, timeframe: str, candle_type: CandleType, since_ms: Optional[int] = None) -> int:
        candel_limit = 1000
        return candel_limit


    def get_max_leverage(self, pair: str, stake_amount: Optional[float]) -> float:
        if self.trading_mode == TradingMode.SPOT:
            return 1.0

        if self.trading_mode == TradingMode.FUTURES:
            lev = float(self._config.get('leverage', 1))
            return math.floor(lev)
    
    @retrier
    def fetch_ticker(self, pair: str) -> Ticker:
        try:
            if (pair not in self.markets or self.markets[pair].get('active', False) is False):
                raise ExchangeError(f"Pair {pair} not available")  
            data: Ticker = self._api.fetch_ticker(pair)
            quote_volume = data['baseVolume'] * data['last']
            data['quoteVolume'] = quote_volume
            return data

        except ccxt.DDoSProtection as e:
            raise DDosProtection(e) from e
        except (ccxt.NetworkError, ccxt.ExchangeError) as e:
            raise TemporaryError(f'Could not load ticker due to {e.__class__.__name__}. Message: {e}') from e
        except ccxt.BaseError as e:
            raise OperationalException(e) from e

    @retrier
    def get_tickers(self, symbols: Optional[List[str]] = None, cached: bool = False) -> Tickers:
        tickers: Tickers
        if cached:
            with self._cache_lock:
                tickers = self._fetch_tickers_cache.get('fetch_tickers')
            if tickers:
                for pair, data in tickers.items():
                    if data['quoteVolume'] is None:
                        quote_volume = data['baseVolume'] * data['last']
                        data['quoteVolume'] = quote_volume
                
                return tickers
        try:
            tickers = self._api.fetch_tickers(symbols)
            for pair, data in tickers.items():
                    if data['quoteVolume'] is None:
                        quote_volume = data['baseVolume'] * data['last']
                        data['quoteVolume'] = quote_volume

            with self._cache_lock:
                self._fetch_tickers_cache['fetch_tickers'] = tickers

            return tickers
        except ccxt.NotSupported as e:
            raise OperationalException(f'Exchange {self._api.name} does not support fetching tickers in batch. '
                                        f'Message: {e}') from e
        except ccxt.BadSymbol as e:
            logger.warning(f"Could not load tickers due to {e.__class__.__name__}. Message: {e} .")
            self.reload_markets(True)
            raise TemporaryError from e
        except ccxt.DDoSProtection as e:
            raise DDosProtection(e) from e
        except (ccxt.NetworkError, ccxt.ExchangeError) as e:
            raise TemporaryError(f'Could not load tickers due to {e.__class__.__name__}. Message: {e}') from e
        except ccxt.BaseError as e:
            raise OperationalException(e) from e

    def _lev_prep(self, pair: str, leverage: float, side: BuySell, accept_fail: bool = False):
        '''
        1: Isolated Margin 2: Cross Margin
        '''
        ISOLATED = 1
        if self.trading_mode != TradingMode.FUTURES and self._config['dry_run']:
            return
        leverage = math.floor(leverage)
        params = {'position_type': ISOLATED}
        try:
            res = self._api.set_leverage(leverage= leverage, symbol= pair , params= params )
            print(res)
            self._log_exchange_response('set_leverage', res)

        except ccxt.DDoSProtection as e:
            raise DDosProtection(e) from e
        except (ccxt.BadRequest, ccxt.InsufficientFunds) as e:
            if not accept_fail:
                raise TemporaryError(f'Could not set leverage due to {e.__class__.__name__}. Message: {e}') from e
        except (ccxt.NetworkError, ccxt.ExchangeError) as e:
            raise TemporaryError(f'Could not set leverage due to {e.__class__.__name__}. Message: {e}') from e
        except ccxt.BaseError as e:
            raise OperationalException(e) from e
