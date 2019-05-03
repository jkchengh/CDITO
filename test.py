from cdito import cdito, phi_consistent
from tos import tos

#
tos(4)
#
# L = [0, 1, 2, 3]
# P = [(0, 0, 3)]
# Phi = []
# def h(L): return (False, [])
# cdito(L, P, Phi, h)


# L = [0, 1, 2, 3, 4]
# phi1 = [(0, 4)]
# phi2 = [(1, 2)]
# phi3 = [(1, 3)]
# phi4 = [(2, 0), (3, 0)]
#
# def h(L):
#     if not phi_consistent(L, [[(3, 0), (4, 1)]]):
#         print("Temporal Inconsistent!")
#         return (False, [[(0, 3), (1, 4)]])
#     if not phi_consistent(L, [[(0, 2), (0, 3)]]):
#         print("State Inconsistent!")
#         return (False, [[(2, 0), (3, 0)]])
#     return (True, [])
#
# Phi = [phi1, phi2, phi3, phi4]
# P = [(0, 0, 4)]
# cdito(L, P, Phi, h)