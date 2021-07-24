#!/usr/bin/python3

import numpy as np
import math

def TRz(q) -> np.matrix: 
    return np.matrix([[math.cos(q), -math.sin(q), 0, 0], 
                    [math.sin(q), math.cos(q), 0, 0], 
                    [0,0,1, 0], 
                    [0,0,0,1]])


TB0 = np.identity(4)
T01 = np.matrix([[0,0,-1,0],[0,1,0,0.03],[1,0,0,0.105],[0,0,0,1]])
T12 = np.matrix([[1,0,0,0.115],[0,1,0,0], [0,0,1,0],[0,0,0,1]])
T23 = np.matrix([[1,0,0,0.02],[0,0,1,0],[0,-1,0,0],[0,0,0,1]])
T3ee = np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0.15],[0,0,0,1]])

# T02 = 




if __name__ == '__main__':
    q0 = math.pi
    q1 = math.pi / 4
    q2 = math.pi / 4
    q3 = 0
    TB0 = TB0 * TRz(q0)
    T01 = T01 * TRz(q1)
    T12 = T12 * TRz(q2 - q1)
    T23 = T23 * TRz(q3)

    TBee = TB0 * T01 * T12 * T23 * T3ee

    
    np.set_printoptions(suppress=True)
    print("TB0:\n {}\n".format(TB0))
    print(TBee)

    # print(T01)
    # print(T12)
    # print(TRz(math.pi/2))
