#from matplotlib import ft2font
#%%
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np

#Consola interactiva

plt.ion()
#preparar los datos
x=np.linspace(0,10,10)
plt.plot(x,np.sin(x),label="Seno",color="r")
plt.plot(np.cos(x),label="Coseno",color="k")

plt.show()

#%%
import matplotlib.pyplot as plt
import numpy as np
datos=np.arange(0,360)
datos=np.radians(datos)
datos=np.sin(datos)
plt.plot(datos,"m--")
plt.show()
#fig.savefig()
# %%

#Para manipular los ejes:
#axis([x1,x2,y1,y2])

#%% 
import numpy as np
import matplotlib.pyplot as plt
#datos=np.arange(0,100)
#plt.plot(datos)
#RECUERDA plot([y],[x])
plt.plot([1,2,3,4],[10,20,25,30],color='lightblue', linewidth=3)
plt.axis([0,10,0,50])
plt.title("Ejemplo")
plt.show()


# %%

#%%

import numpy as np
import matplotlib.pyplot as plt

datos=np.arange(0,360)
datos=np.radians(datos)
datos=np.sin(datos)
plt.plot(datos, label="Sin function")
plt.xlabel('x')
plt.ylabel('y')
plt.legend() #activa la legenda
plt.show()

# %%
import numpy
import matplotlib.pyplot as plt
fig=plt.figure()
fig1=fig.add_subplot()
fig1.set_xlabel("Nombre")
fig1.set_ylabel("Nombre")
fig1.plot(datos)


#%%
#Creación de histogramas
import numpy as np
import matplotlib.pyplot as plt
data=np.random.randn(500)
plt.hist(data)

# %%


#%%
import numpy as np
import matplotlib.pyplot as plt
labels='Bioseñales','Bioinstrumentacion','Bioinformática','biomateriales','otras'
colors=['green','pink','coral','lightskyblue','blue']
sizes=[25,27,22,23,3]
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.show()
# %%
