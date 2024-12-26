import json
from TTS.bin.train_tts import main as train_tts_main
import os
import sys
import time
import glob
import torch

# Debug: Ensure the configuration file exists and is loaded properly
config_path = "config.json"

try:
    with open(config_path, "r") as f:
        config = json.load(f)
except Exception as e:
    print("Error loading config file:", e)
    sys.exit(1)

# Add checkpoint saving logic
def save_checkpoint(model, optimizer, epoch, checkpoint_dir="output/checkpoints/"):
    """Save a checkpoint with the current epoch."""
    os.makedirs(checkpoint_dir, exist_ok=True)
    checkpoint_path = os.path.join(checkpoint_dir, f"checkpoint_epoch_{epoch}.pth")
    torch.save({
        "epoch": epoch,
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
    }, checkpoint_path)
    print(f"Checkpoint saved at: {checkpoint_path}")

# Keep only the latest checkpoints
def clean_old_checkpoints(checkpoint_dir, keep_last=5):
    """Keep only the latest `keep_last` checkpoints."""
    checkpoints = sorted(glob.glob(f"{checkpoint_dir}/checkpoint_epoch_*.pth"), key=os.path.getmtime)
    if len(checkpoints) > keep_last:
        for old_checkpoint in checkpoints[:-keep_last]:
            os.remove(old_checkpoint)
            print(f"Removed old checkpoint: {old_checkpoint}")

# Add pausing logic to the training loop
def train_with_pause():
    """Run training with pause and checkpoint features."""
    pause_file = "pause.txt"  # File to trigger pause
    auto_pause_interval = 5  # Number of epochs before an automatic pause

    # Example model and optimizer (replace with actual instances)
    model = torch.nn.Linear(10, 1)  # Replace with your actual model
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)  # Replace with your optimizer

    try:
        for epoch in range(1, 1001):  # Replace with actual epoch range/config
            print(f"Starting epoch {epoch}/1000")

            # Call the actual training function
            sys.argv = [
                "train_tts",
                "--config_path", config_path,
                "--output_path", "output/",
            ]
            train_tts_main()

            # Save checkpoint every 10 epochs
            if epoch % 10 == 0:
                save_checkpoint(model, optimizer, epoch)

            # Clean up old checkpoints
            clean_old_checkpoints("output/checkpoints/", keep_last=5)

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
        save_checkpoint(model, optimizer, epoch)
        print("Checkpoint saved. Exiting...")
        sys.exit(0)

# Run training with pausing logic
train_with_pause()

print("Training Complete! Model and logs saved to:", "output/")
