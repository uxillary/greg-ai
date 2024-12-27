# Gregg
Ai voice model training for "Greg" Scottish AI

# Text-to-Speech Training and Synthesis

![Project Banner](https://via.placeholder.com/800x200?text=Text-to-Speech+Training+and+Synthesis)

A Python-based text-to-speech (TTS) synthesis and training project using **Tacotron2** and **HiFi-GAN**. This repository enables you to fine-tune models and generate high-quality speech audio.

## Features

- **Model Support:** Pre-trained Tacotron2 and HiFi-GAN models.
- **Dataset Compatibility:** Works with datasets like LJSpeech.
- **Customizable Configurations:** Easily modify training and audio settings via `config.json`.
- **Fine-Tuning:** Fine-tune TTS models with your dataset.
- **Audio Generation:** Generate speech from text with pre-trained or fine-tuned models.

---

## Getting Started

### Prerequisites

- Python 3.7+
- `pip` for package management

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Adjust settings in `config.json`:

```json
{
  "model": "Tacotron2",
  "generator_model": "HiFi-GAN",
  "audio_config": {
    "sample_rate": 22050,
    "fft_size": 1024,
    "win_length": 1024,
    "hop_length": 256
  },
  "training_config": {
    "epochs": 100,
    "batch_size": 16,
    "learning_rate": 0.001
  }
}
```

---

## Usage

### 1. Load Configuration

Ensure `config.json` is properly set up. The script will validate and load this file.

### 2. Generate Speech

Run the `main.py` script to synthesize audio from text:

```bash
python main.py
```

This generates a test output at `output/test-output.wav`.

### 3. Train or Fine-Tune a Model

Use `train_tts.py` to train or fine-tune a TTS model with your dataset:

```bash
python train_tts.py --config_path config.json
```

---

## Directory Structure

```
project-root/
├── config.json         # Configuration file
├── main.py             # Main script for synthesis
├── train_tts.py        # Fine-tuning script
├── dataset/            # Dataset folder
├── output/             # Outputs: checkpoints, logs, and generated audio
```

---

## Dataset Preparation

Ensure your dataset is in the following structure:

```
/dataset/
├── metadata.csv  # Text-audio mappings
├── wavs/         # Audio files
```

Modify `config.json` to point to your dataset directory.

---

## Acknowledgements

- **[LJSpeech Dataset](https://keithito.com/LJ-Speech-Dataset/)**
- **[Tacotron2](https://arxiv.org/abs/1712.05884)**
- **[HiFi-GAN](https://arxiv.org/abs/2010.05646)**

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Contributing

Contributions are welcome! Submit a pull request or report issues in the [issue tracker](https://github.com/uxillary/greg-ai/issues).

---

## Contact

For questions or support, contact [Adam](mailto:mail@ajstudios.online).
