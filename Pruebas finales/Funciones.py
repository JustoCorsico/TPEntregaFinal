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
import sympy as sym
import time
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
    plt.xlim(0,duracion)
    plt.xlabel(name_x)
    plt.ylabel(name_y)
    plt.title(titulo)
    plt.show()

def plot_arrays(np_arrays, sample_rate, titulo, name_x, name_y, leyendas):

    """
    Plots two vectorized signals.
    Parameters:
        np_array1 (numpy.ndarray): The first signal vector to plot.
        np_array2 (numpy.ndarray): The second signal vector to plot.
        sample_rate (int): The sampling rate.
        titulo (str): The title of the plot (in quotes).
        name_x (str): The name of the X-axis (in quotes).
        name_y (str): The name of the Y-axis (in quotes).

    Example of use:

        >>> signal1 = np.array([1, 2, 3, 4, 5])
        >>> signal2 = np.array([5, 4, 3, 2, 1])
        >>> plot_array(signal1, signal2, 44100, "My signals", "Time (s)", "Amplitude")

    Displays a plot with the two signals on the Y-axis and time on the X-axis,
    distinguished by different colors (blue and red).
    
    """
    colores=["blue","red","green"]
    t=np.linspace(0,len(np_arrays[0])/sample_rate,len(np_arrays[0]))
    plt.legend(leyendas[0])
    plt.plot(t,np_arrays[0],colores[0])
    t=np.linspace(0,len(np_arrays[1])/sample_rate,len(np_arrays[1]))
    plt.legend(leyendas[1])
    plt.plot(t,np_arrays[1],colores[1])
    t=np.linspace(0,len(np_arrays[2])/sample_rate,len(np_arrays[2]))
    plt.legend(leyendas[2])
    plt.plot(t,np_arrays[2],colores[2])
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

def conv_logaritmica(signal_data):
    """
    Converts a based-bit array into a based-logaritmic array
    Parameters:
        signal_data(np_array):Array in bits scale
    Return:
        array_log(np_array):Array in logaritmic scale (dB)
    """
    array_log=20*np.log10(signal_data/np.max(signal_data))

    return array_log
    
def hilbert_envolve(signal_data):
    """
    Generates the envolve audio signal using scipy.hilbert method
    Parameters:
        signaldata(np_array):Signal data array
    Return:
        h_envolve(np_array):Envolve array

    """
    analytic_signal = signal.hilbert(signal_data)
    h_envolve = np.abs(analytic_signal)

    return (h_envolve) 

def moving_average_envolve(signal_data):
    """
    Generates the envolve audio signal using moving average method
    Parameters:
        signaldata(np_array):Signal data array
    Return:
        ma_envolve(np_array):Positive envolve array
    """

    n_windows=int(input("Ingrese cantidad muestras a utilizar para el suavizado:"))
    df = pd.DataFrame(signal_data)
    df["Promedio movil"]=df.rolling(n_windows).mean()
    ma_envolve=(df["Promedio movil"]).to_numpy()

    return (ma_envolve)    

def schroeder_envolve(signal_data):
    """
    Generates the envolve audio signal using schroeder integr method
    Parameters:
        signaldata(np_array):Signal data array
    Return:
        schroeder(np_array):Envolve array
    """
    sch_env=pyrato.schroeder_integration(signal_data,is_energy=True)
    return sch_env
def cuadrados_minimos(schroeder_function):
    """
    Fits a least squares linear regression to the provided Schroeder function data.

    Calculates the coefficients `a0` (y-intercept) and `a1` (slope). Additionally,
    computes the coefficient of correlation `r` to assess the strength and direction
    of the linear relationship.

    Args:
        schroeder_function (numpy.ndarray): A 1D NumPy array containing the
            Schroeder function data points.

    Returns:
        tuple: A tuple containing three elements:

            - f (numpy.ndarray): The fitted least squares linear regression function
                represented as a NumPy array.
            - a0 (float): The y-intercept of the fitted line.
            - a1 (float): The slope of the fitted line.

    """
    # Variables xi
    t=np.linspace(0,len(schroeder_function)/44100,len(schroeder_function))
    xm=np.mean(t)
    ym=np.mean(schroeder_function)
    n=len(schroeder_function)

    # Sumatorias
    sx=np.sum(t)
    sy=np.sum(schroeder_function)
    sxy=np.sum(schroeder_function*t)
    sx2=np.sum(t**2)
    sy2=np.sum(schroeder_function**2)

    # obtencin de a0 y a1
    a1=(n*sxy-sx*sy)/(n*sx2-sx**2)
    a0=ym - a1*xm
    f=a0+a1*t

    # Coeficiente de Correlación 'r'
    numerador = n*sxy - sx*sy
    raiz1 = np.sqrt(n*sx2-sx**2)
    raiz2 = np.sqrt(n*sy2-sy**2)
    r = numerador/(raiz1*raiz2)
    # print('Coeficiente de Correlacion= ', r)

    return f, a1
# Igresar con las señal filtrada y suavizada, no schroeder logaritmico
def calcular_c80(signal, fs):
    """
    Calcula el índice de claridad C80 para una señal dada.
    
    :param signal: La señal de presión p(t) como un array de valores.
    :param fs: Frecuencia de muestreo de la señal en Hz.
    :return: El índice de claridad C80 en dB.
    """
    # Convertir el tiempo de 0.08 segundos a muestras
    t_80 = int(0.08 * fs)
    
    # Calcular p^2(t)
    p_squared = signal ** 2
    
    # Integrar desde 0 a 0.08 segundos
    num_integral = np.sum(p_squared[:t_80]) / fs
    
    # Integrar desde 0.08 segundos hasta el final
    denom_integral = np.sum(p_squared[t_80:]) / fs
    
    # Calcular C80
    C80 = 10 * np.log10(num_integral / denom_integral)
    
    return C80

def calcular_d50(signal, fs):
    """
    Calcula el parámetro D50 para una señal dada.
    
    :param signal: La señal de presión p(t) como un array de valores.
    :param fs: Frecuencia de muestreo de la señal en Hz.
    :return: El parámetro D50.
    """
    # Convertir el tiempo de 0.05 segundos a muestras
    t_50 = int(0.05 * fs)
    
    # Calcular p^2(t)
    p_squared = signal ** 2
    
    # Integrar desde 0 a 0.05 segundos
    num_integral = np.sum(p_squared[0:t_50]) / fs
    
    # Integrar desde 0 segundos hasta el final
    denom_integral = np.sum(p_squared) / fs
    
    # Calcular D50
    D50 = num_integral / denom_integral

    return D50

def rt_trim_window(log_sch, rt):
    """
    
    
    :param signal: La señal de presión p(t) como un array de valores.
    :param fs: Frecuencia de muestreo de la señal en Hz.
    :return: El parámetro D50.
    """
    mindb = 0
    # indice_m5db = None
    for x in range(len(log_sch)):
        if log_sch[x] < -5:
            # indice_m5db = x
            mindb = x
            break
    # indice_m25db = None
    maxdb = 0
    for x in range(len(log_sch)):
        if log_sch[x] < -rt-5:
            # indice_m25db = x
            maxdb = x
            break
    
    window = log_sch[mindb:maxdb]
    return window
    

def get_data():
    f1 = int(input('Ingrese frecuencia inferior:'))
    f2 = int(input('Ingrese frecuencia superior:'))
    T = int(input('Ingrese T: '))
    return (f1, f2, T)

def sweep_data(f1, f2, T):
    w1 = 2 * np.pi * f1
    w2 = 2 * np.pi * f2
    w1=2*np.pi*f1
    w2=2*np.pi*f2   
    R = np.log(w2/w1)
    K = float((T*w1)/R) 
    L = T/R
    fs=44100
    t = np.linspace(0,T,T*fs)
    f = np.sin(K*(np.exp(t/L)-1))
    return (f, t, R, K, L, w1, fs)

def normalize_signal(f,kt):
    g = f / np.max(np.abs(f))
    j = kt / np.max(np.abs(kt))
    return (g,j)

def get_signalwav(array,fs,name):
    audio1 = (array * np.iinfo(np.int16).max).astype(np.int16)
    wavfile.write(name+".wav",fs, audio1)

def get_inverse_filter(f, K, L, T, t, w1):
    ssi = np.flip(f)
    wt = (K/L)*np.exp(t/L)
    mt = w1/(2*np.pi*wt)
    kt = mt*ssi
    return (kt, ssi)

def get_convolve(f, kt):
    conv = np.convolve(f, kt)
    return(conv) 

def ruidoRosa_voss(nrows, ncols):
    array = np.full((nrows, ncols), np.nan)
    array[0, :] = np.random.random(ncols)
    array[:, 0] = np.random.random(nrows)
    
    # el numero total de cambios es nrows
    n = nrows
    cols = np.random.geometric(0.5, n)
    cols[cols >= ncols] = 0
    rows = np.random.randint(nrows, size=n)
    array[rows, cols] = np.random.random(n)
    
    df = pd.DataFrame(array)
    filled = df.ffill(axis=0)
    total = filled.sum(axis=1)
    
    ## Centrado de el array en 0
    total = total - total.mean()
    
    ## Normalizado
    valor_max = max(abs(max(total)),abs(min(total)))
    total = total / valor_max
    return total

def get_data_play_rec():
    print(sd.query_devices())
    mic=int(input("Ingrese numero de dispositivo de entrada:"))
    spkr=int(input("Ingrese numero de dispositivo de salida:"))
    return(mic,spkr)

def playrecord(mic,spkr,sample_rate):
    t=int(input("Ingrese tiempo de grabacion y reproducción:"))
    sd.default.samplerate =sample_rate 
    sd.default.device=mic,spkr
    sd.default.channels=1
    myrecording = sd.playrec(data,channels=1)
    time.sleep(t)
    sd.stop() 
    return myrecording
        


        


