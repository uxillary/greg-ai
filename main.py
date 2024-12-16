import json
from TTS.api import TTS

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

# Fine-tune the model if pre-trained model test is successful
print("Starting fine-tuning...")
tts.finetune(
    dataset_path=config["dataset_config"]["path"],
    output_path=config["output_config"]["output_path"],
    config_path="config.json"
)

print("Training Complete! Model and logs saved to:", config["output_config"]["output_path"])
