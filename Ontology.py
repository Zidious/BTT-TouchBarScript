from pycoingecko import CoinGeckoAPI

# INSTANCE OF CoinGeckoAPI()
coinGecko = CoinGeckoAPI()


# ONT FUNCTION - PRICE, 24HVOL
def getONTPrice():
    getONT = coinGecko.get_coins_markets(ids='ontology',
                                         vs_currency='usd')
    currentPrice = "{:,}".format(round(getONT[0]['current_price'], 2))
    totalVolume = "{:,}".format(round(getONT[0]['total_volume'], 2))
    return f"ONT: ${currentPrice} - " \
        f"24H VOL: ${totalVolume}"


print(getONTPrice())
