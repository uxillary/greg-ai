from TTS.api import TTS

# Paths
checkpoint_path = "output/checkpoints/checkpoint_epoch_5.pth"  # Path to your checkpoint
config_path = "config.json"  # Path to the model's configuration
output_path = "output/test-partial-output.wav"  # Path to save the generated audio

# Initialize TTS with the checkpoint and config
print("Loading model and synthesizer...")
tts = TTS(
    model_path=checkpoint_path,  # Checkpoint of the partially trained model
    config_path=config_path,
    progress_bar=True
)

# Input text for synthesis
text = "This is a test of the partially trained model."

# Generate audio
print("Generating audio...")
tts.tts_to_file(text=text, file_path=output_path)

print(f"Audio saved to: {output_path}")
