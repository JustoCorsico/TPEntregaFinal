from Funciones import get_data
from Funciones import conv_logaritmica
from Funciones import plot_array
from Funciones import funcion_multiple
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp
import numpy as np

signal,fs=get_data("untitled.wav")
señal,envelope,suave=funcion_multiple(signal)
duracion=len(signal)/fs
t=np.linspace(0,duracion,len(signal))

fig, (ax0) = plt.subplots(nrows=1)
ax0.plot(t, signal, label='signal')
ax0.plot(t, suave , label='envelope')
plt.show()