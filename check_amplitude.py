import os
import librosa
import numpy as np

def analyze_audio_amplitude(directory, target_db=-20.0, tolerance=5.0):
    """Analyze audio files for amplitude range."""
    for file_name in os.listdir(directory):
        if file_name.endswith(".wav"):
            file_path = os.path.join(directory, file_name)
            y, sr = librosa.load(file_path, sr=None)
            
            rms = librosa.feature.rms(y=y)
            current_db = 20 * np.log10(np.mean(rms))
            
            if not (target_db - tolerance <= current_db <= target_db + tolerance):
                print(f"Out of range: {file_name} (dB: {current_db:.2f})")
            else:
                print(f"Within range: {file_name} (dB: {current_db:.2f})")

# Analyze all audio files in the dataset
analyze_audio_amplitude("dataset/wavs", target_db=-20.0, tolerance=5.0)
