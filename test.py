from calc_AO_overlap import calc_AO_overlap
from get_AO_overlap_from_NWChem import get_AO_overlap_from_NWChem
from get_MO_matrix_from_NWChem import get_MO_matrix_from_NWChem
import numpy as np

# Testing the AO overlpas

file12 = 'cic_tddft_m82m12.out'
file14 = 'cic_tddft_m82m14.out'
fileConc = 'overlaps.out'

ao12 = get_AO_overlap_from_NWChem(file12)
aoConc = get_AO_overlap_from_NWChem(fileConc)

np.savetxt('ao_NWChemConc.txt', aoConc, fmt = '%.6f')
np.savetxt('ao_NWChem.txt', ao12, fmt = '%.6f')

dims = ao12.shape

mo = get_MO_matrix_from_NWChem(file12)

normCheck2 = mo.T @ ao12 @ mo
normCheck3 = mo.T @ aoConc[:dims[0], :dims[1]] @ mo
np.savetxt('normCheck2.txt', normCheck2, fmt = '%.6f')
np.savetxt('normCheck3.txt', normCheck3, fmt = '%.6f')


'''
# Testing reading molden files

Nbf = 519
fileName = 'HBQ_Neutral.molden'
print(getMO_matrix_closed_shell(fileName, Nbf))
'''

'''
# Testing reading CIC vectors from NWChem output file

fileName = 'cic_tddft.out'
print(get_CIC_vector(fileName, 2))
'''
