import json
from TTS.bin.train_tts import main as train_tts_main
import os
import sys
import glob
import torch

import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', type=str, default='config.json',
                        help='Path to the main config file.')
    # Add a dataset_config argument:
    parser.add_argument('--dataset_config', type=str, default=None,
                        help='Path to the dataset config file.')
    return parser.parse_args()


config_path = "aj_config.json"

# Load config
try:
    with open(config_path, "r") as f:
        config = json.load(f)
        # print("Loaded config:", config)
except Exception as e:
    print("Error loading config file:", e)
    sys.exit(1)

# Save checkpoint function
def save_checkpoint(model, optimizer, epoch, checkpoint_dir="output/checkpoints/"):
    os.makedirs(checkpoint_dir, exist_ok=True)
    checkpoint_path = os.path.join(checkpoint_dir, f"checkpoint_epoch_{epoch}.pth")
    torch.save({
        "epoch": epoch,
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
    }, checkpoint_path)
    print(f"Checkpoint saved at: {checkpoint_path}")

# Clean old checkpoints
def clean_old_checkpoints(checkpoint_dir, keep_last=5):
    checkpoints = sorted(glob.glob(f"{checkpoint_dir}/checkpoint_epoch_*.pth"), key=os.path.getmtime)
    if len(checkpoints) > keep_last:
        for old_checkpoint in checkpoints[:-keep_last]:
            os.remove(old_checkpoint)
            print(f"Removed old checkpoint: {old_checkpoint}")

# Training logic
def train():
    """Run training with checkpoint saving."""
    print("Starting training...")

    # Set up command-line arguments for train_tts_main
    sys.argv = [
        "train_tts",
        "--config_path", config_path,
        "--output_path", "output/"
    ]
    
    print("sys.argv = ", sys.argv)

    # Call train_tts_main (it will handle training using the provided config)
    train_tts_main()

    # Example checkpointing logic, ensure model/optimizer are properly integrated in train_tts_main
    try:
        for epoch in range(1, 101):  # Replace 101 with your desired epoch count
            print(f"Starting epoch {epoch}/100")

            # Save checkpoint every 10 epochs (Placeholder)
            # Replace with actual model and optimizer saving if exposed by train_tts_main
            if epoch % 10 == 0:
                # Uncomment and adjust these lines if train_tts_main exposes model/optimizer
                # save_checkpoint(model, optimizer, epoch)
                pass

            # Clean up old checkpoints
            clean_old_checkpoints("output/checkpoints/", keep_last=5)

    except KeyboardInterrupt:
        print("Training interrupted.")
        # Uncomment if train_tts_main exposes model/optimizer
        # save_checkpoint(model, optimizer, epoch)
        sys.exit(0)

# Run training
train()
print("Training Complete! Model and logs saved to:", "output/")
