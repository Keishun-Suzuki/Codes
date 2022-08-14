#This is a Python code for weak axiom of revealed preference (WARP)
import numpy as np

#date A
pa = np.array([2, 4]) #price vector: (pA1, pA2)
xa = np.array([2, 6]) #consumption plan: (xA1, xA2)
eaa = np.dot(pa, xa) #Expenditure (=Budget on date A)

#date B
pb = np.array([6, 2]) #price vector: (pB1, pB2)
xb = np.array([6, 4]) #consumption plan: (xB1, xB2)
ebb = np.dot(pb, xb) #Expenditure (=Budget on date B)

#Counterfactual expenditure
eab = np.dot(pa, xb) #Expenditure of xB on date A
eba = np.dot(pb, xa) #Expenditure of xA on date B

if eaa >= eab: #xB is feasible on date A
    if eba <= ebb: #xA is feasible on date B
        print('WARP is violated.')
    else:
        print('WARP is satisfied.')
        
else:
    if eba <= ebb: #xA is feasible on date B
        if eab <= eaa: #xB is feasible on date A
            print('WARP is violated.')
        else:
            print('WARP is satisfied.')

import matplotlib.pyplot as plt
from pylab import mpl

plt.figure(figsize=(10,6))
plt.axis([0,xa[0]+xb[0],0,xa[1]+xb[1]])

import sympy
sympy.var('x, y')
x= np.linspace((xa[0]+xb[0])/100, xa[0]+xb[0]-1/100, 100) 

#Budget lines
y = -(pa[0]/pa[1])*(x-xa[0])+xa[1] #date A
plt.plot(x, y, color="crimson", label='Budget line on date A')
y = -(pb[0]/pb[1])*(x-xb[0])+xb[1] #date B
plt.plot(x, y, color="darkblue", label='Budget line on date B')

#Points
plt.plot(xa[0],xa[1], marker='.', color="black", markersize="16")
plt.plot(xb[0],xb[1], marker='.', color="black", markersize="16")

#Label
plt.text(xa[0]*0.98, xa[1]*1.05, "xA",  fontsize="20")
plt.text(xb[0]*0.98, xb[1]*1.05, "xB",  fontsize="20")

plt.title('Weak Axiom of Revealed Preference',  fontsize="20") 
plt.xlabel('x1', fontsize="16") 
plt.ylabel('x2', fontsize="16") 

plt.grid(True)
plt.legend(fontsize="16") 
plt.show()
