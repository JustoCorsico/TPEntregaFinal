import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy import signal
import soundfile as sf
from scipy.io import wavfile
from defs import get_plot
from LeerArchivos import normalizacion, cargar_archivos
from GenerarRI import get_signalwav

def obtenerRI(archivo_usuario):
    """
    Calcula la respuesta al impulso (RI) a partir de un archivo de seno y su inverso.

    Args:
        archivo_usuario (list): Lista con dos rutas de archivos:
            - Archivo de seno.
            - Archivo de filtro inverso.

    Devuelve:
        (tuple): Tupla que contiene la respuesta al impulso (RI) y la frecuencia de muestreo (fs).
    """
    read_sine, fs = sf.read(archivo_usuario[0])
    read_inv_filt, fs = sf.read(archivo_usuario[1])
    imp_res = signal.fftconvolve(read_sine, read_inv_filt, mode='full')
    return imp_res, fs

def imp_wav(señal, frec_muestreo, name):
    """
    Guarda una señal de audio normalizada en un archivo WAV.

    Args:
        señal (ndarray): Matriz de datos de audio.
        frec_muestreo (int): Frecuencia de muestreo en Hz.
        name (str): Nombre del archivo WAV a generar.
    """
    audio1 = (señal * np.iinfo(np.int16).max).astype(np.int16)
    wavfile.write(name + '.wav', frec_muestreo, audio1)

# X:\UnTreF\Python\TPgit\SegundaEntrega\Filtro inversoGENERADO.wav
# X:\UnTreF\Python\TPgit\SegundaEntrega\Sine SweepGENERADO.wav

archivo_usuario = [r'X:\UnTreF\Python\TPgit\SegundaEntrega\filtro_inverso.wav', r'X:\UnTreF\Python\TPgit\SegundaEntrega\Toma_n1_a-03.wav']

filtro_inverso = 'Filtro inversoGENERADO.wav'
sine_sweep = 'Sine SweepGENERADO.wav'
imp_res, fs = obtenerRI(archivo_usuario)
imp_res_norm = normalizacion(imp_res)
t = np.linspace(0, (len(imp_res))/fs, (len(imp_res)))
name = input('Nombrar archivo wav: ')
imp_wav(imp_res_norm, fs, name)
get_plot(t, imp_res_norm)
