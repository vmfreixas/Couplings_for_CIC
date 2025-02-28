import numpy as np

def getCIC_vector(fileName, root):
	cic = []
	with open(fileName, 'r') as nwFile:
		readRoot = False
		for line in nwFile:
			if 'Root' in line and int(line.split()[1]) == root:
				readRoot = True
			if readRoot:
				if 'Root' in line and int(line.split()[1]) != root:
					break
				if 'Occ.' in line:
					cic.append([int(line.split()[1]), int(line.split()[5]), float(line.split()[7])])
	return cic
