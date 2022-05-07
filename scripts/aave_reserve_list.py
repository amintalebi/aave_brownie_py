from brownie import interface
from scripts.common import get_lending_pool

def main():
    reserves = get_lending_pool().getReservesList()
    for asset in reserves:
        erc20 = interface.IERC20(asset)
        print(erc20.name(), erc20.decimals(), asset)
