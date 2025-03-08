import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load original audio
y, sr = librosa.load("example_audio.wav", sr=None)

# Resample to 8 kHz
y_resampled_8k = librosa.resample(y, orig_sr=sr, target_sr=8000)

# Plot spectrograms before and after resampling
def plot_spectrogram(y, sr, title):
    plt.figure(figsize=(10, 6))
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    librosa.display.specshow(D, sr=sr, x_axis="time", y_axis="log")
    plt.colorbar(format="%+2.0f dB")
    plt.title(title)
    plt.show()

plot_spectrogram(y, sr, "Original Spectrogram")
plot_spectrogram(y_resampled_8k, 8000, "Resampled Spectrogram (8 kHz)")
