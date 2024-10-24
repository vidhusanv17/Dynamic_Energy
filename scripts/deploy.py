from web3 import Web3
import json

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))

# Load your contract ABI and bytecode
with open('contracts/MyContract.json') as f:
    contract_data = json.load(f)

abi = contract_data['abi']
bytecode = contract_data['bytecode']

# Set up the contract
MyContract = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get the account to deploy the contract
account = w3.eth.accounts[0]

# Build the transaction
tx_hash = MyContract.constructor().transact({'from': account})

# Wait for the transaction to be mined
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

print(f'Contract deployed at address: {tx_receipt.contractAddress}')
