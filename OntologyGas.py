from pycoingecko import CoinGeckoAPI

# INSTANCE OF CoinGeckoAPI()
coinGecko = CoinGeckoAPI()


# ONG FUNCTION - PRICE, 24HVOL
def getONTPrice():
    getONG = coinGecko.get_coins_markets(ids='ong',
                                         vs_currency='usd')
    currentPrice = "{:,}".format(round(getONG[0]['current_price'], 2))
    totalVolume = "{:,}".format(round(getONG[0]['total_volume'], 2))
    return f"ONG: ${currentPrice} - " \
        f"24H VOL: ${totalVolume}"


print(getONTPrice())
