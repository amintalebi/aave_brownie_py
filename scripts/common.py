from brownie import accounts, config, network, interface

def get_account():
    if network.show_active() in ["hardhat", "development", "mainnet-fork"]:
        return accounts[0]
    if network.show_active() in config["networks"]:
        account = accounts.add(config["wallets"]["from_key"])
        return account
    return None


def lending_pool_address_provider():
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )
    return lending_pool_addresses_provider

def get_lending_pool():
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )
    lending_pool_address = lending_pool_addresses_provider.getLendingPool()
    lending_pool = interface.ILendingPool(lending_pool_address)
    # print('lending_pool_addresses_provider:', lending_pool_addresses_provider)
    # print('lending_pool_address           :', lending_pool_address)
    return lending_pool

def get_aave_oracle():
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )
    price_oracle_address = lending_pool_addresses_provider.getPriceOracle()
    aave_oracle =  interface.IAaveOracle(price_oracle_address)
    return aave_oracle


def get_aave_ui_pool_data_provider():
    ui_pool_data_provider =  interface.IUiPoolDataProviderV2(
        config["networks"][network.show_active()]["ui_pool_data_provider"]
    )
    return ui_pool_data_provider