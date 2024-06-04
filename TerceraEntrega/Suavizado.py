from defs import cargar_wav, get_plot
import numpy as np
from scipy import signal

ruta = r'C:\Users\Justo\Desktop\SegundaEntrega\Mono.wav'
data, fs = cargar_wav(ruta)
duracion = int(len(data)/fs)
t = np.linspace(0, duracion, len(data))
# tmin = np.min(t)
# print(tmin)
# t = t + tmin
# hilbert = 1/((np.pi)*t)
suave = signal.hilbert(data)
realmente_suave = np.real(suave)
get_plot(t, data)
get_plot(t, realmente_suave)

