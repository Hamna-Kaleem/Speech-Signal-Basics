# Waveforms in Speech Signals

A waveform is a graphical representation of a speech signal in the time domain. It shows the variation in signal amplitude over time. In speech processing, understanding the time-domain representation of a signal is essential for tasks like speech recognition.

## Visualizing Speech Waveforms

We can visualize waveforms using Python libraries such as `librosa` and `matplotlib`. Below is an example of loading and visualizing a speech signal:
```python
import librosa
import matplotlib.pyplot as plt

y, sr = librosa.load("data/example_audio.wav")
plt.figure(figsize=(10, 6))
librosa.display.waveshow(y, sr=sr)
plt.title("Speech Waveform")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

