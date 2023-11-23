# Solve Zebra using NaryCPS and AC_Sover
from csp import *
# from notebook import psource, plot_NQueens

# %matplotlib inline
# Hide warnings in the matplotlib sections

import math
import warnings
warnings.filterwarnings("ignore")
# variables

def atmost_three(*values):
    """Returns True if all values are assigned to atmost 5 variables, False otherwise"""
    for v in set(values):
        if values.count(v) > 5:
            return False
    return True



HorarioBlocos = '11 12 13 14 21 22 23 24 31 32 33 34 41 42 43 44 51 52 53 54'.split()
Disciplina = 'D1 D2 D3 D4 D5 D6'.split()
variables = set ( Disciplina )

# Domains
dominio = {}
for var in variables:
    dominio[var] = set(HorarioBlocos)     # list(range(1, 6))

# Constraints
restricoes = [
              Constraint(variables, all_diff_constraint),
              Constraint(variables, atmost_three),
              ]

# Define NaryCSP
zebra_narycsp = NaryCSP(dominio, restricoes)

# Apply solver
sol_nary = ac_solver(zebra_narycsp, arc_heuristic=sat_up)

# Print result
for h in range(1, 6):
        print('House', h, end=' ')
        for (var, val) in sol_nary.items():
            if val == h:
                print(var, end=' ')
        print()