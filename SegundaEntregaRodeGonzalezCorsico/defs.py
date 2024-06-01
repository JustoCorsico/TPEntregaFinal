import numpy as np
from matplotlib import pyplot as plt
import simpleaudio as sa
from scipy.io import wavfile
import pandas as pd
import soundfile as sf

def get_signalwav(n):
    audio1 = (n * np.iinfo(np.int16).max).astype(np.int16)
    wavfile.write("Sine Sweep.wav", fs, audio1)

def get_plot(t, f):
    plt.plot(t,f)
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.show()