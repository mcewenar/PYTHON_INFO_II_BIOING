# %%
import numpy as np
from numpy.core.function_base import linspace
n,m=50,100
a=np.empty(5000).reshape(n,m) 
b=np.random.rand(5000).reshape(n,m) 
c=np.random.rand(5000).reshape(n,m)  #n = filas, m=columnas
a=b+c
#print(a)

# ":" significa todo el rango
# el tercer valor significan los pasos (fila,columna,paso)


##x = np.arange(12).reshape((3,4))
#print(x[::1,2:3])
#y= np.linspace(0,10,10,endpoint=False,retstep=True) #10 elementos (tercer parámetro)
#z= np.logspace(1,3,2) #numero de pasos (2) escala logarítmica
#print(z)











# %%
