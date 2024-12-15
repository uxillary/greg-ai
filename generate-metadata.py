import os
import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Paths
dataset_path = "dataset/wavs"
metadata_path = "dataset/metadata-export.csv"

# Create metadata.csv
with open(metadata_path, "w") as f:
    for filename in os.listdir(dataset_path):
        if filename.endswith(".wav"):
            filepath = os.path.join(dataset_path, filename)
            print(f"Transcribing {filename}...")
            result = model.transcribe(filepath)
            text = result["text"].strip()
            f.write(f"{filename}|{text}\n")
