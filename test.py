from tos import tos
from cdito import *


# O = tos(4)
# print("\n")
# for o in O:
#     print(o)

# next_move([0,1,2,3,4], [[(0,2),(0,3)],[(0,3),(1,4)]],2,2,4)
# next_move([0,1,2,3,4], [[(0,2),(0,3)],[(0,3),(1,4)]],0,0,4)

# phi_consistent([3,4,1,0,2], [[(4,2),(2,3)],[(0,3),(1,4)]])
# phi_conflicts([0,1,2,3,4], [[(4,2),(3,2)],[(3,0),(4,1)]])


# print(conflicts2clauses([[(4,2),(2,3)],[(0,3),(1,4)]]))

L = [0, 1, 2, 3, 4]
phi1 = [(0, 4)]
phi2 = [(1, 2)]
phi3 = [(1, 3)]
phi4 = [(2, 0), (3, 0)]
# phi5 = [(3, 0), (4, 1)]
# phi6 = [(0, 2), (0, 3)]

def h(L):
    # print("Check h-Consistency.")
    if not phi_consistent(L, [[(3, 0), (4, 1)]]):
        print("Temporal Inconsistent!")
        return (False, [[(0, 3), (1, 4)]])
    if not phi_consistent(L, [[(0, 2), (0, 3)]]):
        print("State Inconsistent!")
        return (False, [[(2, 0), (3, 0)]])
    # print("h-consistent!")
    return (True, [])

Phi = [phi1, phi2, phi3, phi4]
P = [(0, 0, 4)]
cdito(L, P, Phi, h)
