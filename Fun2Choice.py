"""
Created on Fri Aug 11 00:01:34 2017
@author: raiana
"""
import numpy as np
from math import *
   
### Funções unimodais
    
'''Rosembrock Function'''
def Fx(x,fchoice):  
    
    fun=0
    if(fchoice='Rosenbrock'):
        for i in range(len(x)-1):
            fun = 100*(x[i]-x[i-1]**2)**2 + (1-x[i-1])**2
        return fun 
    
    if(fchoice='Sum_of_different_powers'):
        return sum([abs(x[i])**(i+2) for i in range(len(x))])

    if(fchoice='Sphere'):
        return sum([i**2 for i in x])

    if(fchoice='Easom'):
        return -cos(x[0])*cos(x[1])*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)

    if(fchoice='Booth'):
        return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2)

    if(fchoice='Beale'):
        return (1.5 - x[0] + x[0]*x[1])**2 + (2.25 - x[0] + x[0]*x[1]**2)**2 +\ 
               (2.625 - x[0] + x[0]*x[1]**3)**2


### Unimodais parecidas

    if(fchoice='bohachevsky_function'):
        return x[0]**2 + 2*x[1]**2 - 0.3*cos(3*pi*x[0]) - 0.4*cos(4*pi*x[1]) + 0.7

    if(fchoice='sum_squares_function'):
        return sum([(i+1)*x[i]**2 for i in range(len(x))])
    
    if(fchoice='matyas_function'):
        return 0.26*sphere_function(x) - 0.48*x[0]*x[1]
    
    if(fchoice='mccormick_function'):
        return sin(x[0] + x[1]) + (x[0] - x[1])**2 - 1.5*x[0] + 2.5*x[1] + 1
    
    if(fchoice='dixon_price_function'):#sum_of_different_powers_function
        return (x[0] - 1)**2 + sum([(i+1)*(2*x[i]**2 - x[i-1])**2  for i in range(1, len(x))])
    
    if(fchoice='three_hump_camel_function'):#sum_of_different_powers_function
        return 2*x[0]**2 - 1.05*x[0]**4 + x[0]**6/6 + x[0]*x[1] + x[1]**2



### Funções multimodais

    if(fchoice='Rastrigin'):
      return 10 * len(x) + sum([np.power(i, 2.) - 10 * np.cos(2 * np.pi * i) for i in x]) 
    
    if(fchoice='Shubert'):
        n=1
        sum1=0
        sum2=0
        for n in range(1,6):
            new1=(n*np.cos((n+1)*x[0]+n))
            new2=(n*np.cos((n+1)*x[1]+n))
            sum1=sum1+new1
            sum2=sum2+new2
        return (sum1*sum2+186.7309) 

    if(fchoice='Schwefel'):
        summ=0
        for i in range(len(x)):
            new=x[i]*np.sin((abs(x[i]))**0.5)
            summ=summ+new
        return (418.982887272433799807913601398*len(x)-summ)
 
    if(fchoice='Ackley'):
        return -20*exp(-0.2*sqrt(1/len(x)*sum([i**2 for i in x]))) - \
               exp(1/len(x)*sum([cos(2*np.pi*i) for i in x])) + 20 + exp(1)

    if(fchoice='Bukin'):
        return 100*sqrt(abs(x[1]-0.01*x[0]**2)) + 0.01*abs(x[0] + 10)

    if(fchoice='Cross_in_tray'):
        return round(-0.0001*(abs(sin(x[0])*sin(x[1])*exp(abs(100 -
                            sqrt(sum([i**2 for i in x]))/pi))) + 1)**0.1, 7)

    if(fchoice='Michalewicz'):
        return -sum([sin(x[i])*sin((i)*x[i]**2/pi)**20 for i in range(len(x))])

    if(fchoice='Drop_wave'):
        return -(1 + cos(12*sqrt(sphere_function(x))))/(0.5*sphere_function(x) + 2)

    if(fchoice='Six_hump_camel'):
        return (4 - 2.1*x[0]**2 + (x[0]**4)/3)*x[0]**2 + x[0]*x[1]\
                + (-4 + 4*x[1]**2)*x[1]**2

#fx=-1.0316 ; x=(+-0.0898,+-0.7126) x1 ∈ [-3, 3], x2 ∈ [-2, 2].
