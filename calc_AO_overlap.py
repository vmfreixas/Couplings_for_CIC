#   This subroutine reads two xyz files and returns the atomic orbital
# overlaps for a given basis

from ase import io
from pyscf import gto

def read_xyz(xyzFile):	
	with open(xyzFile, 'r') as f:
		lines = f.readlines()
	atoms = []
	for line in lines[2:]:
		parts = line.split()
		symbol = parts[0]
		coords = [float(coord) for coord in parts[1:4]]
		atoms.append((symbol, coords))
	return atoms

def calc_AO_overlap(xyzFile1, xyzFile2, basis):
	#Reading xyz files:
	mol1 = read_xyz(xyzFile1)
	mol2 = read_xyz(xyzFile2)
	#Concatenating molecules:
	mol12 = mol1 + mol2
	#Building Pyscf molecule objects
	mol12_pyscf = gto.Mole()
	mol12_pyscf.atom = mol12
	mol12_pyscf.basis = basis
	mol12_pyscf.build()
	#Calculating atomic orbital overlaps
	ao = mol12_pyscf.intor('int1e_ovlp')
	#Returning the non-diagonal block of the overlap matrix
	nOrb = int(mol12_pyscf.nao / 2)
	return ao[:nOrb, nOrb:]

