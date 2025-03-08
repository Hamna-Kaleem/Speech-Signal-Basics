
##### **sampling.md**
```markdown
# Sampling in Speech Signals

Sampling is the process of converting a continuous signal into a discrete one by measuring the signal's amplitude at regular intervals. The rate at which samples are taken is called the **sampling rate**.

## Nyquist Theorem

According to the Nyquist Theorem, to avoid aliasing, the sampling rate should be at least twice the highest frequency of the signal. For speech signals, the typical sampling rate is 16 kHz or 44.1 kHz.

## Sampling Example

We can visualize the effect of different sampling rates on a speech signal:
```python
import librosa.display

# Load and resample signal
y_resampled_8k = librosa.resample(y, sr, 8000)  # Resampling to 8kHz

plt.figure(figsize=(10, 6))
librosa.display.waveshow(y_resampled_8k, sr=8000)
plt.title("Resampled Speech Signal at 8 kHz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
