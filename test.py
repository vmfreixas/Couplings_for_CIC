from calc_AO_overlap import calc_AO_overlap
from getMO_matrix_closed_shell import getMO_matrix_closed_shell
from getCIC_vector import getCIC_vector
import numpy as np


'''
# Testing the AO overlpas

file1 = '../../Map_PG3_F8/Structures/m82m12/coords.xyz'
file2 = '../../Map_PG3_F8/Structures/m82m14/coords.xyz'

AO_overlaps = calc_AO_overlap(file1, file2, 'cc-pVDZ')

np.savetxt('ao_cross_overlap.txt', AO_overlaps, fmt = '%.6f')
'''

'''
# Testing reading molden files

Nbf = 519
fileName = 'HBQ_Neutral.molden'
print(getMO_matrix_closed_shell(fileName, Nbf))
'''

# Testing reading CIC vectors from NWChem output file

fileName = 'cic_tddft.out'
print(getCIC_vector(fileName, 2))
