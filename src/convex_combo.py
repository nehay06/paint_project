import numpy as np
from scipy.optimize import linprog

def in_hull(points, x):
    n_points = len(points)
    n_dim = len(x)
    c = np.ones(n_points)#np.zeros(n_points)
    A = Z#np.r_[Z.T,np.ones((1,n_points))]
    b = x#np.r_[x, np.ones(1)]
    lp = linprog(c, A_eq=A, b_eq=b)
    print('A = \n', A)
    print('b = \n', b)
    print('c = \n', c)
    return lp#.success

n_points = 3#10000
n_dim = 10
Z = np.array([[234,255,255],[0, 10, 3],[0,0,20]])#np.random.rand(n_points,n_dim)
x = np.array([245,80,90])#np.random.rand(n_dim)
print(in_hull(Z, x))