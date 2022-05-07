from brownie import config, interface, network
from web3 import Web3
from scripts.get_wavax import get_avax
from scripts.common import get_account, get_lending_pool

amount = Web3.toWei(1, "ether")


def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["usdt_token"]
    if network.show_active() in ["mainnet-fork"]:
        get_avax(account=account)
    lending_pool = get_lending_pool()
    approve_erc20(amount, lending_pool.address, erc20_address, account)
    print("Depositing...")
    lending_pool.deposit(erc20_address, 1000 * 10 ** 6, account.address, 0, {
        "from": account, 'gas_limit': 8000000})
    print("Deposited", amount)


def approve_erc20(amount, lending_pool_address, erc20_address, account):
    print("Approving ERC20...")
    erc20 = interface.IERC20(erc20_address)
    tx_hash = erc20.approve(lending_pool_address, amount, {"from": account})
    tx_hash.wait(1)
    print("Approved!")
    return True

if __name__ == "__main__":
    main()
