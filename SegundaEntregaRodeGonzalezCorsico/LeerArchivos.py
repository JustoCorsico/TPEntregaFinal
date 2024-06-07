import numpy as np
import soundfile as sf
from matplotlib import pyplot as plt
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.io.wavfile import write
from defs import get_plot
def cargar_archivos():
    '''
    
    '''

    archivo_usuario = []
    mas_archivos = 'y'
    while mas_archivos == 'y':

        archivo_usuario.append(input('Ingrese la ruta del archivo: '))

        mas_archivos = input('¿Desea cargar otro archivo? [y/n]: ')

    print(archivo_usuario)

    return archivo_usuario


        
# C:\Users\Justo\Desktop\SegundaEntrega\Mono.wav
# C:\Users\Justo\Desktop\SegundaEntrega\Mono2.wav

def cargar_wav(file):
    
    data, fs = sf.read(file)
    return(data, fs)

def normalizacion(ir_data):
    ir = ir_data.astype(np.float32)  # Or another appropriate data type


    # Normalize data
    ir = ir / np.max(np.abs(ir))  # Normalize using absolute values
    
    return ir



# MAIN
if __name__ == '__main__':
    archivo_usuario = cargar_archivos()

    for i in range(len(archivo_usuario)):
        data, fs = cargar_wav(archivo_usuario[i])
        ir_norm = normalizacion(data)
        t = np.linspace(0, (len(ir_norm))/fs, (len(ir_norm)))
        get_plot(t, ir_norm)





     



# def plotear_ir(ir, fs, nombre_archivo):
#     plt.plot(np.arange(len(ir)) / fs, ir)
#     plt.xlabel('Tiempo [s]')
#     plt.ylabel('Amplitud')
#     plt.title(nombre_archivo)
#     plt.show()





