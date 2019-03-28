from web3 import Web3

# Fill in your infura API key here
# infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY_GOES_HERE"
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = '0x035533aBAD495C581379005262D49b4dF09e925A'
account_2 = '0xBBCF4dC04B5d8E3D33ffec77B25764D25Abb4999'
private_key = '80b3b0e00441d57befb2428df63adffed612dba093fd750844155ad0fe00eb17'

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))

