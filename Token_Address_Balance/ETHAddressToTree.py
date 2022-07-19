from requests import get
from treelib import Node, Tree
import time

API_KEY = "6MC13BXX3216TCPH2IX5DAISK22VGHWYW6"
BASE_URL = "https://api.etherscan.io/api"

address_list =[]

def make_api_url(module, action, address, **kwargs):
	url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={API_KEY}"

	for key, value in kwargs.items():
		url += f"&{key}={value}"

	return url

'''https://api.etherscan.io/api
   ?module=account
   &action=txlist
   &address=0xc5102fE9359FD9a28f877a67E36B0F050d81a3CC
   &startblock=0
   &endblock=99999999
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken'''

# List of transactions by an address across the blocks (contains to and from the address)
def get_transactions(address,depth):


    if depth==1:
        transactions_url = make_api_url("account","txlist", address, startblock=0, endblock=99999999, page=1, offset=100,sort="asc")
        response = get(transactions_url)
        data = response.json()["result"]

        to_addr = []
        for tx in data:
            to = tx["to"]
            from_addr = tx["from"]
            if (to!=address and to!=''):
                to_addr.append(to)
            #print("From:",from_addr)
            
        new = list(set(to_addr))
        

        for i in range(len(new)):
            if new[i] not in address_list:
                tree.create_node(new[i],new[i],address)
                address_list.append(new[i])

        return

    else:
        transactions_url = make_api_url("account","txlist", address, startblock=0, endblock=99999999, page=1, offset=100,sort="asc")
        response = get(transactions_url)
        data = response.json()["result"]

        to_addr = []
        for tx in data:
            to = tx["to"]
            from_addr = tx["from"]
            if (to!=address and to!=''):
                to_addr.append(to)
            #print("From:",from_addr)
            
        new = list(set(to_addr))

        for i in range(len(new)):
            if new[i] not in address_list:
                tree.create_node(new[i],new[i],address)
                address_list.append(new[i])
            get_transactions(new[i],depth-1)
        

        
        
    '''print(new)
    count=1

    tree = Tree()

    tree.create_node(address, count)
    #tree.create_node(new[0],2,parent=1)

    for i in range(len(new)):
        tree.create_node(new[i],count+i+1,count)
        

    tree.show()

    print(len(new))

        #print("To:",to)
        #print("From:", from_addr)
    #print(data[0]['to'])
'''




if __name__ == "__main__":
    address = "0x5b3256965e7C3cF26E11FCAf296DfC8807C01073"
    depth = 2

        #initial_list = get_transactions(address)

        #print(len(initial_list))

    tree = Tree()
    tree.create_node(address, address)

    address_list.append(address)
        #tree.create_node(new[0],2,parent=1)

    '''for i in range(len(initial_list)):
        tree.create_node(initial_list[i],initial_list[i],address)


        tree.show()'''

    start = time.time()
    get_transactions(address,depth)
    print(time.time()-start)
    tree.show()
