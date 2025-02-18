# Define a list of models to test (English only)
$models = @(
    "tts_models/en/ek1/tacotron2"
    "tts_models/en/ljspeech/tacotron2-DDC"
    "tts_models/en/ljspeech/tacotron2-DDC_ph"
    "tts_models/en/ljspeech/glow-tts"
    "tts_models/en/ljspeech/speedy-speech"
    "tts_models/en/ljspeech/tacotron2-DCA"
    "tts_models/en/ljspeech/vits"
    "tts_models/en/ljspeech/vits--neon"
    "tts_models/en/ljspeech/fast_pitch"
    "tts_models/en/ljspeech/overflow"
    "tts_models/en/ljspeech/neural_hmm"
    "tts_models/en/vctk/vits"
    "tts_models/en/vctk/fast_pitch"
    "tts_models/en/sam/tacotron-DDC"
    "tts_models/en/blizzard2013/capacitron-t2-c50"
    "tts_models/en/blizzard2013/capacitron-t2-c150_v2"
    "tts_models/en/multi-dataset/tortoise-v2"
    "tts_models/en/jenny/jenny"
)

# Define a sample sentence
$text = "Hello, this is a test of the Mozilla TTS model. Which one sounds most like me?"

# Loop through each model, generate speech, and play it
foreach ($model in $models) {
    Write-Host "Generating with model: $model"

    # Run the TTS command
    Start-Process -NoNewWindow -Wait -FilePath "tts" -ArgumentList "--text `"$text`" --model_name `"$model`" --out_path output.wav"

    # Play the output audio
    Start-Process -NoNewWindow -Wait -FilePath "ffplay" -ArgumentList "-nodisp -autoexit output.wav"

    # Wait for user input before moving to the next model
    Read-Host "Press Enter to continue to the next model"
}
