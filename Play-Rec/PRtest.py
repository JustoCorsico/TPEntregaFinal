import sounddevice as sd
import numpy as np
import soundfile as sf
from scipy.io import wavfile
t=int(input("Ingrese tiempo de grabacion y reproducción:"))
data, frec = sf.read("Sine Sweep.wav", dtype='float32')
print(sd.query_devices())
mic=int(input("Ingrese numero de dispositivo de entrada:"))
spkr=int(input("Ingrese numero de dispositivo de salida:"))
sd.default.samplerate = frec
sd.default.device=mic
sd.default.channels=2
myrecording = sd.rec(t * frec, blocking=True)
sd.default.device=spkr
sd.play(data)
sd.wait()
audio2 = (myrecording * np.iinfo(np.int16).max).astype(np.int16)
wavfile.write("grabetas2.wav",frec,audio2)