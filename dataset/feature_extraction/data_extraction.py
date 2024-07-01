import librosa
import numpy as np
import os
import csv
from tqdm import tqdm

def detect_pitch(y, sr):
    pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr, fmin=75, fmax=16000)
    max_indexes = np.argmax(magnitudes, axis=0)
    pitches = pitches[max_indexes, range(magnitudes.shape[1])]
    pitch = np.mean(pitches)
    return pitch

def estimate_loudness_rms(audio_file):
    y, sr = librosa.load(audio_file)
    rms = librosa.feature.rms(y=y)
    if rms.size == 0:
        return 0
    loudness_rms = np.mean(rms)
    return loudness_rms

def calculate_angular_frequency(frequency):
    if frequency is None:
        return None
    angular_frequency = 2 * np.pi * frequency
    return angular_frequency

def process_audio_files(folder_path):
    data = []
    audio_files = [f for f in os.listdir(folder_path) if f.endswith(".wav")]
    
    for file_name in tqdm(audio_files, desc="Processing audio files"):
        file_parts = file_name.split('_')
        if len(file_parts) != 2:
            print(f"Skipping file with unexpected name format: {file_name}")
            continue
        
        try:
            waveform = int(file_parts[0])
            second_number = int(file_parts[1].replace(".wav", ""))
        except ValueError:
            print(f"Skipping file with non-integer values in the name: {file_name}")
            continue
        
        file_path = os.path.join(folder_path, file_name)
        
        y, sr = librosa.load(file_path)
        frequency = detect_pitch(y, sr)
        loudness = estimate_loudness_rms(file_path)
        angular_frequency = calculate_angular_frequency(frequency)
        cv_frequency = (second_number - 13) * 0.33
        cv_waveform = waveform * 0.50
        
        data.append({
            'filename': file_name,
            'waveform': waveform,
            'frequency': frequency,
            'loudness': loudness,
            'angular_frequency': angular_frequency,
            'cv_frequency': cv_frequency,
            'cv_waveform': cv_waveform,
            'waveform_data': ','.join(map(str, y.tolist())) 
        })
    
    if data:
        keys = data[0].keys()
        with open('/dataset/new_analysis.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys, quoting=csv.QUOTE_MINIMAL)
            dict_writer.writeheader()
            dict_writer.writerows(data)
    else:
        print("No valid audio files found or processed.")

folder_path = "/dataset/audios"
process_audio_files(folder_path)
