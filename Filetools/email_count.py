import csv, timeit
domains = ['erthcorp.com', 'erthpower.com', 'erthsolutions.com', 'eriethamespower.com', 'ebterthcorp.com']
with open('hendy2.csv') as csvfile:
    cvsreader = csv.reader(csvfile, delimiter=',')
    incoming = lambda erth_dom,recip_address : erth_dom in recip_address 
    em = { row[1] : row[0] for row in cvsreader for domain in domains if incoming(domain, row[1])} 
    em = sorted(em.items(), key=lambda x: int(x[1]))

"""
f = open('email_count.cvs', 'w')
for line in em:
    f.write(line[0] + ', ' + line[1] + '\n')
f.close()
"""

