import json
from TTS.api import TTS

# Load the configuration
with open("config.json", "r") as f:
    config = json.load(f)

# Initialize TTS
tts = TTS(model_name=config["training_config"]["model"], progress_bar=True)

# Train the model
tts.finetune(
    dataset_path=config["dataset_config"]["path"],
    output_path=config["output_config"]["output_path"],
    config_path="config.json"
)

print("Training Complete! Model and logs saved to:", config["output_config"]["output_path"])
