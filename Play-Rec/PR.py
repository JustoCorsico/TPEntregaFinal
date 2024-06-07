import sounddevice as sd
import wavio
import timeit
import matplotlib.pyplot as plt
print(sd.query_devices())
elegir_input = int(input("Elija el input a utilizar: "))
elegir_output = int(input("Elija el output a utilizar: "))
#sd.default.device = elegir_input, elegir_output
samplerate = sd.query_devices(elegir_output, 'output')['default_samplerate']
# Nombre del archivo de salida (grabación)
filename = "Grabacion.wav"
# Nombre del archivo WAV a reproducir
def reproducir_y_grabar_wav(wav_filename, duration=10, fs=44100):
    print("Reproduciendo y grabando", wav_filename)
    wav_data = wavio.read(wav_filename).data
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    # sd.wait()  # Espera a que comience la grabación
    sd.play(wav_data, samplerate)  # Reproduce la señal
    sd.wait()  # Espera a que termine la reproducción
    wavio.write(filename, recording, fs, sampwidth=2)
    print("Reproducción y grabación completadas. Archivo de grabación guardado como", filename)
    return recording, fs

# Latencia
# def latencia(titulo, tiempo):
#     start_time = timeit.default_timer() # Comienzo de la función
#     reproducir_y_grabar_wav(titulo, tiempo)
#     duracion = timeit.default_timer() - start_time
#     # La diferencia entre la duración de ejecución y el tiempo de grabación es la latencia
#     latencia = duracion-tiempo
#     return latencia
# def visualizar(wav_filename, titulo= "Latencia"):
#     plt.plot(wav_filename)
#     plt.title(titulo,size=16)
#     plt.xlabel("Tiempo [s]")
#     plt.ylabel("Amplitud")
#     plt.show()
# if __name__ == "__main__":
#     lat = latencia(wav_filename, 10)
#     print(f'La latencia de la función es de {lat} segundos')
# visualizar(wav_filename, "Latencia")