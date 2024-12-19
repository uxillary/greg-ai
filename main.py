import json
from TTS.api import TTS
from TTS.bin.train_tts import main as train_tts_main
import sys

# Debug: Ensure the configuration file exists and is loaded properly
config_path = "config.json"

try:
    with open(config_path, "r") as f:
        config = json.load(f)
    print("Config file loaded successfully:")
    print(json.dumps(config, indent=4))  # Pretty-print the loaded config
except Exception as e:
    print("Error loading config file:", e)
    sys.exit(1)

# Initialize TTS with a pre-trained model for testing
print("Testing pre-trained model...")
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True)

# Generate test audio to verify setup
test_text = "Hello, this is a test of text-to-speech synthesis."
output_test_path = "output/test-output.wav"
try:
    tts.tts_to_file(text=test_text, file_path=output_test_path)
    print(f"Test audio generated: {output_test_path}")
except Exception as e:
    print("Error generating test audio:", e)

# Fine-tuning
print("Starting fine-tuning...")
sys.argv = [
    "train_tts",  # Placeholder for script name
    "--config_path", config_path,
    "--output_path", "output/"
]

# Call the training function
try:
    train_tts_main()
except Exception as e:
    print("Fine-tuning failed:", e)

print("Training Complete! Model and logs saved to:", "output/")
