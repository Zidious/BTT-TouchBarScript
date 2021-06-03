from pycoingecko import CoinGeckoAPI

# INSTANCE OF CoinGeckoAPI()
coinGecko = CoinGeckoAPI()


# ETH FUNCTION - PRICE, 24HVOL
def getASSPrice():
    getAss = coinGecko.get_coins_markets(ids='australian-safe-shepherd',
                                         vs_currency='usd')
    currentPrice = "{:,}".format(round(getAss[0]['current_price'], 10))
    totalVolume = "{:,}".format(round(getAss[0]['market_cap'], 2))
    return f"ETH: ${currentPrice} - " \
        f"MC: ${totalVolume}"


print(getASSPrice())
