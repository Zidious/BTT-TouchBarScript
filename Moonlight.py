from pycoingecko import CoinGeckoAPI

# INSTANCE OF CoinGeckoAPI()
coinGecko = CoinGeckoAPI()


# LX FUNCTION - PRICE, 24HVOL
def getLXPrice():
    getLX = coinGecko.get_coins_markets(ids='lux',
                                        vs_currency='usd')
    currentPrice = "{:,}".format(round(getLX[0]['current_price'], 8))
    totalVolume = "{:,}".format(round(getLX[0]['total_volume'], 2))
    return f"BTC: ${currentPrice} - " \
        f"24H VOL: ${totalVolume}"


print(getLXPrice())
