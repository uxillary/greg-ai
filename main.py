import json
from TTS.api import TTS
from TTS.bin.train_tts import main as train_tts_main
import os
import sys
import torch
import time

# Debug: Ensure the configuration file exists and is loaded properly
config_path = "config.json"

try:
    with open(config_path, "r") as f:
        config = json.load(f)
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

def save_checkpoint(model, epoch, checkpoint_dir="output/checkpoints/"):
    """Save model checkpoint"""
    os.makedirs(checkpoint_dir, exist_ok=True)
    checkpoint_path = os.path.join(checkpoint_dir, f"checkpoint_epoch_{epoch}.pth")
    torch.save(model.state_dict(), checkpoint_path)
    print(f"Checkpoint saved at: {checkpoint_path}")

# Add pausing logic to the training loop
def train_with_pause():
    pause_file = "pause.txt"  # File to trigger pause
    auto_pause_interval = 5  # Number of epochs before an automatic pause

    try:
        for epoch in range(1, 1001):  # Replace with actual epoch range/config
            print(f"Starting epoch {epoch}/1000")
            
            # Simulate training logic (replace with actual training function calls)
            time.sleep(1)  # Simulate time for one epoch
            
            # Save checkpoint after every epoch
            save_checkpoint(tts, epoch)

            # Check for manual pause via pause.txt
            if os.path.exists(pause_file):
                print("Pause file detected. Pausing training...")
                break

            # Auto-pause every 'auto_pause_interval' epochs
            if epoch % auto_pause_interval == 0:
                print(f"Auto-pause after {epoch} epochs.")
                break

    except KeyboardInterrupt:
        print("Training interrupted. Saving current checkpoint...")
        save_checkpoint(tts, epoch)
        print("Checkpoint saved. Exiting...")
        sys.exit(0)

# Call the training function with pause logic
train_with_pause()

print("Training Complete! Model and logs saved to:", "output/")
