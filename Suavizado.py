from Funciones.Funciones import plot_array, leer_wav, cargar_wav
import numpy as np
from scipy import signal


wav = cargar_wav()
signal_data, fs = leer_wav(wav)
# duracion = int(len(signal_data)/fs)
# t = np.linspace(0, duracion, len(signal_data))
def suavizar_hilbert(signal_data):
    suave_signal = signal.hilbert(signal_data)
    envelope_suave = np.abs(suave_signal)
    return (suave_signal, envelope_suave)
suave_signal, envelope_suave = suavizar_hilbert(signal_data)
plot_array(signal_data, fs, 'Señal no Suavizada', 'Tiempo (s)', 'Amplitud')
plot_array(envelope_suave, fs, 'Envolvente', 'Tiempo (s)', 'Amplitud')