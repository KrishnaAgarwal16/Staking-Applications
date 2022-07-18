from requests import get
from treelib import Node, Tree

API_KEY = "6MC13BXX3216TCPH2IX5DAISK22VGHWYW6"
BASE_URL = "https://api.etherscan.io/api"

def make_api_url(module, action, address, **kwargs):
	url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={API_KEY}"

	for key, value in kwargs.items():
		url += f"&{key}={value}"

	return url

'''https://api.etherscan.io/api
   ?module=account
   &action=tokentx
   &contractaddress=0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2
   &address=0x4e83362442b8d1bec281594cea3050c8eb01311c
   &page=1
   &offset=100
   &startblock=0
   &endblock=27025780
   &sort=asc
   &apikey=YourApiKeyToken'''


def get_erc20_token_transfers(contract,address):
    transfer_url = make_api_url("account","tokentx", address, contractaddress=contract, page=1,offset=100,startblock=0,endblock=25025780,sort="asc")
    response = get(transfer_url)
    #print(transfer_url)
    data = response.json()["result"]
    to_addr = []
    for tx in data:
        to = tx["to"]
        from_addr = tx["from"]
        if (to!="0xb4a81261b16b92af0b9f7c4a83f1e885132d81e4"):
            to_addr.append(to)
        
    new = list(set(to_addr))
    #return new
    #print(new[0])
    count=1

    tree = Tree()

    tree.create_node(address, count)
    #tree.create_node(new[0],2,parent=1)

    for i in range(len(new)):
        tree.create_node(new[i],count+i+1,count)
        

    tree.show()

        #print("To:",to)
        #print("From:", from_addr)
    #print(data[0]['to'])





address = "0xb4a81261b16b92af0b9f7c4a83f1e885132d81e4"
contract = "0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE"
get_erc20_token_transfers(contract,address)
