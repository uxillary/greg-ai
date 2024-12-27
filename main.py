import json
from TTS.bin.train_tts import main as train_tts_main
import os
import sys
import glob
import torch

config_path = "config.json"

try:
    with open(config_path, "r") as f:
        config = json.load(f)
        print("Loaded config:", config)
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

# Training with pause and checkpoint logic
def train_with_pause():
    pause_file = "pause.txt"
    auto_pause_interval = 50  # Pause every 50 epochs

    # Initialize model and optimizer
    print("Starting training...")
    model, optimizer = train_tts_main()  # Ensure this returns model and optimizer

    try:
        for epoch in range(1, 101):
            print(f"Starting epoch {epoch}/100")

            # Training logic is handled in train_tts_main
            if epoch % 10 == 0:
                save_checkpoint(model, optimizer, epoch)

            clean_old_checkpoints("output/checkpoints/", keep_last=5)

            if os.path.exists(pause_file):
                print("Pause file detected. Pausing training...")
                break

            if epoch % auto_pause_interval == 0:
                print(f"Auto-pause after {epoch} epochs.")
                break

    except KeyboardInterrupt:
        print("Training interrupted. Saving current checkpoint...")
        save_checkpoint(model, optimizer, epoch)
        sys.exit(0)

# Run training
train_with_pause()
print("Training Complete! Model and logs saved to:", "output/")
