import os
import librosa
import soundfile as sf
import numpy as np  # Add this to fix the error

def normalize_audio(input_dir, output_dir, target_db=-20.0):
    """Normalize all .wav files in a directory to a target dB."""
    os.makedirs(output_dir, exist_ok=True)
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".wav"):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name)

            # Load audio
            y, sr = librosa.load(input_path, sr=None)

            # Compute current dB level
            rms = librosa.feature.rms(y=y)
            current_db = 20 * librosa.core.amplitude_to_db(rms, ref=np.max)

            # Normalize
            gain = target_db - current_db.mean()
            y_normalized = y * (10 ** (gain / 20))

            # Save normalized audio
            sf.write(output_path, y_normalized, sr)
            print(f"Normalized: {file_name}")

# Normalize audio files in 'dataset/wavs' and save them back
normalize_audio("dataset/wavs", "dataset/wavs_normalized", target_db=-20.0)
