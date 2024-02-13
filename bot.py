import os
from freqtrade import main

current_path = os.path.abspath(__file__)
folder_path = os.path.dirname(current_path)
user_data_path = os.path.join(folder_path, 'user_data')
config_path = os.path.join(user_data_path, 'config.json')
pairs_file_path = os.path.join(user_data_path, 'pairs.json')
data_path = os.path.join(user_data_path, "data")
strategy_path = os.path.join(user_data_path, "strategies")
log_file_path = os.path.join(user_data_path, "logs\\coinex.txt")

# if os.path.isfile(config_path):
#     with open(config_path) as file:
#         config = json.load(file)

# if 'days' in config:
#     days = config['days']


# arg = ['list-exchanges','-c' , config_path,'--userdir' , user_data_path]

# arg = ['hyperopt','-c',config_path,'-d',data_path,'--userdir',user_dir_path,'-s' ,  '--strategy-path',strategy_path]
# arg = ['backtesting','-c',config_path,'-d',data_path,'--userdir',user_dir_path,'-s','EagleEye','--timerange','2023122']

# Strategy004
# Strategy003
arg =['install-ui']
# arg = ['backtesting' , '--help']
# arg = ['list-markets', '--userdir', user_data_path, '-c', config_path]
# arg = ['list-data','--userdir',user_data_path,'-c',config_path]
# arg = ['download-data', '--userdir', user_data_path, '-c', config_path , '--days' , '5' , '-t' , '5m' ]
# arg = ['list-strategies','--logfile','log.txt' ,'--userdir', user_data_path, '-c', config_path]
# arg = ['new-strategy', '--userdir',user_data_path,'-s','Rsi','--template','advanced']
# arg = ['backtesting','-c',config_path,'--userdir',user_data_path,'-s','Diamond' ]
# /# arg = ['list-freqaimodels' , '-c' , config_path , '-d' , data_path ,'--userdir',user_dir_path ]
# arg = ['plot-dataframe' ,'-c',config_path,'--userdir',user_dir_path , '-p' ,pairs[0] , '--strategy' , 'Diamond']
# arg = ['create-userdir','--userdir',user_data_path]
# arg = ['test-pairlist', '-c', config_path, '--userdir', user_data_path]
# arg = ['trade' , '--userdir', user_data_path, '-c', config_path, '-s', 'Diamond']
main.main(arg)

'''
{
    'command': 'list-strategies', 
    'verbosity': 0, 
    'logfile': None, 
    'config': ['C:\\freqtrade-develop\\my_freq\\user_data\\config.json'], 
    'datadir': None, 'user_data_dir': 'C:\\freqtrade-develop\\my_freq\\user_data', 
    'strategy_path': None, 
    'print_one_column': False, 
    'print_colorized': True, 
    'recursive_strategy_search': False, 
    'func': <function start_list_strategies at 0x000002AE9C47DEE0>}
{
    'days': 20, 
    'max_open_trades': 2, 
    'startup_candle_count': 300, 
    'db_url': 'sqlite:///user_data/database/tradesv3.sqlite', 
    'stake_amount': 0.2, 
    'fee': 0.001, 
    'available_capital': 50, 
    'tradable_balance_ratio': 0.9, 
    'timeframe': '5m', 
    'process_only_new_candles': False, 
    'dry_run': True, 
    'cancel_open_orders_on_exit': True, 
    'trading_mode': <TradingMode.FUTURES: 'futures'>, 
    'margin_mode': 'isolated', 
    'fiat_display_currency': 'USD', 
    'stake_currency': 'USDT', 
    'amend_last_stake_amount': True, 
    'dry_run_wallet': 100, 
    'initial_state': 'running', 
    'dataformat_ohlcv': 'json', 
    'dataformat_trades': 'json', 
    'force_entry_enable': True, 
    'recursive_strategy_search': True, 
    'entry_pricing': {'price_side': 'same', 'use_order_book': True, 'order_book_top': 1, 'price_last_balance': 0.0, 'check_depth_of_market': {'enabled': False, 'bids_to_ask_delta': 1}}, 'exit_pricing': {'price_side': 'same', 'use_order_book': True, 'order_book_top': 1, 'price_last_balance': 0.0}, 
    'unfilledtimeout': {'entry': 10, 'exit': 10, 'unit': 'minutes', 'exit_timeout_count': 0}, 
    'order_types': {'entry': 'limit', 'exit': 'limit', 'emergency_exit': 'market', 'force_exit': 'market', 'force_entry': 'market', 'stoploss': 'limit', 'stoploss_on_exchange': True, 'stoploss_price_type': 'last', 'stoploss_on_exchange_interval': 60, 'stoploss_on_exchange_limit_ratio': 0.99}, 
    'order_time_in_force': {'entry': 'GTC', 'exit': 'GTC'}, 
    'exchange': {'name': 'coinex', 'key': 'B9DF5F3B8CD54EB88498ED416F4DCBB1', 'secret': 'ED0442B6FF05AF077C836948204940A29719140935F24471', 'ccxt_config': {}, 'ccxt_async_config': {}, 'markets_refresh_interval': 30, 'pair_whitelist': ['PEPE/USDT:USDT', 'BTT/USDT:USDT'], 'password': ''}, 
    'pairlists': [{'method': 'StaticPairList'}], 
    'edge': {'enabled': False, 'process_throttle_secs': 3600, 'calculate_since_number_of_days': 7, 'allowed_risk': 0.01, 'stoploss_range_min': -0.01, 'stoploss_range_max': -0.1, 'stoploss_range_step': -0.01, 'minimum_winrate': 0.6, 'minimum_expectancy': 0.2, 'min_trade_number': 10, 'max_trade_duration_minute': 1440, 'remove_pumps': False}, 
    'telegram': {'enabled': True, 'token': '6304509441:AAHHpT_MTITDpjh01cOwFHYX6R2xAxBz-Wk', 'chat_id': '5514429070', 'allow_custom_messages': True, 'notification_settings': {'entry_fill': 'off', 'exit_fill': 'on', 'protection_trigger': 'on', 'protection_trigger_global': 'on', 'show_candle': 'off', 'strategy_msg': 'on'}}, 
    'bot_name': 'eagle_eye', 
    'api_server': {'enabled': True, 'listen_ip_address': '127.0.0.1', 'listen_port': 8080, 'verbosity': 'error', 'enable_openapi': True, 'jwt_secret_key': '95ee043b07757de739cacb5efffd52089f9a5959f1375b2375128263b6f76432', 'ws_token': '6PY_SjxK-LK-NP1bkg3IYIxA7dnrkBOnlA', 'CORS_origins': [], 'username': 'mupol313', 'password': 'Yamaha.123'}, 
    'internals': {'process_throttle_secs': 5, 'heartbeat_interval': 120, 'sd_notify': True}, 
    'strategy_path': 'user_data/strategies/', 
    'config_files': ['C:\\freqtrade-develop\\user_data\\config.json'], 
    
    'original_config': {'days': 20, 'max_open_trades': 2, 'startup_candle_count': 300, 'db_url': 'sqlite:///user_data/database/tradesv3.sqlite', 'stake_amount': 0.2, 'fee': 0.001, 'available_capital': 50, 'tradable_balance_ratio': 0.9, 'timeframe': '5m', 'process_only_new_candles': False, 'dry_run': True, 'cancel_open_orders_on_exit': True, 'trading_mode': 'futures', 'margin_mode': 'isolated', 'fiat_display_currency': 'USD', 'stake_currency': 'USDT', 'amend_last_stake_amount': True, 'dry_run_wallet': 100, 'initial_state': 'running', 'dataformat_ohlcv': 'json', 'dataformat_trades': 'json', 'force_entry_enable': True, 'recursive_strategy_search': True, 'entry_pricing': {'price_side': 'same', 'use_order_book': True, 'order_book_top': 1, 'price_last_balance': 0.0, 'check_depth_of_market': {'enabled': False, 'bids_to_ask_delta': 1}}, 'exit_pricing': {'price_side': 'same', 'use_order_book': True, 'order_book_top': 1, 'price_last_balance': 0.0}, 'unfilledtimeout': {'entry': 10, 'exit': 10, 'unit': 'minutes'}, 'order_types': {'entry': 'limit', 'exit': 'limit', 'emergency_exit': 'market', 'force_exit': 'market', 'force_entry': 'market', 'stoploss': 'limit', 'stoploss_on_exchange': True, 'stoploss_price_type': 'last', 'stoploss_on_exchange_interval': 60, 'stoploss_on_exchange_limit_ratio': 0.99}, 'order_time_in_force': {'entry': 'GTC', 'exit': 'GTC'}, 'exchange': {'name': 'coinex', 'key': 'B9DF5F3B8CD54EB88498ED416F4DCBB1', 'secret': 'ED0442B6FF05AF077C836948204940A29719140935F24471', 'ccxt_config': {}, 'ccxt_async_config': {}, 'markets_refresh_interval': 30, 'pair_whitelist': ['PEPE/USDT:USDT', 'BTT/USDT:USDT']}, 'pairlists': [{'method': 'StaticPairList'}], 'edge': {'enabled': False, 'process_throttle_secs': 3600, 'calculate_since_number_of_days': 7, 'allowed_risk': 0.01, 'stoploss_range_min': -0.01, 'stoploss_range_max': -0.1, 'stoploss_range_step': -0.01, 'minimum_winrate': 0.6, 'minimum_expectancy': 0.2, 'min_trade_number': 10, 'max_trade_duration_minute': 1440, 'remove_pumps': False}, 'telegram': {'enabled': True, 'token': '6304509441:AAHHpT_MTITDpjh01cOwFHYX6R2xAxBz-Wk', 'chat_id': '5514429070'}, 'bot_name': 'eagle_eye', 'api_server': {'enabled': True, 'listen_ip_address': '127.0.0.1', 'listen_port': 8080, 'verbosity': 'error', 'enable_openapi': True, 'jwt_secret_key': '95ee043b07757de739cacb5efffd52089f9a5959f1375b2375128263b6f76432', 'ws_token': '6PY_SjxK-LK-NP1bkg3IYIxA7dnrkBOnlA', 'CORS_origins': [], 'username': 'mupol313', 'password': 'Yamaha.123'}, 'internals': {'process_throttle_secs': 5, 'heartbeat_interval': 120, 'sd_notify': True}, 'strategy_path': 'user_data/strategies/', 'config_files': ['C:\\freqtrade-develop\\user_data\\config.json']}, 'verbosity': 0, 'runmode': <RunMode.UTIL_EXCHANGE: 'util_exchange'>, 'strategy': None, 'user_data_dir': WindowsPath('C:/freqtrade-develop/user_data'), 'datadir': WindowsPath('C:/freqtrade-develop/user_data/data/coinex'), 'exportfilename': WindowsPath('C:/freqtrade-develop/user_data/backtest_results'), 'print_colorized': True, 'candle_type_def': <CandleType.FUTURES: 'futures'>, 'pairs': ['PEPE/USDT:USDT', 'BTT/USDT:USDT'], 'new_pairs_days': 30, 'last_stake_amount_min_ratio': 0.5, 'reduce_df_footprint': False, 'minimum_trade_amount': 10, 'targeted_trade_amount': 20, 'startup_candle': [199, 399, 499, 999, 1999], 'export': 'trades'}



'original_config': {
    'days': 20, 
    'pair_options': {'max_price': 2, 'min_price': 0, 'qute_volume': True, 'asset_number': 50, 'markets_refresh_interval': 30}, 
    'max_open_trades': 2, 
    'startup_candle_count': 300, 
    'db_url': 'sqlite:///user_data/database/tradesv3.sqlite', 
    'stake_amount': 0.2, 
    'fee': 0.001, 
    'available_capital': 100, 
    'tradable_balance_ratio': 0.9, 
    'timeframe': '5m', 
    'process_only_new_candles': False, 
    'dry_run': True, 
    'cancel_open_orders_on_exit': True, 
    'trading_mode': 'futures', 
    'margin_mode': 'isolated', 
    'fiat_display_currency': 'USD', 
    'stake_currency': 'USDT', 
    'amend_last_stake_amount': True, 
    'dry_run_wallet': 100, 
    'initial_state': 'running', 
    'dataformat_ohlcv': 'json', 
    'dataformat_trades': 'json', 
    'force_entry_enable': True, 
    'recursive_strategy_search': True, 
    'entry_pricing': {'price_side': 'same', 'use_order_book': False, 'order_book_top': 1, 'price_last_balance': 0.0, 'check_depth_of_market': {'enabled': False, 'bids_to_ask_delta': 1}}, 
    'exit_pricing': {'price_side': 'same', 'use_order_book': False, 'order_book_top': 1, 'price_last_balance': 0.0}, 
    'unfilledtimeout': {'entry': 10, 'exit': 10, 'unit': 'minutes'}, 
    'order_types': {'entry': 'limit', 'exit': 'limit', 'emergency_exit': 'market', 'force_exit': 'market', 'force_entry': 'market', 'stoploss': 'limit', 'stoploss_on_exchange': False, 'stoploss_price_type': 'last', 'stoploss_on_exchange_interval': 60, 'stoploss_on_exchange_limit_ratio': 0.99}, 
    'exchange': {'name': 'coinex', 'key': 'B9DF5F3B8CD54EB88498ED416F4DCBB1', 'secret': 'ED0442B6FF05AF077C836948204940A29719140935F24471', 'ccxt_config': {}, 'ccxt_async_config': {}, 'markets_refresh_interval': 30, 'pair_whitelist': ['ARB/USDT:USDT']}, 
    'pairlists': [{'method': 'StaticPairList'}, {'method': 'VolumePairList', 'number_assets': 2, 'sort_key': 'quoteVolume', 'min_value': 0, 'refresh_period': 1800}, {'method': 'PriceFilter', 'min_price': 1e-14, 'max_price': 2}], 
    'edge': {'enabled': False, 'process_throttle_secs': 3600, 'calculate_since_number_of_days': 7, 'allowed_risk': 0.01, 'stoploss_range_min': -0.01, 'stoploss_range_max': -0.1, 'stoploss_range_step': -0.01, 'minimum_winrate': 0.6, 'minimum_expectancy': 0.2, 'min_trade_number': 10, 'max_trade_duration_minute': 1440, 'remove_pumps': False}, 'telegram': {'enabled': True, 'token': '6304509441:AAHHpT_MTITDpjh01cOwFHYX6R2xAxBz-Wk', 'chat_id': '5514429070'}, 'bot_name': 'eagle_eye', 'api_server': {'enabled': True, 'listen_ip_address': '127.0.0.1', 'listen_port': 8080, 'verbosity': 'error', 'enable_openapi': True, 'jwt_secret_key': '95ee043b07757de739cacb5efffd52089f9a5959f1375b2375128263b6f76432', 'ws_token': '6PY_SjxK-LK-NP1bkg3IYIxA7dnrkBOnlA', 'CORS_origins': [], 'username': 'mupol313', 'password': 'Yamaha.123'}, 'internals': {'process_throttle_secs': 5, 'heartbeat_interval': 120, 'sd_notify': True}, 'config_files': ['C:\\freqtrade-stable\\user_data\\config.json']}, 'verbosity': 0, 'runmode': <RunMode.UTIL_EXCHANGE: 'util_exchange'>, 'strategy': None, 'user_data_dir': WindowsPath('C:/freqtrade-stable/user_data'), 'datadir': WindowsPath('C:/freqtrade-stable/user_data/data/coinex'), 'exportfilename': WindowsPath('C:/freqtrade-stable/user_data/backtest_results'), 'print_colorized': True, 'candle_type_def': <CandleType.FUTURES: 'futures'>, 'pairs': ['ARB/USDT:USDT'], 'new_pairs_days': 30, 'last_stake_amount_min_ratio': 0.5, 'reduce_df_footprint': False, 'minimum_trade_amount': 10, 'targeted_trade_amount': 20, 'startup_candle': [199, 399, 499, 999, 1999], 'export': 'trades'}

'''
'''
trade               Trade module.
*   create-userdir      Create user-data directory.
*   new-config          Create new config
new-strategy        Create new strategy
++++++   download-data       Download backtesting data.
convert-data        Convert candle (OHLCV) data from one format to another.
convert-trade-data  Convert trade data from one format to another.
trades-to-ohlcv     Convert trade data to OHLCV data.
list-data           List downloaded data.
++++++  backtesting         Backtesting module.
++++++  backtesting-show    Show past Backtest results
++++++ backtesting-analysis     Backtest Analysis module.
edge                Edge module.
++++++  hyperopt            Hyperopt module.
++++++ hyperopt-list       List Hyperopt results
++++++ hyperopt-show       Show details of Hyperopt results
*   list-exchanges      Print available exchanges.
+++++  list-markets        Print markets on exchange.
++++   list-pairs          Print pairs on exchange.
+++++  list-strategies     Print available strategies.
list-freqaimodels   Print available freqAI models.
list-timeframes     Print available timeframes for the exchange.
++++  show-trades         Show trades.
test-pairlist       Test your pairlist configuration.
convert-db          Migrate database to different system
install-ui          Install FreqUI
+++++++  plot-dataframe      Plot candles with indicators.
++++++  plot-profit         Generate plot showing profits.
webserver           Webserver module.
strategy-updater    updates outdated strategyfiles to the current version
lookahead-analysis  Check for potential look ahead bias.
recursive-analysis  Check for potential recursive formula issue."""

{'command': 'download-data', 
'verbosity': 0, 
'logfile': None, 
'config': ['C:\\project\\trader\\user_data\\config.json'], 
'datadir': None, 
'user_data_dir': 'C:\\project\\trader\\user_data', 
'pairs': None, 
'pairs_file': None, 
'days': 3, 
'new_pairs_days': None,
'include_inactive': False, 
'timerange': None, 
'download_trades': False, 
'exchange': None, 
'timeframes': None, 
'erase': False, 
'dataformat_ohlcv': None, 
'dataformat_trades': None, 
'trading_mode': None, 
'prepend_data': False, 
'func': <function start_download_data at 0x000001B59F3B1120>}
'''

# {'command': 'list-exchanges', 'verbosity': 0, 'logfile': None,
#  'config': ['C:\\project\\trader\\user_data\\config.json'],
#  'datadir': None, 'user_data_dir': None, 'print_one_column': False,
#  'list_exchanges_all': False, 'func': <function start_list_exchanges at 0x00000247C8B609A0>}
