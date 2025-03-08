
##### **quantization.md**
```markdown
# Quantization in Speech Signals

Quantization is the process of mapping the continuous amplitude of a signal into discrete values. It involves rounding the amplitude values to a certain number of levels based on bit-depth. 

## Effect of Quantization

The bit-depth determines how fine-grained the quantization is. A lower bit-depth leads to higher quantization noise, while a higher bit-depth preserves more details of the signal.

## Quantization Example

You can simulate quantization effects by changing the bit-depth of a signal:
```python
import numpy as np

def quantize(signal, bit_depth):
    max_value = np.max(np.abs(signal))
    levels = 2 ** bit_depth
    step_size = max_value / (levels // 2)
    quantized_signal = np.round(signal / step_size) * step_size
    return quantized_signal

quantized_signal = quantize(y, 8)  # 8-bit quantization

plt.figure(figsize=(10, 6))
librosa.display.waveshow(quantized_signal, sr=sr)
plt.title("Quantized Speech Signal (8-bit)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
