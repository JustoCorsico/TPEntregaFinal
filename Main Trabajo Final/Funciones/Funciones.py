from matplotlib import pyplot as plt
import numpy as np
from ipywidgets import Button
from tkinter import Tk, filedialog
from IPython.display import clear_output, display
import soundfile as sf
from scipy.io import wavfile
import os
import sounddevice as sd
from scipy import signal
import pandas as pd
import math
import pyrato
def plot_array(np_array,sample_rate,titulo,name_x,name_y):

    """
 Plots a vectorized signal.

    Parameters:
        np_array (numpy.ndarray): The signal vector to plot.
        sample_rate (int): The sampling rate.
        title (str): The title of the plot (in quotes).
        name_x (str): The name of the X-axis (in quotes).
        name_y (str): The name of the Y-axis (in quotes).

    Example of use:

        >>> signal = np.array([1, 2, 3, 4, 5])
        >>> plot_array(signal, 44100, "My signal", "Time (s)", "Amplitude")

    Displays a plot with the signal "signal" on the Y-axis and time on the X-axis.
    """
    duracion=(len(np_array)/sample_rate)
    t=np.linspace(0,duracion,len(np_array))
    plt.plot(t,np_array)
    plt.xlim((0,duracion))
    plt.xlabel(name_x)
    plt.ylabel(name_y)
    plt.title(titulo)
    plt.show()
 
def cargar_wav():
    """
    Allows the user to load WAV files.

    return: A list with the files path.
    """
    files = []
    def select_files():
        clear_output()
        root = Tk()
        root.withdraw() # Hide the main window.
        root.call('wm', 'attributes', '.', '-topmost', True) # Raise the root to the top of all windows.
        files.append(filedialog.askopenfilenames()) # List of selected files will be set button's file attribute.
        print(files) # Print the list of files selected.
    fileselect = Button(description="Seleccione el archivo")
    fileselect.on_click(select_files)
    select_files()
def normalizacion(signal):
    norm_signal = (signal* np.iinfo(np.int16).max).astype(np.int16)
    return norm_signal


def plot_wav(wav_path):
    """
    Plots the waveform of a WAV audio file.

    Args:
      wav_path (str): Path to the WAV audio file.
    """
    sample_rate, data = wavfile.read(wav_path)
    duracion=(len(data)/sample_rate)
    t=np.linspace(0,duracion,len(data))
    plt.plot(t,data)
    plt.xlim((0,duracion))
    plt.xlabel("Amplitud")
    plt.ylabel("Tiempo(S)")
    plt.title(os.path.basename(wav_path))
    plt.show()

def get_wav(myrecording):
    """
    Generates a WAV file from an array:

        Parameters:
        myrecording: 

    """
    frec_sampleo=int(input("Ingrese frecuencia de sampleo: "))
    audio2 = (myrecording* np.iinfo(np.int16).max).astype(np.int16)
    name=(input("Ingrese Nombre del archivo: "))+".wav"
    wavfile.write(name,frec_sampleo,audio2)
    
def get_data(archivo_wav):
    """
    Vectorize a WAV file
    Parameters:
        archivo_wav(WAV): WAV file name
    Return: 
        data(np_array):Array with amplitude values  
        fs(int): WAV file samplerate
    """  
    data,fs=sf.read(archivo_wav)
    return data,fs
def conv_logaritmica(array,sample_rate):
    Audio=array/max(abs(array))
    epsilon = 1e-12
    Audio[Audio==0]=epsilon
    Audio[Audio<0]=np.abs(Audio[Audio<0])
    Audio_log=20*np.log10(Audio)
    return Audio_log
    
def funcion_multiple(signal_data):
    """
    """
    analytic_signal = signal.hilbert(signal_data)
    hilbert = np.abs(analytic_signal)

    windows=int(input("Ingrese cantidad muestras a utilizar para el suavizado:"))
    df = pd.DataFrame(hilbert)
    df["Promedio movil"]=df.rolling(windows).mean()
    prom_movil=(df["Promedio movil"]).to_numpy()

    schroeder=pyrato.schroeder_integration(prom_movil,is_energy=False)

    return (hilbert,prom_movil,schroeder)   

def cuadrados_minimos(schroeder_function):
    t=np.linspace(0,len(schroeder_function)/44100,len(schroeder_function))
    x_i=np.sum(t)
    y_i=np.sum(schroeder_function)
    x_mean=np.mean(t)
    y_mean=np.mean(schroeder_function)
    n=len(schroeder_function)
    a1=(n*(np.sum(schroeder_function*t))-x_i*y_i)/(n*np.sum(t**2)-x_i**2)
    a2=(y_i*np.sum(t**2)-x_i*np.sum(t*schroeder_function))/(n*np.sum(t**2)-x_i**2)
    v2=[a2]*len(schroeder_function)
    y=a1*t+v2
    t60=(-60-a2)/a1
    print(t60)
    return y    