from Funciones.Funciones import cargar_wav, plot_array, leer_wav
import numpy as np
from scipy import signal


wav = cargar_wav()
signal_data, fs = leer_wav(wav)
duracion = int(len(signal_data)/fs)
# t = np.linspace(0, duracion, len(data))
def suavizar_hilbert(signal_data):
    suave_signal = signal.hilbert(signal_data)
    envelope_suave = np.abs(suave)
    return 
get_plot(t, signal_data)
get_plot(t, envelope_suave)


