import os
import numpy as np
import librosa

def analyze_audio(directory, target_db=-20.0, tolerance=5.0, quiet_threshold=0.1):
    """Analyze audio files for amplitude and RMS (dB) range."""
    for file_name in os.listdir(directory):
        if file_name.endswith(".wav"):
            file_path = os.path.join(directory, file_name)
            y, sr = librosa.load(file_path, sr=None)
            
            # Check max amplitude
            max_amplitude = np.max(np.abs(y))
            if max_amplitude > 1.0:
                print(f"Too loud: {file_name} (max amplitude: {max_amplitude:.2f})")
            elif max_amplitude < quiet_threshold:
                print(f"Too quiet: {file_name} (max amplitude: {max_amplitude:.2f})")
            else:
                print(f"Within amplitude range: {file_name} (max amplitude: {max_amplitude:.2f})")
            
            # Calculate RMS and dB
            rms = librosa.feature.rms(y=y)
            current_db = 20 * np.log10(np.mean(rms))
            
            if not (target_db - tolerance <= current_db <= target_db + tolerance):
                print(f"Out of RMS range: {file_name} (dB: {current_db:.2f})")
            else:
                print(f"Within RMS range: {file_name} (dB: {current_db:.2f})")

# Analyze all audio files in the directory
analyze_audio("dataset/wavs", target_db=-20.0, tolerance=5.0, quiet_threshold=0.1)
