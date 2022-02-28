from scripts.helpful_scripts import get_account
from brownie import OurToken, network, config
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def deploy_erc20():
    account = get_account()
    ourToken = OurToken.deploy(
        initial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )

    print("Deployed ERC20 Token!")
    print(ourToken.name())
    return ourToken


def main():
    deploy_erc20()
