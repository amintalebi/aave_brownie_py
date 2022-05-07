from brownie import config, network, interface
from scripts.common import get_account

def main():
    account = get_account()
    lending_pool_configurator = get_lending_pool_configurator()
    lending_pool_configurator.setPoolPause(False, {"from": account})
    print("Unpaused lending pool")

def get_lending_pool_configurator():
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )
    lending_pool_configurator_address = lending_pool_addresses_provider.getLendingPoolConfigurator()
    lending_pool_configurator = interface.ILendingPoolConfigurator(lending_pool_configurator_address)
    return lending_pool_configurator
