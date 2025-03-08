import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import librosa
import librosa.display

# Load an audio file
audio, sr = librosa.load("example_audio.wav")

# Function to apply quantization
def quantize_signal(signal, num_bits):
    num_levels = 2 ** num_bits  # Quantization levels
    quantized_signal = np.round(signal * (num_levels / 2)) / (num_levels / 2)
    return quantized_signal

# Apply quantization (Example: 4-bit)
num_bits = 8
quantized_audio = quantize_signal(audio, num_bits)

# Save quantized audio
sf.write("quantized_example.wav", quantized_audio, sr)

# Plot Spectrograms Side by Side
plt.figure(figsize=(12, 6))

# Original Audio Spectrogram
plt.subplot(2, 1, 1)
plt.specgram(audio, Fs=sr, NFFT=1024, cmap="magma")
plt.title("Original Audio Spectrogram")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.colorbar(label="Amplitude (dB)")

# Quantized Audio Spectrogram
plt.subplot(2, 1, 2)
plt.specgram(quantized_audio, Fs=sr, NFFT=1024, cmap="magma")
plt.title(f"Quantized Audio Spectrogram ({num_bits}-bit)")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.colorbar(label="Amplitude (dB)")

plt.tight_layout()
plt.show()
