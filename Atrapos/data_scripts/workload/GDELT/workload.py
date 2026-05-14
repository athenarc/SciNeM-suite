import random
import sys
import math
import numpy
import pandas as pd
import scipy.stats as stats


dataset = "GDELT-0.6"
output = sys.argv[2]
distribution = sys.argv[3]

p = float(sys.argv[1])
m = 0
s = 10
zipf_alpha = 2

metapaths = {   'C': [   'PAPCP',
             'APCI',
             'CPATA',
             'CPALA',
             'ICI',
             'APC',
             'TAPC',
             'PCPAP',
             'ICPAL',
             'PCPAS',
             'ATAPC',
             'ICP',
             'SAPCP',
             'LAPCI',
             'CPASA',
             'PCPAT',
             'PAPCI',
             'LAPCP',
             'OAPCI',
             'CPAP',
             'PCPAL',
             'PCP',
             'CPAT',
             'ICPAP',
             'PCI',
             'TAPCI',
             'ICPAT',
             'CPAPA',
             'ICPA',
             'LAPC',
             'PCPA',
             'CPAL',
             'OAPCP',
             'SAPC',
             'ASAPC',
             'PAPC',
             'CPA',
             'APCP',
             'TAPCP',
             'OAPC',
             'CPAO',
             'SAPCI'],
    'I': [   'APCI',
             'CPCI',
             'CPCIC',
             'ICPAL',
             'APCIC',
             'PCPCI',
             'ICP',
             'CICPC',
             'LAPCI',
             'PAPCI',
             'OAPCI',
             'ICPCP',
             'PCIC',
             'ICPAP',
             'CICP',
             'PCI',
             'PCICP',
             'TAPCI',
             'ICPAT',
             'CIC',
             'ICPA',
             'CICPA',
             'ICPC',
             'SAPCI'],
    'L': [   'LAPA',
             'ALA',
             'LATAP',
             'CPALA',
             'OALAT',
             'LATAS',
             'OAOAL',
             'LAO',
             'ATAL',
#              'ALASA',
             'LASAS',
             'ICPAL',
             'ALAO',
             'OATAL',
             'TATAL',
             'OAL',
             'SAL',
             'ASAL',
             'LATAT',
             'TALAS',
             'SALAS',
             'SALAP',
             'TAOAL',
             'LAT',
             'LAPAO',
             'LAOA',
             'LAOAO',
             'LAPCI',
             'LAOAS',
             'PALAS',
             'LAPCP',
             'AOAL',
             'LAPAP',
             'LASA',
             'SATAL',
             'PALAO',
             'OALAS',
             'LASAP',
#              'AOALA',
             'OALAP',
#              'ALATA',
             'PCPAL',
             'ALAS',
             'PATAL',
             'TALAT',
             'LAOAT',
             'OASAL',
#              'ATALA',
             'TAL',
             'LAPC',
             'OAPAL',
             'TASAL',
             'TALAO',
             'SALAT',
             'TALAP',
             'LATAO',
             'ALAT',
             'CPAL',
             'LAS',
             'LASAO',
             'PALA',
             'LATA',
             'TALA',
             'PALAT',
             'LAP',
             'OALAO',
             'LAPAT',
             'OALA',
             'SALAO',
             'PAL',
             'LAOAP',
#              'ALAOA',
#              'ASALA',
             'SALA',
             'SASAL',
             'PAOAL',
             'PALAP',
             'PASAL',
             'LASAT'],
    'O': [   'SASAO',
             'OASAS',
             'ASAO',
             'OAPAS',
             'PAOAT',
             'SAO',
             'OALAT',
             'LAO',
             'PAOAP',
#              'AOATA',
             'SAOA',
             'LALAO',
             'SATAO',
             'ALAO',
             'OATAL',
             'TASAO',
             'APAO',
             'OAL',
             'TAOAP',
             'OATAS',
             'LAOAL',
             'AOAT',
             'TAOAL',
             'LAPAO',
             'LAOA',
             'TATAO',
             'AOAP',
             'PAOA',
             'OAT',
             'LAOAS',
             'AOAL',
             'SAOAP',
             'OAPCI',
             'PALAO',
             'OALAS',
#              'AOALA',
             'OAS',
             'OALAP',
             'TAOAT',
             'SAOAT',
             'OAPA',
             'AOA',
             'TAO',
             'OALAL',
             'LAOAT',
             'PATAO',
             'TAPAO',
             'OASAL',
#              'AOASA',
             'OASA',
             'TAOA',
             'TAOAS',
             'OAP',
             'OAPAT',
             'OAPAL',
             'TALAO',
#              'ATAOA',
             'OATAT',
             'LATAO',
             'OAPAP',
             'OAPCP',
             'ATAO',
             'LASAO',
             'OATAP',
             'OASAT',
             'OALA',
             'SALAO',
             'LAOAP',
             'PAO',
#              'ALAOA',
             'PAOAL',
#              'AOAPA',
             'OAPC',
             'CPAO',
             'OATA',
             'AOAS'],
    'P': [   'PATAS',
             'LAPA',
             'OAPAS',
             'APCI',
             'CPATA',
             'LATAP',
             'PAOAT',
             'CPALA',
             'CPCI',
             'TAP',
             'APC',
             'PATAT',
             'CPCIC',
             'TAPC',
#              'TASAP',
             'SAP',
             'ICPAL',
             'APCIC',
             'APAO',
             'PALAL',
             'ATAPC',
             'ASAP',
             'TAOAP',
             'ICP',
             'PASAT',
             'CICPC',
             'SALAP',
             'PCICI',
             'PAT',
             'LAPAO',
             'TAPA',
             'LAPCI',
             'AOAP',
             'CPC',
             'PAOA',
             'PAS',
             'LALAP',
             'PALAS',
             'SAPAS',
             'CPASA',
             'SAOAP',
#              'APATA',
             'OAPCI',
             'ATAP',
             'PALAO',
             'LASAP',
             'PCIC',
             'OALAP',
             'OAOAP',
             'OAPA',
             'CPAT',
             'PATAL',
             'ICICP',
             'ICPCI',
             'SAPA',
             'CICP',
             'PCI',
             'PATAO',
             'TAPAO',
             'TAPCI',
             'ICPAT',
             'PASA',
             'ICPA',
             'CICPA',
             'LAPC',
             'OAP',
             'OAPAT',
             'OAPAL',
             'OAPAO',
             'ICPC',
             'TAPAT',
             'TALAP',
             'CPAL',
             'PALA',
             'SAPC',
             'PALAT',
             'PATA',
             'ASAPC',
             'LAP',
             'APA',
             'OATAP',
             'LAPAT',
             'PAL',
#              'APASA',
             'LAOAP',
             'CPA',
             'PAO',
             'PAOAL',
#              'AOAPA',
             'OAPC',
             'PASAL',
             'PAOAO',
             'CPAO',
             'SAPCI'],
    'S': [   'PATAS',
             'ASAO',
             'OAPAS',
             'SALAL',
             'SAO',
             'LATAS',
#              'ALASA',
             'SAOA',
#              'TASAP',
             'SATAO',
             'SAP',
             'PCPAS',
             'TASAO',
             'ASA',
             'SAL',
             'ASAL',
             'ASAP',
             'OATAS',
             'TASA',
             'TALAS',
             'PASAT',
             'SALAP',
             'SAPCP',
             'SAT',
             'PAS',
             'LAOAS',
             'PALAS',
             'CPASA',
             'SAOAP',
             'LASA',
             'SATAT',
             'SAOAO',
             'SATAL',
             'OALAS',
             'LASAP',
             'OAS',
             'TAS',
             'TASAT',
             'SAOAT',
             'ALAS',
             'SATA',
             'SAPA',
             'OASAL',
             'PASA',
#              'AOASA',
             'ASAT',
             'OASA',
             'TAOAS',
             'TASAL',
             'SALAT',
#              'ASATA',
             'TATAS',
             'LAS',
             'LASAO',
             'SAPC',
             'OASAO',
             'ASAPC',
             'LALAS',
             'PASAP',
             'OASAT',
             'SALAO',
#              'APASA',
             'OAOAS',
             'ATAS',
             'LASAL',
#              'ASALA',
             'SALA',
             'PAPAS',
             'PASAL',
             'SAPCI',
             'LASAT',
             'AOAS'],
    'T': [   'PATAS',
             'CPATA',
             'LATAP',
             'PAOAT',
             'TAP',
             'OALAT',
             'TASAS',
             'LATAS',
             'ATAL',
             'TAPC',
#              'AOATA',
             'SASAT',
#              'TASAP',
             'SATAS',
             'SATAO',
             'OATAL',
             'TASAO',
             'ATAPC',
             'TAOAP',
             'OATAS',
             'ATA',
             'TASA',
             'TAPAP',
             'TALAS',
             'PASAT',
             'AOAT',
             'TAOAL',
             'LAT',
             'PAT',
             'TAPA',
             'SAT',
             'OAT',
             'PCPAT',
#              'APATA',
             'TALAL',
             'SATAL',
             'ATAP',
             'TAS',
#              'ALATA',
             'SAOAT',
             'CPAT',
             'PATAL',
             'SATA',
             'LALAT',
             'TAO',
             'LAOAT',
             'PATAO',
             'TAPAO',
             'TAPCI',
             'ICPAT',
#              'ATALA',
             'TAL',
             'ASAT',
             'TAOA',
             'TAOAS',
             'OAPAT',
             'TASAL',
             'TALAO',
             'SALAT',
#              'ATAOA',
             'TALAP',
#              'ASATA',
             'LATAO',
             'ALAT',
             'ATAO',
             'OATAO',
             'LATA',
             'TALA',
             'PALAT',
             'PATA',
             'OATAP',
             'LAPAT',
             'OASAT',
             'ATAS',
             'TAPCP',
             'OATA',
             'LASAT']}


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

constraints = { 'T': [], 'S': [], 'L': [], 'O': [], 'P': [], 'C': [], 'I': [] }

constraints["T"] = get_ids("TA", 700, 800)
constraints["S"] = get_ids("SA", 200, 300)
constraints["L"] = get_ids("LA", 200, 300)

# constraints["A"] = get_ids("AP", 100, 200)
# constraints["V"] = get_ids("VP", 100, 200)
# constraints["T"] = get_ids("TP", 400, 500)

constraints["O"] = get_ids("OA", 200, 300)
constraints["P"] = get_ids("PA", 200, 300)
constraints["C"] = get_ids("CP", 0, 100)
constraints["I"] = get_ids("IC", 0, 100)

for fileId in range (0, 30):
#   print(fileId)

  constraints_normal = { 'T': [], 'S': [], 'L': [], 'O': [], 'P': [], 'C': [], 'I': [] }
  metapaths_normal = { 'T': [], 'S': [], 'L': [], 'O': [], 'P': [], 'C': [], 'I': [] }
  constraints_zipf= { 'T': [], 'S': [], 'L': [], 'O': [], 'P': [], 'C': [], 'I': [] }
  metapaths_zipf = { 'T': [], 'S': [], 'L': [], 'O': [], 'P': [], 'C': [], 'I': [] }
  
  metapaths_normal["T"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(metapaths["T"]))) )
  metapaths_normal["S"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(metapaths["S"]))) )
  metapaths_normal["L"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(metapaths["L"]))) )
  metapaths_normal["O"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(metapaths["O"]))) )
  metapaths_normal["P"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(metapaths["P"]))) )
  metapaths_normal["C"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(metapaths["C"]))) )
  metapaths_normal["I"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(metapaths["I"]))) )
  
  metapaths_zipf["T"] = zipf_distribution(zipf_alpha, len(metapaths["T"]))
  metapaths_zipf["S"] = zipf_distribution(zipf_alpha, len(metapaths["S"]))
  metapaths_zipf["L"] = zipf_distribution(zipf_alpha, len(metapaths["L"]))
  metapaths_zipf["O"] = zipf_distribution(zipf_alpha, len(metapaths["O"]))
  metapaths_zipf["P"] = zipf_distribution(zipf_alpha, len(metapaths["P"]))
  metapaths_zipf["C"] = zipf_distribution(zipf_alpha, len(metapaths["C"]))
  metapaths_zipf["I"] = zipf_distribution(zipf_alpha, len(metapaths["I"])) 
  
  constraints_normal["T"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(constraints["T"]))))
  constraints_normal["S"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(constraints["S"]))))
  constraints_normal["L"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(constraints["L"]))))
  constraints_normal["O"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(constraints["O"]))))
  constraints_normal["P"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(constraints["P"]))))
  constraints_normal["C"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(constraints["C"]))))
  constraints_normal["I"] = list ( map (normal_distribution.pdf, numpy.random.normal(m, s, size=len(constraints["I"]))))
  
  constraints_zipf["T"] = zipf_distribution(zipf_alpha, len(constraints["T"]))
  constraints_zipf["S"] = zipf_distribution(zipf_alpha, len(constraints["S"]))
  constraints_zipf["L"] = zipf_distribution(zipf_alpha, len(constraints["L"]))
  constraints_zipf["O"] = zipf_distribution(zipf_alpha, len(constraints["O"]))
  constraints_zipf["P"] = zipf_distribution(zipf_alpha, len(constraints["P"]))
  constraints_zipf["C"] = zipf_distribution(zipf_alpha, len(constraints["C"]))
  constraints_zipf["I"] = zipf_distribution(zipf_alpha, len(constraints["I"])) 
  
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
  
