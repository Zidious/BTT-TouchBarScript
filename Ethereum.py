from pycoingecko import CoinGeckoAPI

# INSTANCE OF CoinGeckoAPI()
coinGecko = CoinGeckoAPI()


# ETH FUNCTION - PRICE, 24HVOL
def getETHPrice():
    getEth = coinGecko.get_coins_markets(ids='ethereum',
                                         vs_currency='usd')
    currentPrice = "{:,}".format(round(getEth[0]['current_price'], 2))
    totalVolume = "{:,}".format(round(getEth[0]['total_volume'], 2))
    return f"ETH: ${currentPrice} - " \
        f"24H VOL: ${totalVolume}"


print(getETHPrice())
