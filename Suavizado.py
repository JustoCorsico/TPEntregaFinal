from Funciones.Funciones import plot_array, get_data, cargar_wav, suavizar_hilbert
import numpy as np
from scipy import signal
from scipy import stats

# Metodo de la transformada de Hilbert
wav = r'X:\UnTreF\Python\TPsysEntregaFinalGit\TPEntregaFinal\SegundaEntregaRodeGonzalezCorsico\Mono.wav'
signal_data, fs = get_data(wav)
# duracion = int(len(signal_data)/fs)
# t = np.linspace(0, duracion, len(signal_data))
# def suavizar_hilbert(signal_data):
#     suave_signal = signal.hilbert(signal_data)
#     envelope_suave = np.abs(suave_signal)
#     return (suave_signal, envelope_suave)
suave_signal, envelope_suave = suavizar_hilbert(signal_data)

# Metodo del filtro de promedio movil
señal_fpm = np.cumsum(signal_data)

sch = np.cumsum(señal_fpm[::-1]**2)[::-1]
sch_db = 10.0 * np.log10(sch / np.max(sch))

plot_array(sch_db, fs, 'schroeder', 'Tiempo (s)', 'Amplitud')
plot_array(signal_data, fs, 'Señal no Suavizada', 'Tiempo (s)', 'Amplitud')
plot_array(envelope_suave, fs, 'Envolvente', 'Tiempo (s)', 'Amplitud')
plot_array(señal_fpm, fs, 'Suavizado con Filtro de Promedio Movil', 'Tiempo(s)', 'Amplitud')
