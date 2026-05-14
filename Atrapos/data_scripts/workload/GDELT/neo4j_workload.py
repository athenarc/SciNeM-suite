import random
import sys
import math
import numpy
p = float(sys.argv[1])

data = {   
    'P': {   
        'constraints':[1192, 7937, 403, 37, 1002, 1114, 7948, 7335, 103, 536, 1547, 7668, 414, 7780, 3459, 1091, 7557, 1080, 2248, 2237, 8098, 1237, 1226, 3669, 570, 392, 70, 547, 3403, 2780, 2681, 2669, 3436, 2891, 1102, 163, 2506, 4825, 3481, 28, 2548, 8048, 5447, 3002, 1203, 1670, 162, 1214, 7546, 27, 692, 2546, 4447, 614, 4780, 4014, 3470, 1255, 5458, 487, 481, 4669, 4558, 3448, 7942, 4335, 3169, 1869, 4224, 3414, 3025, 2670, 7977, 58, 3102, 2023, 1058, 559, 5535, 3558, 5603, 3947, 3392],
        # 'metapaths':  "PAS", "PASA", "APAS", "PALAP", "PALA", "PAL", "SAP", "SAPA", "SAPAL", "AOAP", "OAP", "PAO", "PAOA", "APA", "APAL", "LAPA"]
'metapaths': [   'ALAP',
                              'SAPA',
                              'APA',
                              'OAP',
                              'ASAP',
                              'APAL',
                              'LAPA',
                              'TAP',
                              'PALA',
                              'PAOA',
                              'OAPA',
                              'AOAP',
                              'PAS',
                              'TAPA',
                              'LAP',
                              'PAO',
                              'APAS',
                              'APAO',
                              'SAP',
                              'PAL',
                              'PASA']
    },
    'O': {   
        'constraints': [1336, 3, 114, 1114, 5318, 5674, 1, 5330, 203, 5463, 1780, 5552, 5002, 2392, 2447, 1525, 314, 281, 913, 592, 5396, 81, 403, 3392, 5429, 858, 5651, 647, 1669, 1036, 1025, 792, 2224, 1381, 1237, 1225, 3359, 2558, 5553, 1447, 5574, 1736, 492, 4503, 567, 5718, 5361, 980, 5638, 5554, 337, 5426, 4448, 1411, 1410, 1014, 2625, 4169, 5537, 5384, 803, 1720, 1292, 5533, 348, 3381, 1758, 1203, 1046, 359, 2740],
        # 'metapaths': [ "AOAT", "OATA", "AOA", "OAO", "OAOA", "AOAP", "AOAS", "TAOA", "TAO", "OAT", "OAP", "PAO", "OAPA", "PAOA", "SAOA", "SAOAT", "SAO", "OAS" ]
'metapaths': [   'LAO',
                              'AOA',
                              'OAP',
                              'SAOA',
                              'TAOA',
                              'TAO',
                              'AOAL',
                              'OAS',
                              'PAOA',
                              'OAPA',
                              'AOAP',
                              'SAO',
                              'PAO',
                              'ASAO',
                              'LAOA',
                              'APAO',
                              'OAL',
                              'OASA',
                              'AOAS',
                              'OALA',
                              'ALAO']
},    
    'S': {
        'constraints': [37, 1732, 1718, 325, 2156, 1438, 1591, 181, 1382, 1650, 2166, 1080, 1621, 1270, 792, 2107, 2087, 1982, 1745, 2125, 1702, 257, 2129, 1769, 1693, 1513, 283, 170, 1336, 403, 2102, 2014, 1458, 103, 1905, 1669, 1556, 1003, 378, 2131, 1835, 92, 2196, 2068, 2009, 1699, 1696, 570, 366, 339, 248, 1777, 1560, 1420, 115, 2039, 316, 265, 1646, 1482, 836, 331, 2075, 203, 1775, 1000, 81, 712, 696, 655, 436, 351, 31, 2152, 2096, 2084, 2073, 1709],
        # 'metapaths': [ "PAS", "PASA", "APAS", "SAP", "SAPA", "SAPAL", "AOAS", "SAP", "SAL", "SALA", "LAS", "LASA", "ALAS", "SAOA", "SAOAT", "SAO", "OAS"]
'metapaths': [   'SAPA',
                              'TASA',
                              'SAOA',
                              'ASAP',
                              'LASA',
                              'ASAL',
                              'OAS',
                              'ALAS',
                              'LAS',
                              'PAS',
                              'SAO',
                              'SALA',
                              'ASAO',
                              'APAS',
                              'OASA',
                              'TAS',
                              'ASA',
                              'AOAS',
                              'SAP',
                              'SAL',
                              'PASA']
},    
    'T': {
        'constraints': [1118, 518, 496, 1018, 807, 48, 1096, 330, 397, 1162, 463, 929, 996, 341, 829, 398, 1, 507, 974, 332, 685, 663, 365, 1262, 399, 383, 951, 519, 440, 4, 59, 1251, 874, 347, 485, 2, 349, 37, 338, 303, 1185, 348, 530, 339, 352, 81, 551, 896, 407, 430],
        # 'metapaths': [ "OATA", "OATAO", ]
        'metapaths': [   'TASA',
                              'TAOA',
                              'TAP',
                              'TAL',
                              'TAO',
                              'TALA',
                              'TAPA',
                              'TAS']
    },
    'L': {
        'constraints': [2200, 714, 692, 725, 1901, 869, 1912, 1848, 1002, 2278, 2258, 2500, 547, 1336, 1436, 1603, 15, 559, 880, 1967, 4, 2311, 1990, 170, 558, 1113, 1956, 81, 503, 514, 1114, 336, 536, 2422, 2300, 447, 225, 2134, 148, 525, 1915, 1935, 79, 1425, 2053, 1669, 2556, 2578, 2567, 2082, 2068, 1459, 1878, 936, 747, 1978, 1558, 2533, 2193, 781],
        # 'metapaths': [ "PALAP", "PALA", "PAL" ]
'metapaths': [   'ALAP',
                              'LAO',
                              'LASA',
                              'APAL',
                              'LAPA',
                              'TAL',
                              'ASAL',
                              'AOAL',
                              'ALAS',
                              'TALA',
                              'LAS',
                              'PALA',
                              'LAP',
                              'SALA',
                              'LAOA',
                              'ALA',
                              'OAL',
                              'OALA',
                              'SAL',
                              'PAL',
                              'ALAO']
},
}

        

queries = []
duplicates = 0
max_duplicates = 10

i = 0
while (True):
    i += 1

    if (i == 1):
        choice = "new"
    else: 
        choice = numpy.random.choice(["continue", "new"], p=[1-p, p])
    
    if (choice == "new"):
        entity = random.choice(list(data.keys()))
        constraint = random.choice(data[entity]['constraints'])
    # else:
    #     repeat = numpy.random.choice(["yes", "no"], p=[0.10, 0.90])
    #     if repeat == "yes":
    #         queries.append(queries[len(queries)-1])
    
    metapath = random.choice(data[entity]['metapaths'])
    q = metapath + "\t" + entity + ".id=\"" + str(constraint) + "\""
    
    # if q not in queries:
    queries.append(q)

    if (len(queries) == 200):
        break

for q in queries:
    print(q)
