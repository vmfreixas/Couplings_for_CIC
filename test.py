from calc_AO_overlap import calc_AO_overlap
import numpy as np

file1 = '../../Map_PG3_F8/Structures/m82m12/coords.xyz'
file2 = '../../Map_PG3_F8/Structures/m82m14/coords.xyz'

AO_overlaps = calc_AO_overlap(file1, file2)

np.savetxt('ao_cross_overlap.txt', AO_overlaps, fmt = '%.6f')
