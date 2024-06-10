import numpy as np
from scipy import signal
import soundfile as sf
import sounddevice as sd
frecuencia_muestreo=44100
#Octava - G = 1.0/2.0 / 1/3 de Octava - G=1.0/6.0
def filtrar_frec(centerFrequency_Hz,G,i):
    """
    Calcula y aplica un filtro de banda o de tercio de octava a una señal de audio.

    Args:
        centerFrequency_Hz (float): Frecuencia central del filtro en Hz.
        G (float): Factor de ganancia del filtro (1/2 para banda, 1/6 para tercio de octava).
        i (int): Índice de la banda o tercio de octava (para numeración interna).

    Devuelve:
        None: No se devuelve ningún valor, pero se guardan los resultados en archivos WAV.
    """
    factor = np.power(2, G)
    #Calculo los extremos de la banda a partir de la frecuencia central
    lowerCutoffFrequency_Hz=centerFrequency_Hz/factor
    upperCutoffFrequency_Hz=centerFrequency_Hz*factor
    if upperCutoffFrequency_Hz >= (frecuencia_muestreo/2):
        upperCutoffFrequency_Hz = (frecuencia_muestreo/2)-1
    print('Frecuencia de corte inferior: ', round(lowerCutoffFrequency_Hz), 'Hz')
    print('Frecuencia de corte superior: ', round(upperCutoffFrequency_Hz), 'Hz')

    #Extraemos los coeficientes del filtro 
    sos = signal.iirfilter(4, [lowerCutoffFrequency_Hz,upperCutoffFrequency_Hz],rs=60, btype='band', analog=False,ftype='butter', fs=frecuencia_muestreo, output='sos') 
    audiodata,fs=sf.read("ir_posic2-pb_-_sfdc.wav")
    filt = signal.sosfilt(sos, audiodata)
    nombre_archivo=f"Posicion 2ba.wav"
    sf.write(nombre_archivo,filt,fs)
frec_centrales_octava=(31.25, 62.5, 125, 250, 500, 1000, 2000, 4000, 8000,16000)
frec_centrales_tercio=(25,31.5,40,50,63,80,100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150,4000,5000,6300,8000,10000,12500,16000,20000)
tipo_octava=str(input("Ingrese tipo de filtro(tercio/banda): "))
if tipo_octava=="banda":
    G=1/2
    octava_elegida=frec_centrales_octava
else: 
    G=1/6
    octava_elegida=frec_centrales_tercio
for i in range(len(octava_elegida)):
    filtrar_frec(octava_elegida[i],G,i)




