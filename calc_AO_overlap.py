# This subroutine reads two xyz files and calculates the atomic overlap

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
	#Reading the first xyz file:
	mol1 = read_xyz(xyzFile1)
	mol2 = read_xyz(xyzFile2)
	mol12 = mol1 + mol2
	mol12_pyscf = gto.Mole()
	mol12_pyscf.atom = mol12
	mol12_pyscf.basis = basis
	mol12_pyscf.build()
	ao = mol12_pyscf.intor('int1e_ovlp')
	nOrb = int(mol12_pyscf.nao / 2)
	return ao[:nOrb, nOrb:]

