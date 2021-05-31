import matplotlib.pyplot as plt
import numpy as np

#Consola interactiva
#%%
plt.ioff()
#preparar los datos
x=np.linspace(0,10,10)
plt.plot(x,np.sin(x),label="Seno",color="r")
plt.plot(np.cos(x),label="Coseno",color="y")

plt.show()
# %%
