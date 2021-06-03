from pycoingecko import CoinGeckoAPI

# INSTANCE OF CoinGeckoAPI()
coinGecko = CoinGeckoAPI()


# AVA FUNCTION - PRICE, 24HVOL
def getBunnyPrice():
    getBunny = coinGecko.get_coins_markets(ids='pancake-bunny',
                                           vs_currency='usd')
    currentPrice = "{:,}".format(round(getBunny[0]['current_price'], 2))
    marketCap = "{:,}".format(round(getBunny[0]['market_cap'], 2))
    totalVolume = "{:,}".format(round(getBunny[0]['total_volume'], 2))
    return f"${currentPrice} - MC: ${marketCap} - VOL: ${totalVolume}"


print(getBunnyPrice())
