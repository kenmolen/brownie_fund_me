from brownie import accounts, network, config, MockV3Aggregator

FORKED_LOCAL_ENVINRONMENTS = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000

def get_account():
    if  network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() not in FORKED_LOCAL_ENVINRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from":get_account()})
    price_feed_address = MockV3Aggregator[-1].address
    print("Mocks deployed")


