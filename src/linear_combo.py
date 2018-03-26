import numpy as np

def lin_comb(x, y):
    """x: numpy array of RGB values for component colors
          = np.array([[R1, R2, ... Rn], [G1, G2, ..., Gn], [B1, B2, ..., Bn]])
       y: numpy array vector of RGB value for target color
          = np.array([Rtarget, Gtarget, Btarget])
       
       returns: numpy array of co-efficients np.array([a1, a2, ..., an]) such that
                Rtarget = a1*R1 + a2*R2 + ... + an*Rn
                Gtarget = a1*G1 + a2*G2 + ... + an*Gn
                Btarget = a1*B1 + a2*B2 + ... + an*Bn"""
                
    scalars = np.linalg.solve(x,y)
    return scalars


if __name__=="__main__":
    x = np.array([[234,255,255],[0, 10, 3],[0,0,20]])
    y = np.array([245,80,90])
    print('Example:')
    print('Component colors: [234, 0, 0], [255, 10, 0], [255, 3, 20]', '\nTarget color: [245, 80, 90]')
    
    combos = lin_comb(x, y)
    print('Co-efficients for linear combination:')
    print(combos)