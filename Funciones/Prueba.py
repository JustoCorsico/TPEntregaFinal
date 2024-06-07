from Funciones import conv_logaritmica
from Funciones import get_data
from Funciones import plot_array
audio,fs=get_data("Mono.wav")
log_array=conv_logaritmica(audio,fs)
plot_array(audio,fs,"Audio sin logartimos","X","Y")
plot_array(log_array,fs,"Audio con logaritmos","X","Y")