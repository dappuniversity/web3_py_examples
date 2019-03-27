from web3 import Web3

# Fill in your infura API key here
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY_GOES_HERE"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

# Fill in your account here
balance = web3.eth.getBalance("YOUR_ACCOUNT_GOES_HERE")
print(web3.fromWei(balance, "ether"))
