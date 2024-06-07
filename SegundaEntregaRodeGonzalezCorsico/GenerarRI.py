import numpy as np
from tkinter import *
from IPython.display import clear_output, display
from tkinter import filedialog
import soundfile as sf
from scipy import signal
from scipy.io.wavfile import write
from LeerArchivos import normalizacion
from defs import get_plot
import simpleaudio
from scipy.io import wavfile





def IR_sint(t, f_i, RT_i, tiempo_impulso, frec_muestreo):
    
    
    tau_i = np.log(10**(-3))/RT_i
    y_i = (np.exp(tau_i*t))*np.cos(2*np.pi*f_i*t)

    return y_i


# Main

tiempo_impulso=6
frec_muestreo=44100
t = np.linspace(0, tiempo_impulso, tiempo_impulso*frec_muestreo)

# Bandas de Octava según IEC 61260
nominal_frec = [31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
# Genero un vector con T60i para cada frecuencia con los datos de Openair.com, Usina del Arte Symphony Hall 
RT_xfrec_list = [2.15, 1.48, 1.63, 1.91, 2.08, 2.09, 1.82, 1.6, 1.18, 1.11]
RT_xfrec_list2 = [10, 10, 10, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
RT_xfrec_list3 = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

decay = []

for i in range(len(nominal_frec)):
    decay.append(IR_sint(t, nominal_frec[i], RT_xfrec_list[i], tiempo_impulso, frec_muestreo))

impulso = sum(decay)

# Normalizado
norm_impulse = normalizacion(impulso) 

name = input('Nombrar archivo wav: ')
def get_signalwav(señal, frec_muestreo, name):
    audio1 = (señal * np.iinfo(np.int16).max).astype(np.int16)
    wavfile.write(name + '.wav', frec_muestreo, audio1)

get_signalwav(norm_impulse, frec_muestreo, name)
get_plot(t, norm_impulse)






