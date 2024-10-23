from web3 import Web3
import json

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))

# Replace with your contract address
contract_address = 'YOUR_CONTRACT_ADDRESS'

# Load your contract ABI
with open('contracts/MyContract.json') as f:
    contract_data = json.load(f)

abi = contract_data['abi']

# Set up the contract instance
MyContract = w3.eth.contract(address=contract_address, abi=abi)

# Call the message function
message = MyContract.functions.message().call()
print(f'Message from contract: {message}')
