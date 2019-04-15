from pycoingecko import CoinGeckoAPI

# INSTANCE OF CoinGeckoAPI()
coinGecko = CoinGeckoAPI()


# NEO FUNCTION - PRICE, 24HVOL
def getNEOPrice():
    getNeo = coinGecko.get_coins_markets(ids='neo',
                                         vs_currency='usd')
    currentPrice = "{:,}".format(round(getNeo[0]['current_price'], 2))
    totalVolume = "{:,}".format(round(getNeo[0]['total_volume'], 2))
    return f"NEO: ${currentPrice} - " \
        f"24H VOL: ${totalVolume}"


print(getNEOPrice())
