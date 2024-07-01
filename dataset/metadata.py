import os
import librosa
import numpy as np
import pandas as pd

waveform_types = {
    0: "triangular",
    1: "triangular +",
    2: "triangular + sawtooth",
    3: "triangular + sawtooth +",
    4: "triangular + sawtooth ++",
    5: "sawtooth",
    6: "sawtooth +",
    7: "sawtooth ++",
    8: "sawtooth + square",
    9: "sawtooth + square +",
    10: "sawtooth + square ++",
    11: "square",
    12: "square +",
    13: "square ++",
    14: "square + pulse",
    15: "square + pulse +",
    16: "square + pulse ++",
    17: "pulse",
    18: "pulse +"
}

def get_waveform_type(filename):
    try:
        waveform_number = int(filename.split('_')[0])
        return waveform_types.get(waveform_number, "Unknown")
    except (ValueError, IndexError):
        return "Unknown"

def estimate_note_frequency(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    fft_result = np.fft.fft(y)
    n = len(y)
    frequencies = np.fft.fftfreq(n, d=1/sr)
    positive_freq_indices = np.where(frequencies >= 0)
    frequencies = frequencies[positive_freq_indices]
    fft_result = fft_result[positive_freq_indices]
    magnitudes = np.abs(fft_result)

    if len(magnitudes) == 0:
        return None

    peak_index = np.argmax(magnitudes)
    fundamental_frequency = frequencies[peak_index]
    return fundamental_frequency

audio_directory = "/Users/sofiavallejo/Desktop/PeriodicUnit/dataset/audios"
output_csv = "/Users/sofiavallejo/Desktop/PeriodicUnit/dataset/metadata.csv"

results = []

for filename in os.listdir(audio_directory):
    if filename.endswith(".wav"):
        file_path = os.path.join(audio_directory, filename)
   
        waveform_type = get_waveform_type(filename)

        frequency = estimate_note_frequency(file_path)
        
        results.append([filename, waveform_type, frequency])

df = pd.DataFrame(results, columns=["File Name", "Waveform Type", "Frequency"])

df = df.sort_values(by="File Name")

df.to_csv(output_csv, index=False)

print(f"Analysis complete. Results saved to {output_csv}")
