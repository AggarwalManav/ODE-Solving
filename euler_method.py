#ordinary differential equation
#def ode_euler(f,x0,y0,xn,n):
#....return x,y
#Yn+1=Yn+hf(Xn,Yn)
#h=common difference between solutions (x0,y0),(x1,y1),(x2,y2)...(xn,yn) 
#n=no. of solutions to the differential equations

import numpy as np

def f(x,y):
  return x*np.sqrt(y)
  
def ode_euler(f,x0,y0,xn,n):
  h=(xn-x0)/float(n)
  x=np.arange(x0,xn+h,h)
  y=[y0]
  for i in range(n):
    y.append(y[i]+h*f(x[i],y[i]))
  return x,y
  
x,y=ode_euler(f,0.0,1.0,1,10)
for i in range(0,11,1):
  print("%4.1f %10.5f %10.5f"%(x[i],y[i],(4+x[i]*x[i])**2/16.0))   