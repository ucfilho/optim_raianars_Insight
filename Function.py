import numpy as np
from math import *


# Funções self-tuning implementation

################################### 

def Shekel(x):
    a=np.array([[-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32],
                [-32,-32,-32,-32,-32,-16,-16,-16,-16,-16,0,0,0,0,0,16,16,16,16,16,32,32,32,32,32]])  
    sumj = 0
    for j in range(2):
      sumi = 0
      for i in range(len(x)):
        sumi = sumi + (x[i]+a[j,i])**6
      sumj = sumj + 1.0 / (j+ sumi)
    fun =1.0 / (1/500.0+ sumj)  
    return fun
    # Shekel's Foxholes Function 
    # Range of initial points: -65.536 <= xj <= 65.536 , j=1,2
    # Global minima: (x1,x2)=(-31.97833,-31.97833)
    # f(x1,x2)=0.998003837794449325873406851315 obs dim =30 optimum close to zero..
    
def PenaltyOne(x):
    n = len(x); a = 10 ; k = 100 ; m =4; pi = np.pi;
    sumy=0
    sumu=0
    
    for i in range((n-1)):
        yi = 1 + 1.0/4*(x[i]+1)
        yip = 1 + 1.0/4*(x[i+1]+1)
        sumy=sumy+(yi-1)**2*(1+10*(np.sin(pi*yip))**2)
        if( x[i] > a):
            sumu = sumu + k*(x[i]-a)**m
        elif( x[i] < -a):
            sumu = sumu + k*(-x[i]-a)**m
        else:
            sumu = sumu # it could be done without put this case
        
    y0 = 1 + 1.0/4*(x[0]+1)
    yn = 1 + 1.0/4*(x[n-1]+1)
    fun = pi/n*(10*(np.sin(pi*y0))**2 + sumy + (yn-1)**2 ) + sumu 
    return fun

def PenaltyTwo(x):
    n = len(x); a = 5 ; k = 100 ; m =4; pi = np.pi;
    sumx=0
    sumu=0
    
    for i in range((n-1)):
        sumx=sumx+   (x[i]-1)**2*(1+(np.sin(3*pi*x[i+1]))**2)
        if( x[i] > a):
            sumu = sumu + k*(x[i]-a)**m
        elif( x[i] < -a):
            sumu = sumu + k*(-x[i]-a)**m
        else:
            sumu = sumu # it could be done without put this case
        
    fun = 0.1*( (np.sin(3*pi*x[0]))**2 + sumx + (x[n-1]-1)**2*(1+(np.sin(2*pi*x[n-1]))**2) ) + sumu 
    return fun
# f(x)=0 x=(0,0) [−1.28, 1.28]

def Kowalik(x):
    n = 11; 
    a= [0.1957,0.1947,0.1735,0.1600,   0.0844,0.0627,0.0456,0.0342,    0.0323,0.0235,0.0246]
    b=[0.25, 0.5, 1,2,4,6,8,10,12,14,16]
    sumx=0
    
    for i in range(n):
        bi = 1/b[i]
        upfrac = x[0]*(bi**2+bi*x[1])
        downfrac = bi**2+bi*x[2]+x[3]
        sumx=sumx+ (a[i] -upfrac/downfrac)**2
 
    fun = sumx 
    return fun
# f(x)=0 x=(0,0) [−1.28, 1.28]


def Michalewicz(x):
    return -sum([sin(x[i])*sin((i+1)*x[i]**2/pi)**20 for i in range(len(x))])
#fx=-9.66015 d=10 [0,pi]

def Michalewicz_New(x):
    Num=len(x)
    S=0
    for i in range(Num):
        S=S+np.sin(x[i])*np.sin((i+1)*x[i]**2/np.pi)**20 
    return S
#fx=-9.66015 d=10 [0,pi]

def Bent_Cigar(x):

  soma=0
  Num=len(x)

  for i in range(1,Num):
    soma=soma+x[i]**2
  soma=soma*10**6+x[0]**2
  return soma
# f(x)=0 , x=(0,0,...,0) [-100,100]

def Fake_Rosenbrock(x):
    fun=0
    Num=len(x)-1
    for i in range(Num):
        fun = 100*(x[i]-x[i-1]**2)**2 + (1-x[i-1])**2
    return fun 
# Global Minimum: 0 , domain=[-30,30]


def Noisy_Quartic(x):
    sumx4=0
    i=0
    for k in x:
        i=i+1
        sumx4=sumx4+i*k**4
    sumx4=sumx4+np.random.random()
    return sumx4
# f(x)=0 x=(0,0) [−1.28, 1.28]



def Schwefel_222(x):
    sumx=0
    prodx=1
    i=0
    for k in x:
        i=i+1
        sumx=sumx+abs(k)
        prodx=prodx*abs(k)
    sumx=sumx+prodx
    return sumx
# f(x)=0 x=(0,0) [−10, 10]

def Schwefel_221(x):
    maximum = 0.0
    for c in x:
        if(abs(c) > maximum):
            maximum = abs(c)
    return maximum
# f(x)=0 x=(0,0) [−100, 100]

def Schwefel_12(x):
    sum2=0
    for k in range(len(x)):
        sum1=0
        for i in range(k+1):
            sum1=sum1+x[i]
        sum2=sum2+sum1**2
    return sum2
# f(x)=0 x=(0,0) [−100, 100]


# Funções n-dimensionais

################################### Funções Unimodais Separáveis

def Sphere(x):
    return sum([i**2 for i in x])
# f(x)=0 x=(0,0) [-5.12,5.12]

def Step(x):
    return sum([(i+0.5)**2 for i in x])
# f(x)=0 x=(0,0) [-100,100]

def Sum_of_different_powers(x):
    return sum([abs(x[i])**(i+2) for i in range(len(x))])
# f(x)=0 x=(0,0) , d=[-1,1]

def sum_squares_function(x): #gráfico parecido c a espera
    return sum([(i+1)*x[i]**2 for i in range(len(x))])
# f(x)=0 x=(0,0) , d=[-10,10]


# Zakharov Function
def Zakharov(x):
  sumx2=0
  sum_05ix=0
  i=0
  for k in x:
    i=i+1
    sumx2=sumx2+k**2
    sum_05ix=sum_05ix+0.5*i*k
  return sumx2+ (sum_05ix)**2+ (sum_05ix)**4
# Global minimum 0  at x=(0,0,...,0) 
# Convex it is usually evaluated on the hypercube xi =[(-5,10),..(-5,10)]

################################### Funções Unimodais Não Separáveis

def ridge(x):
  soma=0
  d=2
  alpha=0.1
  for i in x:
    soma=soma+i**2
  soma=soma-x[0]**2
  return x[0]+d*soma**(alpha)
# f(x)=-gamma , x=(-gamma,0,0,...,0) ex gamma=5 (gamma é o limite inferior do intervalo)

# Xin-She Yang N. 3 Function
def XinSheYang(x):
  m=5
  b=15
  sumx_b_2m=0
  sumx2=0
  prod_cos2x=1
  for k in x:
    sumx2=sumx2+k*k
    sumx_b_2m=sumx_b_2m+(k/b)**(2*m)
    prod_cos2x=prod_cos2x*np.cos(k)**2
  return np.exp(-sumx_b_2m)-2*np.exp(-sumx2)*prod_cos2x
# Global minimum -1  at x=(0,0,...,0) for m=5 e b=15
# Convex it is usually evaluated  xi =[(-2*pi,2*pi),..,(-2*pi,2*pi)]
################################### Funções Multimodais Separáveis
    
def Rastrigin(args):
    f = 10 * len(args) + sum([np.power(x, 2.) - 10 * np.cos(2 * np.pi * x) for x in args])
    return f
# f(x)=0 x=(0,0) [-5.12,5.12]

def Schwefel(x):
    summ=0
    for i in range(len(x)):
        new=x[i]*np.sin((abs(x[i]))**0.5)
        summ=summ+new
    return (418.982887272433799807913601398*len(x)-summ)
# f(xi)= 0 for xi = 420.968746 for i=1,...,n  ;  xi in [-500,500] 
    
def Ackley(x):
    return -20*exp(-0.2*sqrt(1/len(x)*sum([i**2 for i in x]))) - \
           exp(1/len(x)*sum([cos(2*np.pi*i) for i in x])) + 20 + exp(1)
 # f(x)=0 x=(0,0) [-32, 32]


# Shubert3 function
def Shubert3(x):
  soma=0

  for i in x:
    for k in range(5):
      j=k+1
      soma=soma +j * np.sin(((j + 1) * i) + j)

  return soma
# global minimum −29.6733337 at x (not specified but DE found)=(-1.11409968,-1.11409968) 
# not convex it is usually evaluated  xi =[(-10,10),..,(-10,10)]

# Styblinskitank function
def Styblinskitank(x):
  sumx1=0
  sumx2=0
  sumx4=0
  for i in x:
    sumx1=sumx1+i
    sumx2=sumx2+i**2
    sumx4=sumx4+i**4
  fun= (sumx4-16*sumx2+5*sumx1)/2
  return fun
# global minimum −39.16599∗n at x=(−2.903534,…,−2.903534) 
# Not Convex it is usually evaluated  xi =[(-5,5),..(-5,5)]

################################### Funções Multimodais Não Separáveis
    
def Fake_Rosenbrock(x):
    fun=0
    Num=len(x)-1
    for i in range(Num):
        fun = 100*(x[i]-x[i-1]**2)**2 + (1-x[i-1])**2
    return fun 
# Global Minimum: 0 , domain=[-30,30]

def Rosenbrock(x):
    fun=0
    Num=len(x)-1
    for i in range(Num):
        fun = fun+100*(x[i+1]-x[i]**2)**2 + (1-x[i])**2
    return fun 
# Global Minimum: 0 , domain=[-30,30]
'''
def HappyCat(x): 
    alpha=1. / 8
    s = sum(x**2) 
    return ((s - len(x))**2)**alpha + (s / 2 + sum(x)) / len(x) + 0.5 
# global mimima at (-1,-1,...,-1) - f(x)=0  - d=[-2,2] (qlq dominio)
'''
def HappyCat(x): 
    alpha=1. / 8
    s=0
    Num=len(x)
    for i in range(Num):
               s=s+x[i]*x[i]
    return ((s - len(x))**2)**alpha + (s / 2 + sum(x)) / len(x) + 0.5 
# global mimima at (-1,-1,...,-1) - f(x)=0  - d=[-2,2] (qlq dominio)

def Alpinen2(x):
  prod=1
  for i in x:
    prod=prod*(i**0.5*np.sin(i))
  return prod*(-1)
# global maxima f(x)= 2.808^n - x=(7.917,...,7.917) d=[0,10]

def Alpine_n1(x):
  s=0
  for i in x:
    s=s+abs(i*np.sin(i)+0.1*i)
  return s
# global minimum f(0)= 0 d=[-10,10] 

def Periodic(x):
  sumx2=0
  sin2x=0
  for i in x:
    sumx2=sumx2+i**2
    sin2x=sin2x+(np.sin(i))**2
  return 1+sin2x-0.1*np.exp(-sumx2)
# global minimum 0.9 at x=(0,0,...,0) , d=[-10,10] 

def Salomon(x):
  sumx2=0
  sqrtsx2=0
  for i in x:
    sumx2=sumx2+i**2
  sqrtsx2=sumx2**0.5
  return 1-np.cos(2*np.pi*sqrtsx2)+(0.1 * sqrtsx2)
# global minimum 0  at x=(0,0,...,0) 

# Griewank Function
def Griewank(x):
  prod_cosx_i05=1
  sumx1=0
  sumx2=0
  i=0
  for k in x:
    i=i+1
    sumx1=sumx1+k
    sumx2=sumx2+k*k
    prod_cosx_i05=prod_cosx_i05*np.cos(k/(i**0.5))
  return 1+sumx2/4000 - prod_cosx_i05
# Global minimum 1  at x=(0,0,...,0) 
# Not convex it is usually evaluated  xi =[(-600,600),..(-600,600)]

# Qing Function
def Qing(x):
  sumx2_i_2=0
  i=0
  for k in x:
    i=i+1
    sumx2_i_2=sumx2_i_2+(k**2-i)**2
  return sumx2_i_2
# Global minimum 0  at x=(1^0.5,2^0.5,...,n^0.5) (xi=square root (i) for i=1,2,....n)
# Convex it is usually evaluated  xi =[(-500,500),..(-500,500)]
# PS: negative values of square root (i) for i=1,2,....n also provide global minimum

# Shubert Function
def Shubert(x):
  prod=1
  for i in x:
    sum_eq=0
    for k in range(5):
      j=k+1
      sum_eq=sum_eq+np.cos(((j + 1) * i) + j)
    prod=prod*sum_eq
  return prod
#  Global minimum The function has 18 global minima  equal -186.7309
#  Not Convex it is usually evaluated  xi =[(-10,10),..,(-10,10)]

def Drop_wave(x):
    return -(1 + cos(12*sqrt(sphere_function(x))))/(0.5*sphere_function(x) + 2)

#======================================

fixed dimention

def Easom(x):
    return -cos(x[0])*cos(x[1])*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)
# f(x)=-1 x=(pi,pi) [-100,100]

def Booth(x):
    return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2
# f(x)=0 x=(1,3) [-10,10]
    
def Beale(x):
    return (1.5 - x[0] + x[0]*x[1])**2 + (2.25 - x[0] + x[0]*x[1]**2)**2 + \
           (2.625 - x[0] + x[0]*x[1]**3)**2

def dixon_price_function(x): # parece sum_of_different_powers_function
    return (x[0] - 1)**2 + sum([(i+1)*(2*x[i]**2 - x[i-1])**2
                                for i in range(1, len(x))])
# f(x)=0 xi=2^(-(2^i - 2)/2^i   d= [-10,10]

def Six_hump_camel(x): 
    return (4 - 2.1*x[0]**2 + (x[0]**4)/3)*x[0]**2 + x[0]*x[1]\
           + (-4 + 4*x[1]**2)*x[1]**2
#fx=-1.0316 ; x=(+-0.0898,+-0.7126) x1 ∈ [-3, 3], x2 ∈ [-2, 2]. 

def Cross_in_tray(x):
    return round(-0.0001*(abs(sin(x[0])*sin(x[1])*exp(abs(100 -
                            sqrt(sum([i**2 for i in x]))/pi))) + 1)**0.1, 7)
#fx--2.06261 x=( +/-1.3491.+/-1.3491) [-10,10]

def Bukin(x):
    return 100*sqrt(abs(x[1]-0.01*x[0]**2)) + 0.01*abs(x[0] + 10)
# f(X)=0, x=(-10,1)    x_1∈[-15.-5]  x2 ∈ [-3, 3]. 
