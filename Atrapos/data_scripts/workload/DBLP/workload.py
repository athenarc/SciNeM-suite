import random
import sys
import math
import numpy
import pandas as pd
import scipy.stats as stats


dataset = "DBLP-0.6"
output = sys.argv[2]
distribution = sys.argv[3]

p = float(sys.argv[1])
m = 0
s = 10
zipf_alpha = 2

metapaths = {   'A': [   
'VPAPV',
             'PCPAP',
             'VPVPA',
             'TPAPV',
             'CPAPC',
             'PAPC',
             'PCPAO',
             'CPAP',
             'OAPVP',
             'APVPC',
             'APTPC',
             'VPAPC',
             #'VPTPA',
             'OAPV',
             'APV',
             #'TPTPA',
             'CPAPV',
             'APTP',
             'TPAP',
             'CPAO',
             'TPCPA',
             'APCPT',
             'VPA',
             'APT',
             #'CPTPA',
             'TPVPA',
             'VPCPA',
             'APTPV',
             'PVPA',
             #'PTPAP',
             'TPA',
             'OAPTP',
             'APC',
             'CPA',
             'CPVPA',
             'APVPT',
             'VPAO',
             'CPCPA',
             'PAO',
             'PAPVP',
             'PVPAO',
             'APCPV',
             'OAPT',
             #'PAPTP',
             'OAP',
             'APCP',
             'VPAP',
             #'PTPAO',
             'OAPC',
             'APTPT',
             'APVP',
             'TPAPT',
             'OAO',
             'PAP',
             'OAPCP',
             'TPAO',
             'PAPT',
             #'PTPA',
             'TPAPC',
             'PAPCP',
             'PCPA'],
    'C': [   
    'PVPC',
             'CPTPV',
             'PCPAP',
             'VPTPC',
             'PAPC',
             'PCPAO',
             'TPCPT',
             'CPAP',
             'CPVP',
             'APVPC',
             'PCPV',
             'APTPC',
             'PVPCP',
             'CPTP',
             'PCP',
             'VPCPV',
             'VPAPC',
             'TPCP',
             'TPC',
             'CPAPA',
             'APCPA',
             'CPAOA',
             'CPAPV',
             'TPCPV',
             'PCPT',
             'CPAO',
             'TPCPA',
             'APCPT',
             'CPVPT',
             'CPTPA',
             'CPTPT',
             'CPV',
             'VPCPA',
             'TPVPC',
             'APC',
             'CPA',
             'CPT',
             'CPVPA',
             'VPCPT',
             'VPVPC',
             'APCPV',
             'PTPC',
             'APCP',
             'OAPC',
             'OAPCP',
             'VPC',
             'VPCP',
             'CPVPV',
             'TPTPC',
             'PCPTP',
             'AOAPC',
             'TPAPC',
             'PAPCP',
             'PCPA'],
    'O': [   
    'PAPAO',
             'APAO',
             'OAPA',
             'PCPAO',
             'OAPVP',
             'AOA',
             'VPAOA',
             'OAPV',
             #'PAOAP',
             'CPAOA',
             'CPAO',
             'PAOA',
             'OAPTP',
             'OAPAP',
             'VPAO',
             'AOAP',
             'PAO',
             'PVPAO',
             'OAPT',
             'OAP',
             'AOAPA',
             'TPAOA',
             'PTPAO',
             'OAPC',
             'APAOA',
             'OAPCP',
             'AOAPT',
             'AOAPV',
             'AOAPC',
             'TPAO'],
    'T': [   
             'CPTPV',
             'VPTPC',
             'TPAPV',
             #'PTPVP',
             'TPV',
             'APTPC',
             'PTPV',
             'CPTP',
             'TPVP',
             'VPTPA',
             'TPCP',
             'TPC',
             'APTP',
             'TPAP',
             'TPCPV',
             'PTP',
             'PCPT',
             'TPCPA',
             'APCPT',
             'APT',
             'CPVPT',
             'TPAPA',
             'CPTPA',
             'TPVPA',
             'TPVPC',
             'APTPV',
             #'PTPAP',
             'TPA',
             #'OAPTP',
             'TPVPV',
             'VPTPV',
             'CPT',
             'APVPT',
             'VPCPT',
             'CPCPT',
             'OAPT',
             #'PAPTP',
             #'PVPTP',
             'PTPC',
             'TPCPC',
             'TPAOA',
             #'PTPAO',
             'CPTPC',
             'VPT',
             'APAPT',
             'PVPT',
             'VPVPT',
             'VPTP',
             'AOAPT',
             'PCPTP',
             'TPAO',
             'PAPT',
             'PTPA',
             'TPAPC'],
    'V': [   
    'PVPC',
             #'CPTPV',
             #'VPTPC',
             'TPAPV',
             'OAPVP',
             'CPVP',
             #'PTPVP',
             'TPV',
             'APVPC',
             'PCPV',
             'PVPCP',
             'PTPV',
             'APVPA',
             'VPAOA',
             'VPAPC',
             'TPVP',
             'VPTPA',
             'OAPV',
             'APV',
             'CPAPV',
             'TPCPV',
             'VPCPC',
             'VPA',
             'PVP',
             'VPAPA',
             'CPVPT',
             'VPTPT',
             'CPV',
             'TPVPA',
             'VPCPA',
             'TPVPC',
             'APTPV',
             'PVPA',
             'CPVPA',
             'APVPT',
             'CPCPV',
             'VPAO',
             'VPCPT',
             'PAPVP',
             'PVPAO',
             'APCPV',
             #'PVPTP',
             'CPVPC',
             'VPAP',
             'TPVPT',
             'APVP',
             'VPT',
             'TPTPV',
             'VPC',
             'VPCP',
             'PVPT',
             'APAPV',
             'VPTP',
             'AOAPV'
]}

def zipf_distribution(a, size):
    k = numpy.linspace(1, size, size)
    p = stats.zipf.pmf(k, a=a)
    numpy.random.shuffle(p)
    return p
  
def get_ids(relation, start, end):  
  df = pd.read_csv("../../../data/" + dataset + "/relations/" + relation + ".crs", sep='\t', header=None, names=['src',  'dest'])
  df_counts = df['src'].value_counts()[start:end].index.tolist()
  return df_counts

normal_distribution = stats.norm(m, s)

constraints = { 'A': [], 'P': [], 'C': [], 'V': [], 'T': [], 'O': [] }

constraints["A"] = get_ids("AP", 200, 300)
constraints["V"] = get_ids("VP", 200, 300)
constraints["T"] = get_ids("TP", 600, 700)

# constraints["A"] = get_ids("AP", 100, 200)
# constraints["V"] = get_ids("VP", 100, 200)
# constraints["T"] = get_ids("TP", 400, 500)

constraints["C"] = get_ids("CP", 0, 50)
constraints["O"] = get_ids("OA", 0, 50)

for fileId in range (0, 30):
#   print(fileId)

  constraints_normal = { 'A': [], 'P': [], 'C': [], 'V': [], 'T': [], 'O': [] }
  metapaths_normal = { 'A': [], 'P': [], 'C': [], 'V': [], 'T': [], 'O': [] }
  constraints_zipf= { 'A': [], 'P': [], 'C': [], 'V': [], 'T': [], 'O': [] }
  metapaths_zipf = { 'A': [], 'P': [], 'C': [], 'V': [], 'T': [], 'O': [] }
  
  metapaths_normal["A"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(metapaths["A"]))) )
  metapaths_normal["V"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(metapaths["V"]))) )
  metapaths_normal["T"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(metapaths["T"]))) )
  metapaths_normal["C"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(metapaths["C"]))) )
  metapaths_normal["O"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(metapaths["O"]))) )

  metapaths_zipf["A"] = zipf_distribution(zipf_alpha, len(metapaths["A"]))
  metapaths_zipf["V"] = zipf_distribution(zipf_alpha, len(metapaths["V"]))
  metapaths_zipf["T"] = zipf_distribution(zipf_alpha, len(metapaths["T"]))
  metapaths_zipf["C"] = zipf_distribution(zipf_alpha, len(metapaths["C"]))
  metapaths_zipf["O"] = zipf_distribution(zipf_alpha, len(metapaths["O"]))
  
  constraints_normal["A"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(constraints["A"]))))
  constraints_normal["V"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(constraints["V"]))))
  constraints_normal["T"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(constraints["T"]))))
  constraints_normal["C"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(constraints["C"]))))
  constraints_normal["O"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(constraints["O"]))))

  constraints_zipf["A"] = zipf_distribution(zipf_alpha, len(constraints["A"]))
  constraints_zipf["V"] = zipf_distribution(zipf_alpha, len(constraints["V"]))
  constraints_zipf["T"] = zipf_distribution(zipf_alpha, len(constraints["T"]))
  constraints_zipf["C"] = zipf_distribution(zipf_alpha, len(constraints["C"]))
  constraints_zipf["O"] = zipf_distribution(zipf_alpha, len(constraints["O"]))
  
  i = 0
  queries = []
  while (True):
      i += 1

      if (i == 1):
          choice = "new"
      else:           choice = numpy.random.choice(["continue", "new"], p=[1-p, p])

      if (choice == "new"):
          entity = random.choice(list(metapaths.keys()))
          if distribution == 'normal':
              constraint = random.choices(constraints[entity], weights=constraints_normal[entity])[0]
          elif distribution == 'uniform':
              constraint = random.choice(constraints[entity])
          elif distribution == 'zipf':
              constraint = random.choices(constraints[entity], weights=constraints_zipf[entity])[0]
          else:
              print("Unknown distribution given")
              sys.exit(-1)
              
      if distribution == 'normal':
          metapath = random.choices(metapaths[entity], weights=metapaths_normal[entity])[0]
#           metapath = normal_choice(m, s, metapaths[entity])
      elif distribution == 'uniform':
          metapath = random.choice(metapaths[entity])
      elif distribution == 'zipf':
          metapath = random.choices(metapaths[entity], weights=metapaths_zipf[entity])[0]
      else:
          print("Unknown distribution given")
          sys.exit(-1)
          
      q = metapath + "\t" + entity + ".id=\"" + str(constraint) + "\""

      queries.append(q)

      if (len(queries) == 500):
          break

  fd = open(output + "/" + str(fileId) + ".csv", "w")

  random.shuffle(queries)
  for q in queries:
    fd.write(q + "\n")
  
  fd.close()
  
