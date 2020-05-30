from pycoingecko import CoinGeckoAPI

# INSTANCE OF CoinGeckoAPI()
coinGecko = CoinGeckoAPI()


# GAS FUNCTION - PRICE, 24HVOL
def getGASPrice():
    getGas = coinGecko.get_coins_markets(ids='gas',
                                         vs_currency='usd')
    currentPrice = "{:,}".format(round(getGas[0]['current_price'], 2))
    totalVolume = "{:,}".format(round(getGas[0]['total_volume'], 2))
    return f"NEO: ${currentPrice} - " \
        f"24H VOL: ${totalVolume}"


print(getGASPrice())
