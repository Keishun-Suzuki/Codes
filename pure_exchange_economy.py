#This is a Python code for a simple pure exchange economy
import sympy
import numpy as np

#Parameters of Cobb-Douglas utility function
a = np.array([2, 1]) #consumer A: uA=(x1^a1)*(x2^a2)
b = np.array([1, 2]) #consumer B: uB=(x1^b1)*(x2^b2)

#Endowment vector
ea = np.array([3, 4]) #consumer A: (eA1, eA2)
eb = np.array([6, 2]) #consumer B: (eB1, eB2)

#Initial utility
uae=ea[0]**a[0]*ea[1]**a[1]
ube=eb[0]**b[0]*eb[1]**b[1]

#Competitive equilibrium price
sympy.var('p, pstar')
pstar=sympy.solve ((ea[0]*p+ea[1])/(1+a[1]/a[0])+(eb[0]*p+eb[1])/(1+b[1]/b[0])-(ea[0]+eb[0])*p, p)

#Competitive equilibrium allocation
xa1=(ea[0]+ea[1]/pstar[0])/(1+a[1]/a[0])
xa2=(ea[0]*pstar[0]+ea[1])/(1+a[0]/a[1])
xb1=(eb[0]+eb[1]/pstar[0])/(1+b[1]/b[0])
xb2=(eb[0]*pstar[0]+eb[1])/(1+b[0]/b[1])

#Utility
ua=xa1**a[0]*xa2**a[1]
ub=xb1**b[0]*xb2**b[1]
display(pstar[0])
display([xa1, xa2])
display([xb1, xb2])

import matplotlib.pyplot as plt
from pylab import mpl

plt.figure(figsize=(12,8))
plt.axis([0,ea[0]+eb[0],0,ea[1]+eb[1]])
sympy.var('x, y')
x= np.linspace((ea[0]+eb[0])/100, ea[0]+eb[0]-1/100, 100)

#Budget line
y = -pstar[0]*(x-ea[0])+ea[1]
plt.plot(x, y, color="green", label='Budget line')

#Indifferenct curve
y = (uae/(x**a[0]))**(1/a[1]) #consumer A (Initial)
plt.plot(x, y, linestyle="dotted", color="crimson")
y = ea[1]+eb[1]-(ube/((ea[0]+eb[0]-x)**b[0]))**(1/b[1]) #consumer B (Initial)
plt.plot(x, y, linestyle="dotted", color="darkblue")
y = (ua/(x**a[0]))**(1/a[1]) #consumer A
plt.plot(x, y, color="crimson")
y = ea[1]+eb[1]-(ub/((ea[0]+eb[0]-x)**b[0]))**(1/b[1]) #consumer B
plt.plot(x, y, color="darkblue")

#Contract curve
H = a[1]*b[0]*(ea[1]+eb[1])
J = a[0]*b[1]*(ea[0]+eb[0])
K = b[0]*a[1]-a[0]*b[1]
y= H*x/(J+K*x)
plt.plot(x, y, linestyle="dashed", color="magenta", label='Contract curve')

#Point
plt.plot(ea[0],ea[1], marker='.', color="black", markersize="16")
plt.plot(xa1,xa2, marker='.', color="red", markersize="16")

#Label
plt.text(ea[0]*0.98, ea[1]*1.05, "\u03c9", fontsize="24")
plt.text(xa1*0.98, xa2*1.05, "E", fontsize="24")
plt.title('Edgeworth Box', fontsize="20")
plt.xlabel('xA1', fontsize="16")
plt.ylabel('xA2',  fontsize="16")

plt.grid(True)
plt.legend(fontsize="16")
plt.show()
