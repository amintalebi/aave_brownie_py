from brownie import accounts, config, network, interface


def main():
    """
    Runs the get_avax function to get AVAX
    """
    get_avax()


def get_avax(account=None):
    """
    Mints WAVAX by depositing AVAX.
    """
    account = (
        account if account else accounts.add(config["wallets"]["from_key"])
    )  # add your keystore ID as an argument to this call
    weth = interface.WethInterface(
        config["networks"][network.show_active()]["wavax_token"]
    )
    amount = 10
    tx = weth.deposit({"from": account, "value": amount * 1e18})
    print(f"Received {amount} WAVAX")
    return tx
