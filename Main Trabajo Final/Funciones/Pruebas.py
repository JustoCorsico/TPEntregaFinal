from Funciones import get_data
from Funciones import conv_logaritmica
from Funciones import plot_array
from Funciones import funcion_multiple
from Funciones import get_wav
from Funciones import cuadrados_minimos
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp
import numpy as np
from Funciones import normalizacion
import pyrato

signal,fs=get_data("impulso filtrado tercio6.wav")

hilber,prom_movil,schroeder=funcion_multiple(signal)
log_signal=conv_logaritmica(schroeder,fs)
recta=cuadrados_minimos(schroeder)
plot_array(log_signal,fs,"schroeder","x","y")