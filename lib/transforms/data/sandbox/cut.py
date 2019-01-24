#!/usr/bin/env python3
import pandas as pd
import os
import sys
import fileinput as fi
from pprint import pprint
import shutil

def stripLine(str):
	xs = line.split('\t')
	xs = [ x.strip() for x in xs ]
	# Replace missing calls (-1) with NA
	for i, x in enumerate(xs):
		if x == '-1':
			xs[i] = 'NA'
	return xs

# Get all of the output directory info and set up the folderimport shutil
fprefix = sys.argv[1].split('.')[0]
outputdir = sys.argv[4]
if os.path.isdir(outputdir):
	shutil.rmtree(outputdir)
os.mkdir(outputdir)

posfp = fi.input(sys.argv[1])
erdbeere = {}
current_chromosome = None
max_lineno = 0
print('/============= .pos =============')
for line in posfp:
	line = stripLine(line)
	print(line)
	chromosome, snp = line
	if current_chromosome != chromosome:
		current_chromosome = chromosome
		erdbeere[chromosome] = {}
		erdbeere[chromosome]['data'] = {}
		erdbeere[chromosome]['data']['genotype'] = []
		erdbeere[chromosome]['min'] = posfp.lineno()
	erdbeere[chromosome]['max'] = posfp.lineno()
	prefix = current_chromosome[:3].lower()
	id_num = str(int(current_chromosome[-2:]))
	filename = f'{outputdir}/{prefix}{id_num}_{fprefix}.012.pos'
	message = f"{str(int(current_chromosome[-2:]))}\t{snp}\n"
	with open(filename, 'a+') as ofp:
		ofp.write(message)
print('============= .pos =============/')
# Make sure to define the upper bound for the last chromosome
erdbeere[current_chromosome]['max'] = posfp.lineno()
print('/============= Erdbeere =============')
pprint(erdbeere)
print('============= Erdbeere =============/')

print('/============= Pedigree =============')
indvxs = []
# Find the pedigree name for each genotype
with open(sys.argv[2], 'r') as indvfp:
	for line in indvfp:
		# print(stripLine(line))
		indvxs.append(stripLine(line))
indvdf = pd.DataFrame(indvxs)
# Copy the individual/line files
for i, c in enumerate(erdbeere.keys()):
	dest = f'{outputdir}/{c[:3].lower()}{str(int(c[-2:]))}_{fprefix}.012.indv'
	shutil.copyfile(sys.argv[2], dest)
pprint(indvdf)
print('============= Pedigree =============/')

print('/======================================= Genotype =======================================')
# Cut out the columns for each
genoxs = []
with open(sys.argv[3], 'r') as genofp:
	for line in genofp:
		xs = stripLine(list)
		# For each chromosome, pull out the columns from the genotype
		for i, c in enumerate(erdbeere.keys()):
			chr_lowerbound = erdbeere[c]['min']
			chr_upperbound = erdbeere[c]['max'] + 1
			xss = xs[chr_lowerbound:chr_upperbound]
			c = f'{c[:3].lower()}{str(int(c[-2:]))}_{fprefix}.012'
			filename = f'{outputdir}/{c}'
			message = '\t'.join(xss)
			with open(filename, 'a+') as genofp:
				genofp.write(f"{message}\n")
			# erdbeere[chromosome]['data']['genotype'].append(xss) # TODO(timp): replace with appending to tempfile for chromosome
		# print(stripLine(line))
		# genoxs.append(xs)
# genodf = pd.DataFrame(genoxs)
# genodf = genodf.rename(columns = {0:'lineno'})
# genodf.set_index('lineno', inplace = True)
# pprint(genodf)
print('======================================= Genotype =======================================/')



# print('/============================== Chromosomes Extracted ===============================')

# pprint(erdbeere)
# for i, c in enumerate(erdbeere):
# 	xs = erdbeere[c]['data']['genotype']
# 	print(c)
# 	df = pd.DataFrame(xs)
# 	# df = df.transpose()
# 	# df.columns = [ x[0] for x in indvxs]
# 	print(df)
# 	c = f'{c[:3].lower()}{str(int(c[-2:]))}_{fprefix}.012'
# 	filename = f'{outputdir}/{c}'
# 	df.to_csv(filename, sep = '\t', index = False, header = False)
# print('=============================== Chromosomes Extracted ==============================/')


