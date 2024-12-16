import json
from TTS.api import TTS
from TTS.bin.train_tts import main as train_tts_main
import sys

# Load the configuration
with open("config.json", "r") as f:
    config = json.load(f)

# Initialize TTS with a pre-trained model for testing
print("Testing pre-trained model...")
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True)

# Generate test audio to verify setup
test_text = "Hello, this is a test of text-to-speech synthesis."
output_test_path = "output/test-output.wav"
tts.tts_to_file(text=test_text, file_path=output_test_path)
print(f"Test audio generated: {output_test_path}")

# Fine-tuning
print("Starting fine-tuning...")
sys.argv = [
    "train_tts",                    # Placeholder for script name
    "--config_path", "config.json", # Path to your config.json
    "--output_path", config["output_config"]["output_path"] # Output directory
]
train_tts_main()

print("Training Complete! Model and logs saved to:", config["output_config"]["output_path"])
