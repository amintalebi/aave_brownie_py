from brownie import config, interface, network
from web3 import Web3
from scripts.common import get_account, get_lending_pool

amount = Web3.toWei(0.1, "ether")

def main():
    account = get_account()
    lending_pool = get_lending_pool()
    borrowable_eth, total_debt_eth = get_borrowable_data(lending_pool, account)
    print(f"LETS BORROW IT ALL")
    erc20_eth_price = get_asset_price()
    # 1 ETH = 3000
    # amount = x
    amount_erc20_to_borrow = (erc20_eth_price) * (borrowable_eth * 0.80)
    print(f"We are going to borrow {amount_erc20_to_borrow} USDT")
    borrow_erc20(lending_pool, amount_erc20_to_borrow, account)
    get_borrowable_data(lending_pool, account)


def approve_erc20(amount, lending_pool_address, erc20_address, account):
    print("Approving ERC20...")
    erc20 = interface.IERC20(erc20_address)
    tx_hash = erc20.approve(lending_pool_address, amount, {"from": account})
    tx_hash.wait(1)
    print("Approved!")
    return True


def get_borrowable_data(lending_pool, account):
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
    return (float(available_borrow_eth), float(total_debt_eth))


def borrow_erc20(lending_pool, amount, account, erc20_address=None):
    erc20_address = (
        erc20_address
        if erc20_address
        else config["networks"][network.show_active()]["usdt_token"]
    )
    # 2 is variable interest rate
    # 0 is the referral code
    print('actual amount', amount * 10 ** 6)
    transaction = lending_pool.borrow(
        erc20_address,
        amount * 10 ** 6,
        2,
        0,
        account.address,
        {"from": account},
    )
    transaction.wait(1)
    print(f"Congratulations! We have just borrowed {amount}")


def get_asset_price():
    # For mainnet we can just do:
    # return Contract(f"{pair}.data.eth").latestAnswer() / 1e8
    eth_usd_price_feed = interface.AggregatorV3Interface(
        config["networks"][network.show_active()]["eth_usd_price_feed"]
    )
    return float(eth_usd_price_feed.latestRoundData()[1]) / 1e8


def repay_all(amount, lending_pool, account):
    approve_erc20(
        Web3.toWei(amount, "ether"),
        lending_pool,
        config["networks"][network.show_active()]["aave_dai_token"],
        account,
    )
    tx = lending_pool.repay(
        config["networks"][network.show_active()]["aave_dai_token"],
        Web3.toWei(amount, "ether"),
        1,
        account.address,
        {"from": account},
    )
    tx.wait(1)
    print("Repaid!")


if __name__ == "__main__":
    main()
