import numpy as np
from numpy.core.defchararray import array 


#Alias. U would to use other alias

#get information of elements Numpy
#np.lookfor('solve')

#version
#print(np.__version__)

#constante:
#np.pi
#np.e 


#funciones matemáticas
#np.log
#np.sin 
#np.cos 

#degrees(x) Convierte rad to grades
# radians(x) Covierte grade to rad



#ARRAYS IS LIKE LIST
#invoke array:
#np.array([1,2,3])


#Indicate type array:
#print(np.array([1,2,3], dtype=float))

#np.array([1,2,3]), dtype=complex)
#array([1.+0.j, 2.+0.j, 3.+0.j])

#convertir tipos
#a = np.array([4,5,6])

#a.astype('int')
#array([1,2,3])


#Crear arreglo muy fácil y para gran cantidad de datos:

#a=np.empty(5000)

#Modificar la forma:

#a.reshape(50,100)

#Ejemplo: unidimensional a bidimensional (e incluso tridimencional)
a=np.empty(12) #matriz vacía de dim 12
b=a.reshape(2,6) #las dimensiones tienen que coincidir con la matriz original
# b=a.reshape(2,2,3)
print(b)













