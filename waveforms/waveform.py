import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load audio file (keep original sample rate)
y, sr = librosa.load("./example_audio.wav", sr=None)

# Print sample rate
print(f"Sample Rate: {sr} Hz")

# Plot waveform
plt.figure(figsize=(10, 6))
librosa.display.waveshow(y, sr=sr)  # Use librosa.display.waveshow
plt.title("Speech Waveform")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
