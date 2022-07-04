from requests import get
from datetime import datetime

API_KEY = "W8JGDK5T85ZPUW3PPI9FISYRKNXHNYU6HW"
BASE_URL = "https://api.etherscan.io/api"

VALUE = 10**18

def make_api_url(module, action, contract, address, **kwargs):
	url = BASE_URL + f"?module={module}&action={action}&contractaddress={contract}&address={address}&apikey={API_KEY}"

	for key, value in kwargs.items():
		url += f"&{key}={value}"

	return url

'''https://api.etherscan.io/api
   ?module=account
   &action=tokenbalance
   &contractaddress=0x57d90b64a1a57749b0f932f1a3395792e12e7055
   &address=0xe04f27eb70e025b78871a2ad7eabe85e61212761
   &tag=latest&apikey=YourApiKeyToken'''

def get_account_balance(contract, address):
	balance_url = make_api_url("account", "tokenbalance", contract, address, tag="latest")
	response = get(balance_url)
	data = response.json()

	value = int(data["result"])/VALUE
	return value

address = "0xb4a81261b16b92af0b9f7c4a83f1e885132d81e4"
contract = "0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE"

print(get_account_balance(contract,address))