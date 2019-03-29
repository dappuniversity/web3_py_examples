from web3 import Web3

# Fill in your infura API key here
infura_url = "https://mainnet.infura.io/v3/953247d0c42b419aa3416810d625cc8c"
web3 = Web3(Web3.HTTPProvider(infura_url))

# get latest block number
print(web3.eth.blockNumber)

# get latest block
print(web3.eth.getBlock('latest'))

# get latest 10 blocks
latest = web3.eth.blockNumber
for i in range(0, 10):
  print(web3.eth.getBlock(latest - 10))

# get transaction from specific block
hash = '0x66b3fd79a49dafe44507763e9b6739aa0810de2c15590ac22b5e2f0a3f502073'
print(web3.eth.getTransactionByBlock(hash, 2))
