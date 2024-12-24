import os
from TTS.utils.synthesizer import Synthesizer

# Set paths output/
checkpoint_path = "output/run-December-24-2024_02+48AM-c19f59f/best_model.pth"  # Update to your checkpoint path
config_path = "config.json"  # Path to your model's configuration
output_path = "preview_output.wav"  # Path to save the generated audio

# Initialize the synthesizer
synthesizer = Synthesizer(
    checkpoint_path=checkpoint_path,
    config_path=config_path,
    use_cuda=True  # Set to False if you don’t have a GPU
)

# Input text for synthesis
text = "This is a test of my custom voice model."

# Generate audio
wav = synthesizer.tts(text)

# Save the audio
synthesizer.save_wav(wav, output_path)
print(f"Preview generated and saved to: {output_path}")
