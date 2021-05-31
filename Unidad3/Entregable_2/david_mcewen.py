# -*- coding: utf-8 -*-
#DAVID MCEWEN ARANGO, GRUPO 2, INFORMÁTICA II.



"""
Created on Fri Dec  4 11:10:51 2020

@author: dmcew
"""

#Realice un módulo en Python que permita el tratamiento básico de señales. 
#Para hacerlo tenga en cuenta lo siguiente:
    
#4.1. Un objeto que contenga toda la información relevante de una señal, 
    #como lo son las dimensiones (número de canales, épocas y puntos), frecuencia de 
    #muestreo y la señal. Dicha señal es cargada desde un archivo con extensión mat.
#4.2. Un método que permita redimensionar, o extraer partes de la señal. Especifique 
    #por medio de argumentos los canales y épocas que se deseen utilizar.
#4.3. Un método que permita calcular algunas variables estadísticas de la señal, 
    #tales como media, desviación estándar, valor máximo y valor mínimo. 
    #Especifique por medio de argumentos los canales y épocas que se desean analizar.

#4.5. Un método que permita graficar cualquier segmento de la señal, 
    #utilizando etiquetas en los ejes (tiempo vs amplitud), un título que contenga el 
    #canal y épocas graficadas. Es necesario especificar por medio de argumentos el 
    #canal o época que se desee graficar.
#4.6. Realizar un código donde se muestra en funcionamiento cada uno de los 
    #métodos del objeto que contiene el módulo.
    
import numpy as np;
import matplotlib.pyplot as plt;
import scipy.io as sio;



mat_contents = sio.loadmat('C001R_EP_reposo.mat') #Cargar archivo .mat
data = mat_contents["data"] #Acceder a los datos del diccionario
canales = data.shape[0] #extraer los canales
puntos = data.shape[1] #" " "
epocas = data.shape[2]

promedio_dato= np.mean(data,1) #Promedio
desviacion_dato=np.std(data,1) #el 1 significa las muestras, es decir, promedia de los puntos
valor_minimo = np.amin(data,0) #retorna valor minimo. Valor mínimo de los canales. Valor máx de las épocas
valor_maximo = np.amax(data,2) #Retorna valor máximo
print("El promedio es: " + str(promedio_dato.shape))
print("La desviación estandar es: " + str(desviacion_dato.shape))
print("El valor mínimo es: " + str(valor_minimo.shape)) #si no usas shape, te muestra los valores y no las dimensiones
print("El valor máximo es " + str(valor_maximo.shape))


print("Dimensiones de los datos cargados: " + str(data.shape))
print("Numero de dimensiones: " + str(data.ndim))
print("Tamaño (canales*muestras*): " + str(data.size))
print("Tamanio en memoria (bytes): " + str(data.nbytes))
print("Número de canales: "+str(len(data[:])))
#print("Número de muestras: " +str(len(data[None,:]))) (NO)
print("numero de canales: " + str(canales))
print("Numero de épocas: " +str(epocas))
print("Numero de puntos: " +str(puntos))

#CONVERTIR LA SEÑAL A CONTINUA: 3d to 2d
dataTo2d = np.reshape(data,(data.shape[0],data.shape[1]*data.shape[2]), order="F") #"F" Form in that python read the info
print(dataTo2d.shape) #Convert to 2d (señal continua)

#GRAFICAR SEGMENTOS DE LA SEÑAL CARGADA:

#Opcional y no menos importante, para organizar cuando hay muchas muestras:
#for canal in range(dataTo2d.shape[0]):
    #plt.plot(dataTo2d[canal,2000:4000]+ canal*10,label="canal"+str(canales))

plt.plot(dataTo2d[5,0:5000], label="Muestra") #Graficamos un canal y muestra en específico. ya no hay épocas
plt.title("Canal 5, muestras 0 a 5000") #Título
plt.xlabel("Tiempo") #eTIQUETA axis x
plt.ylabel("Potencia") #Axis y
plt.legend() #Esto permite clasificar los ejes. Sin esto, no se vería a la hora de plotear
plt.grid(True) #Rendijas bien chidas 
plt.show() #Así como en PyQT5, sirve pa' mostrar gráficos con ejes. Existe Bar, Hist, Pie, etc.
