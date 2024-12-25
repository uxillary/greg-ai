import os
from TTS.utils.synthesizer import Synthesizer

# Paths
checkpoint_path = "output/checkpoints/checkpoint_epoch_5.pth"  # Update this to the checkpoint you want to test
config_path = "config.json"  # Your model's config file
output_path = "output/test-partial-output.wav"  # Path to save the generated audio

# Initialize synthesizer
print("Loading synthesizer...")
synthesizer = Synthesizer(
    checkpoint_path=checkpoint_path,
    config_path=config_path,
    use_cuda=True  # Set to False if you don’t have a GPU
)

# Input text for synthesis
text = "This is a test of the partially trained model."

# Generate audio
print("Generating audio...")
wav = synthesizer.tts(text)

# Save audio file
synthesizer.save_wav(wav, output_path)
print(f"Audio saved to: {output_path}")
