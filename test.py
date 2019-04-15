from tos import tos
from cdito import cdito, next_move, phi_conflicts, phi_consistent


# O = tos(4)
# print("\n")
# for o in O:
#     print(o)

# next_move([0,1,2,3,4], [[(0,2),(0,3)],[(0,3),(1,4)]],2,2,4)
# next_move([0,1,2,3,4], [[(0,2),(0,3)],[(0,3),(1,4)]],0,0,4)

# phi_consistent([3,4,1,0,2], [[(4,2),(2,3)],[(0,3),(1,4)]])
# phi_conflicts([0,1,2,3,4], [[(4,2),(3,2)],[(3,0),(4,1)]])

L = [0, 1, 2, 3, 4]
phi1 = [(0, 4)]
phi2 = [(1, 2)]
phi3 = [(1, 3)]
phi4 = [(2, 0), (3, 0)]
phi5 = [(3, 0), (4, 1)]
phi6 = [(0, 2), (0, 3)]
Phi = [phi1, phi2, phi3, phi4, phi5, phi6]
P = [(0, 0, 4)]
cdito(L, P, Phi)
