import os
import librosa
import soundfile as sf
import numpy as np

def normalize_audio(directory, output_directory, target_db=-20.0):
    """Normalize audio files to the target dB range."""
    os.makedirs(output_directory, exist_ok=True)
    for file_name in os.listdir(directory):
        if file_name.endswith(".wav"):
            file_path = os.path.join(directory, file_name)
            output_path = os.path.join(output_directory, file_name)
            
            y, sr = librosa.load(file_path, sr=None)
            rms = librosa.feature.rms(y=y)
            current_db = 20 * np.log10(np.mean(rms))
            
            # Calculate gain to normalize
            gain = target_db - current_db
            y_normalized = y * (10 ** (gain / 20))
            
            # Save the normalized audio
            sf.write(output_path, y_normalized, sr)
            print(f"Normalized: {file_name} to {target_db} dB")

# Normalize all files in "dataset/wavs" to -20 dB
normalize_audio("dataset/wavs", "dataset/wavs_normalized", target_db=-20.0)
