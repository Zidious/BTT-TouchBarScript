from pycoingecko import CoinGeckoAPI

# INSTANCE OF CoinGeckoAPI()
coinGecko = CoinGeckoAPI()


# AVA FUNCTION - PRICE, 24HVOL
def getBTCPrice():
    getAVA = coinGecko.get_coins_markets(ids='bitcoin',
                                         vs_currency='usd')
    currentPrice = "{:,}".format(round(getAVA[0]['current_price'], 2))
    totalVolume = "{:,}".format(round(getAVA[0]['total_volume'], 2))
    return f"BTC: ${currentPrice} - " \
        f"24H VOL: ${totalVolume}"


print(getBTCPrice())
