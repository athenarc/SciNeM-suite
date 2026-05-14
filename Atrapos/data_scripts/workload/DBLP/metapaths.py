import sys   
import random
import pprint

graph = {
    'A': [ 'P', 'O' ],
    'P': [ 'C', 'P', 'A', 'T', 'V' ],
    'C': [ 'P' ],
    'V': [ 'P' ],
    'T': [ 'P' ],
    'O': [ 'A' ]
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

data = { 'A': [], 'P': [], 'C': [], 'V': [], 'T': [], 'O': [] }

for m in metapaths:

    if m.count("A") == 1:
        data['A'].append(m)
    if m.count("P") == 1:
        data['P'].append(m)
    if m.count("C") == 1:
        data['C'].append(m)
    if m.count("V") == 1:
        data['V'].append(m)
    if m.count("T") == 1:
        data['T'].append(m)
    if m.count("O") == 1:
        data['O'].append(m)

pp = pprint.PrettyPrinter(indent=4)

pp.pprint (data)
