from pycoingecko import CoinGeckoAPI

# INSTANCE OF CoinGeckoAPI()
coinGecko = CoinGeckoAPI()


# AVA FUNCTION - PRICE, 24HVOL
def getCakePrice():
    getCake = coinGecko.get_coins_markets(ids='pancakeswap-token',
                                          vs_currency='usd')
    currentPrice = "{:,}".format(round(getCake[0]['current_price'], 2))
    marketCap = "{:,}".format(round(getCake[0]['market_cap'], 2))
    totalVolume = "{:,}".format(round(getCake[0]['total_volume'], 2))
    return f"${currentPrice} - MC: ${marketCap} - VOL: ${totalVolume}"


print(getCakePrice())
