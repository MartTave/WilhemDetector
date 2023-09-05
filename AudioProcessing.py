import numpy as np
import librosa
import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve
from scipy.signal import find_peaks
import scipy.signal
from scipy import fftpack
from scipy.io import wavfile

#material
scream_file = "C:/Users/capma/Desktop/ADSR/scream.wav"
movie_file = "C:/Users/capma/Desktop/ADSR/movie.wav"
movie6_file = "C:/Users/capma/Desktop/ADSR/movie6.wav"

#load audio files
scream, srr = librosa.load(scream_file)
movie6, sr = librosa.load(movie6_file)

#display
ipd.Audio(movie6_file)

# duration of 1 sample
sample_duration = 1 / sr
print(f"Duration of 1 sample is: {sample_duration:.6f} seconds")

#duration of the audio signal in seconds
duration_movie6 = sample_duration * len(movie6)
print(f"Duration of the signal is: {duration_movie6:2f} seconds")
#duration of the scream signal in seconds
duration_scream = sample_duration * len(scream)
print(f"Duration of the signal is: {duration_scream:2f} seconds")

def checkCorrelate (template, test):

    return np.convolve(template,test, mode='same')

resultCorrelate = checkCorrelate(scream, movie6)

#display result
librosa.display.waveshow(resultCorrelate, axis="s")

sampleNumberScream = duration_scream*sr
peaks, _ = find_peaks(resultCorrelate, height=27, threshold=2, distance=sampleNumberScream)
plt.plot(resultCorrelate)
plt.plot(peaks, resultCorrelate[peaks], "o")
plt.show()

#convert peaks sample into seconds


def sampleIntoSeconds (nrSample, sampling_rate):

    seconds = []

    for peak in peaks:
        time_in_seconds = peak / sampling_rate
        seconds.append(time_in_seconds)

    return seconds

seconds_peaks = sampleIntoSeconds(peaks, sr)

with open("C:/Users/capma/Desktop/ADSR/peak_times.txt", "w") as file:
    for peak in seconds_peaks:
        minutes = int(peak // 60)
        seconds = int(peak % 60)
        milliseconds = int((peak % 1) * 1000)
        file.write(f"{minutes:02d}:{seconds:02d}:{milliseconds:03d}\n")

print("Peak times written to peak_times.txt")






print("Hello")
