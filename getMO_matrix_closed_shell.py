# This function reads MO from a molden file (closed shell)

import numpy as np

def getMO_matrix_closed_shell(FileName, Nbf):
	MO_matrix = np.zeros((Nbf, Nbf), dtype = float)
	with open(FileName, 'r') as moldenFile:
		read = False
		j = 0 
		for line in moldenFile:
			if read:
				MO_matrix[int(line.split()[0]) - 1, j - 1] = float(line.split()[1])
				if int(line.split()[0]) == Nbf:
					read = False
			if 'Occup=' in line:
				read = True
				j += 1
	return MO_matrix

