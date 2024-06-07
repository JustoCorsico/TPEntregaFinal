from Funciones import get_data
from Funciones import conv_logaritmica
from Funciones import plot_array
from Funciones import funcion_multiple
from Funciones import get_wav
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp
import numpy as np
from Funciones import normalizacion


signal,fs=get_data("Mono.wav")
norm_signal=conv_logaritmica(signal,fs)
t=np.linspace(0,len(norm_signal)/fs,len(norm_signal))
hilber,prom_movil=funcion_multiple(signal)
fig, (ax0) = plt.subplots(nrows=1)
ax0.plot(t, signal, label='original')
ax0.plot(t, hilber, label='Hilber')
ax0.plot(t, prom_movil, label="Prom Movil")
plt.show()
get_wav(hilber)
get_wav(prom_movil)