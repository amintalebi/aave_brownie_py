from scripts.common import get_aave_oracle

def main():
    aave_oracle = get_aave_oracle()
    base_currency =  aave_oracle.BASE_CURRENCY()
    base_currency_unit = aave_oracle.BASE_CURRENCY_UNIT()
    print('base_currency:', base_currency)
    print('base currency unit:', base_currency_unit)
    print('eth price', aave_oracle.getAssetPrice("0x9668f5f55f2712Dd2dfa316256609b516292D554"))
    print('source of eth price', aave_oracle.getSourceOfAsset("0x9668f5f55f2712Dd2dfa316256609b516292D554")) 
    print('usdt price', aave_oracle.getAssetPrice("0x02823f9B469960Bb3b1de0B3746D4b95B7E35543"))
    print('source of usdt price', aave_oracle.getSourceOfAsset("0x02823f9B469960Bb3b1de0B3746D4b95B7E35543"))     
