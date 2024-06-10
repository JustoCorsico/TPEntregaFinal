from Funciones import get_data
from Funciones import conv_logaritmica
from Funciones import plot_array
from Funciones import hilbert_envolve
from Funciones import get_wav
from Funciones import cuadrados_minimos
from Funciones import plot_arrays
from Funciones import schroeder_envolve
from Funciones import moving_average_envolve

# from Funciones import recortar_decaimiento_audio

from Funciones import calcular_c80, calcular_d50
from Funciones import ventaneo

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp
import numpy as np
from Funciones import normalizacion


import pyrato

# PROCESAMIENTO
signal,fs=get_data("impulso filtrado tercio8.wav")

envolvente_hilbert=hilbert_envolve(signal)
ma_signal =moving_average_envolve(envolvente_hilbert)

schroeder = schroeder_envolve(ma_signal)

log_sch = conv_logaritmica(schroeder)
log_hil = conv_logaritmica(envolvente_hilbert)

ventana10=ventaneo(log_sch,10)
ventana20=ventaneo(log_sch,20)
ventana30=ventaneo(log_sch,30)

f10,a10=cuadrados_minimos(ventana10)
f20,a20=cuadrados_minimos(ventana20)
f30,a30=cuadrados_minimos(ventana30)

t10=(-60)/a10
t20=(-60)/a20
t30=(-60)/a30
print("EL T30 ES:",t30)
print("EL T20 ES:",t20)
print("EL T10 ES:",t10)

# Cálculo de D50 y C80
# D50 = calcular_d50(smoothed_signal,fs)
# C80 = calcular_c80(smoothed_signal,fs)
# print('D50= ', D50, 'C80= ', C80)



# PLOT
# plot_array(signal, fs,"Impulso Original","x","y")
#plot_array(log_signal, fs,"Impulso en escala Logaritmica","x","y")
# plot_array(smoothed_signal,fs,"Impulso Suavizado","x","y")
#plot_array(log_hil, fs,"Schoeder Decay","x","y")
plot_array(ma_signal, fs,"ventana10","x","y")
plot_array(log_sch, fs,"lundeby","x","y")
#plot_arrays((ventana10,ventana20,ventana30), fs, 'f10,f20,f30',"x","y",("T10","T20","T30"))
#plot_array(f, fs, 'Ventana entre 5 y 15 db', 'x', 'y')

