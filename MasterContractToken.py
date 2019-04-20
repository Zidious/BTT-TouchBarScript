from pycoingecko import CoinGeckoAPI

# INSTANCE OF CoinGeckoAPI()
coinGecko = CoinGeckoAPI()


# MCT FUNCTION - PRICE, 24HVOL
def getMCTPrice():
    getMCT = coinGecko.get_coins_markets(ids='master-contract-token',
                                         vs_currency='usd')
    currentPrice = "{:,}".format(round(getMCT[0]['current_price'], 8))
    totalVolume = "{:,}".format(round(getMCT[0]['total_volume'], 2))
    return f"MCT: ${currentPrice} - " \
        f"24H VOL: ${totalVolume}"


print(getMCTPrice())
