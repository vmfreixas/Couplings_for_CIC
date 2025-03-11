# Couplings_for_CIC
  Calculates the numerical couplings for Configuration Interaction
Coefficients (CIC) as implemented in NWChem.

  For calculating the AO overlaps between the molecule and the
displaced molecule we can build a concatenated ".xyz" file and perform
"dft" computation with ignoring the convergence by including the
following block in the input:

...

 dft
   xc      pbe0
   mult 2
   iterations 0
   convergence density  100    # default 1e-5
   print "ao overlap"
 end
 task dft

...


