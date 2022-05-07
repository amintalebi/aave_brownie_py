from scripts.common import get_aave_ui_pool_data_provider, lending_pool_address_provider

def main():
    ui_pool_data_provider = get_aave_ui_pool_data_provider()
    print(ui_pool_data_provider.getReservesData(lending_pool_address_provider()))
