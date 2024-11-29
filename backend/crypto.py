import requests
import json
import time
from itertools import permutations
import networkx as nx

print("Crypto Currency Exchange Trading\n")

#Pulling crypto currencies from the api
url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum,bitcoin,ripple,cardano,bitcoin-cash,eos,litecoin&vs_currencies=eth,btc,xrp,ada,bch,eos,ltc"
req = requests.get(url)
data = json.loads(req.text)

#added a ticker_map so that I would have the ticker and not the full name
ticker_map = {
    'ethereum': 'eth',
    'bitcoin': 'btc',
    'ripple': 'xrp',
    'cardano': 'ada',
    'bitcoin-cash': 'bch',
    'eos': 'eos',
    'litecoin': 'ltc'
}

g = nx.DiGraph()

edges = []

#Parsing the JSON and entering the ticker symbol as the node name.
#i.e. 'bitcoin' ----> 'btc'
for node1, rates in data.items():
    ticker1 = ticker_map.get(node1, node1)
    for node2, weight in rates.items():
        ticker2 = ticker_map.get(node2, node2)
        weight = float(weight)
        edges.append((ticker1, ticker2, weight))

#This builds the graph
g.add_weighted_edges_from(edges)

#Initializing factor variables
min_factor = float('inf')
max_factor = float('-inf')

#Initializing path variables for the smallest and biggest factors
min_path = None
max_path = None 

#Querying all permutations of currency pairs
for c1, c2 in permutations(g.nodes,2):
    if c1 == c2:
        continue

    print(f"Paths from {c1} to {c2}--------------------------\n")
    least_path_weight = 99999999999
    least_path = ""
    try:
        for path in nx.all_simple_paths(g, source=c1, target=c2):

            #Setting a forward path weight
            forward_weight = 1
            for i in range(len(path) - 1):
                node1, node2 = path[i], path[i + 1]
                forward_weight *= g[node1][node2].get('weight', 1)

            print(path, forward_weight)

            #Excluding ada from the reverse lists
            reverse_path = list(reversed(path))
            if 'ada' in reverse_path:
                print(f"'ada' has no reverse path\n")
                continue

            #Setting a reverse path weight
            reverse_weight = 1
            reverse_exists = True
            for i in range(len(reverse_path) - 1):
                node1, node2 = reverse_path[i], reverse_path[i + 1]
                if not g.has_edge(node1, node2):
                    reverse_exists = False
                    break
                reverse_weight *= g[node1][node2].get('weight', 1)

            #Checking if the condition is false
            if not reverse_exists:
                print(f"Reverse path does not exist from {c2} to {c1}")
                continue

            print(reverse_path, reverse_weight)

            #Finding any disequilibrium between the weights
            factor = forward_weight * reverse_weight
            print(f"Dis-Equilibrium factor: {factor}\n")    

            #Update min_factor and max_factor
            if factor < min_factor:
                min_factor = factor
                min_path = (path, reverse_path)

            if factor > max_factor:
                max_factor = factor
                max_path = (path, reverse_path)

            if forward_weight < least_path_weight:
                least_path_weight = forward_weight
                least_path = path
        
        if least_path_weight != 99999999999:
            print(f"path {c1} to {c2}: {least_path}, total weight: {least_path_weight}\n")

    except nx.NetworkXNoPath:
        print("no paths exists")

print(f"Smallest Paths Weight Factor: {min_factor}")
print(f"Paths included: {min_path[0]} {min_path[1]}")
print(f"Greatest Paths Weight Factor: {max_factor}")
print(f"Paths Included: {max_path[0]} {max_path[1]}")
