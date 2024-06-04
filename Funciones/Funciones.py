from matplotlib import pyplot as plt
import numpy as np
from ipywidgets import Button
from tkinter import Tk, filedialog
from IPython.display import clear_output, display
import soundfile as sf
from scipy.io import wavfile
import os
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
    duracion=(len(np_array)//sample_rate)
    t=np.linspace(0,duracion,duracion*sample_rate)
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
    


def plot_wav(wav_path):
    sample_rate, data = wavfile.read(wav_path)
    duracion=(len(data)//sample_rate)
    t=np.linspace(0,duracion,duracion*sample_rate)
    plt.plot(t,data)
    plt.xlim((0,duracion))
    plt.xlabel("Amplitud")
    plt.ylabel("Tiempo(S)")
    plt.title(os.path.basename(wav_path))
    plt.show()