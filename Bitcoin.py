from pycoingecko import CoinGeckoAPI

# INSTANCE OF CoinGeckoAPI()
coinGecko = CoinGeckoAPI()


# AVA FUNCTION - PRICE, 24HVOL
def getBTCPrice():
    getBTC = coinGecko.get_coins_markets(ids='bitcoin',
                                         vs_currency='usd')
    currentPrice = "{:,}".format(round(getBTC[0]['current_price'], 2))
    marketCap = "{:,}".format(round(getBTC[0]['market_cap'], 2))
    totalVolume = "{:,}".format(round(getBTC[0]['total_volume'], 2))
    return f"${currentPrice} - MC: ${marketCap} - VOL: ${totalVolume}"


print(getBTCPrice())
