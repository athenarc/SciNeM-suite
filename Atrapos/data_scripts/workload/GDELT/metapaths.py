import sys   
import random
import pprint

graph = {
    'O': [ 'A' ],
    'A': [ 'O', 'L', 'P', 'S', 'T'],
    'L': [ 'A' ],
    'P': [ 'A', 'C' ],
    'S': [ 'A' ],
    'T': [ 'A' ],
    'C': [ 'P', 'I'],
    'I': [ 'C']
}

keys = list(graph.keys())
count = 0
metapaths = set()

while(True):
    node = random.choice(keys)
    metapath = str(node)
    length = random.randrange(3, 6)
    
    for i in range(1, length):
        node = random.choice(graph[node])
        metapath += node

    if (metapath in metapaths):
        count += 1
    
    if (count == 1000):
        break

    metapaths.add(metapath)

data = {
    'P': [],
    'O': [],
    'S': [],
    'T': [],
    'L': [],
    'C': [],
    'I': [],
}

for m in metapaths:

    if m.count("P") == 1:
        data['P'].append(m)
    if m.count("O") == 1:
        data['O'].append(m)
    if m.count("S") == 1:
        data['S'].append(m)
    if m.count("T") == 1:
        data['T'].append(m)
    if m.count("L") == 1:
        data['L'].append(m)
    if m.count("C") == 1:
        data['C'].append(m)
    if m.count("I") == 1:
        data['I'].append(m)
pp = pprint.PrettyPrinter(indent=4)

pp.pprint (data)
