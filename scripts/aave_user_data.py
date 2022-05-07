from brownie import network, interface
from scripts.common import get_lending_pool, get_account
from web3 import Web3

def main():
    lending_pool =  get_lending_pool()
    account = get_account()

    (
        total_collateral_eth,
        total_debt_eth,
        available_borrow_eth,
        current_liquidation_threshold,
        tlv,
        health_factor,
    ) = lending_pool.getUserAccountData(account.address)
    available_borrow_eth = Web3.fromWei(available_borrow_eth, "ether")
    total_collateral_eth = Web3.fromWei(total_collateral_eth, "ether")
    total_debt_eth = Web3.fromWei(total_debt_eth, "ether")
    print(f"You have {total_collateral_eth} worth of ETH deposited.")
    print(f"You have {total_debt_eth} worth of ETH borrowed.")
    print(f"You can borrow {available_borrow_eth} worth of ETH.")
    print('Health factor:', health_factor)
    print('TLV:', tlv)
    print('Current liquidation threshold:', current_liquidation_threshold)
    return (float(available_borrow_eth), float(total_debt_eth))


