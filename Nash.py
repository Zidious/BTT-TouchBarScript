from pycoingecko import CoinGeckoAPI

# INSTANCE OF CoinGeckoAPI()
coinGecko = CoinGeckoAPI()


# NASH FUNCTION - PRICE, 24HVOL
def getNEXPrice():
    getNex = coinGecko.get_coins_markets(ids='neon-exchange',
                                         vs_currency='usd')
    currentPrice = "{:,}".format(round(getNex[0]['current_price'], 2))
    totalVolume = "{:,}".format(round(getNex[0]['total_volume'], 2))
    return f"NEX: ${currentPrice} - " \
        f"24H VOL: ${totalVolume}"


print(getNEXPrice())
