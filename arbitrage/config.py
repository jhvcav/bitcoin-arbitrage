markets = [
    "KuCoinBTC-USDT",
    "KuCoinETH-USDT",
    "BinanceBTC-USDT",
    "BinanceETH-USDT",
]

# observers if any
observers = ["Logger", "TraderBotSim"]

market_expiration_time = 180  # 3 minutes
refresh_rate = 30  # Rafraîchissement toutes les 30 secondes

#### Trader Bot Config
# Access to Private APIs

kucoin_api_key = "675acaaff749cc0001bc1f50"
kucoin_api_secret = "46dbe691-8fcf-4177-9034-6d4d160ce41b"
kucoin_api_passphrase = "AZE4xyGY125!"

binance_api_key = "YOUR_BINANCE_API_KEY"
binance_api_secret = "YOUR_BINANCE_API_SECRET"

# SafeGuards
max_tx_volume = 0.5  # 0.5 ETH maximum
min_tx_volume = 0.01  # 0.01 ETH minimum
balance_margin = 0.1  # 10% de marge
profit_thresh = 10  # Minimum 10 USDT de profit
perc_thresh = 1  # Minimum 1% de profit

#### Emailer Observer Config
smtp_host = "smtp.gmail.com"
smtp_login = "jeanhugues.cavalie@gmail.com"
smtp_passwd = "vwkdpmzh125!"
smtp_from = "jeanhugues.cavalie@gmail.com"
smtp_to = "jhv.cavalie73@gmail.com"

#### XMPP Observer
xmpp_jid = "FROM@jabber.org"
xmpp_password = "FIXME"
xmpp_to = "TO@jabber.org"
