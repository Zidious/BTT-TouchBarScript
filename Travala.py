from pycoingecko import CoinGeckoAPI

# INSTANCE OF CoinGeckoAPI()
coinGecko = CoinGeckoAPI()


# AVA FUNCTION - PRICE, 24HVOL
def getAvaPrice():
    getAVA = coinGecko.get_coins_markets(ids='concierge-io',
                                         vs_currency='usd')
    currentPrice = "{:,}".format(round(getAVA[0]['current_price'], 4))
    marketCap = "{:,}".format(round(getAVA[0]['market_cap'], 2))
    totalVolume = "{:,}".format(round(getAVA[0]['total_volume'], 2))
    return f"${currentPrice} - MC: ${marketCap} - VOL: ${totalVolume}"


print(getAvaPrice())
