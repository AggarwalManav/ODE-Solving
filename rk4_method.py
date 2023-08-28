#runge kutta method is for upto 4 order diff. eqn.
#f(x)=dy/dx, h=xmax-xmin/n
#order=1: Euler method y2=y1+h*k1  , k1=f(x1,y1)

"""
order=4: RK4 method: y2=y1+1/6*(k1+2*k2+2*k3+k4)*h  

k1=f(x1,y1), k2=f(x1+h/2,y+k1*h/2)
 
k3=f(x1+h/2,y1+k2*h/2),   k4=f(x1+h,y1+k3*h)

"""
import numpy as np

def f(x,y):  
  return x*y**0.5
  
def rk4(f,x0,y0,xn,n):
  h=(xn-x0)/n
  x=np.arange(x0,xn+h,h)
  y=[y0]
  for i in range(n):
    k1=f(x[i],y[i])
    k2=f(x[i]+h/2,y[i]+k1*h/2)
    k3=f(x[i]+h/2,y[i]+k2*h/2)
    k4=f(x[i]+h,y[i]+k3*h)
    c=y[i]+((k1+2*k2+2*k3+k4)*h)/6
    y.append(c)
  return x,y
  
x,y=rk4(f,0.0,1.0,1,10)
for i in range(0,11,1):
  print("%4.1f %10.5f %10.5f"%(x[i],y[i],(4+x[i]*x[i])**2/16.0))  
    
  

