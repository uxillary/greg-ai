# Gregg 🗣️🇬🇧  
**Scottish AI Voice Model — TTS Fine-tuning Project**

Welcome to **Gregg**, a voice cloning project using AI to train a custom Scottish accent voice (nicknamed “Greg”). This repository uses **Tacotron2** for spectrogram generation and **HiFi-GAN** for waveform synthesis to create high-quality, expressive speech from text.

---

## 🎯 Project Goals

- Train a natural-sounding voice model for “Greg” (Scottish accent)
- Use open-source tools for fine-tuning on a small custom dataset
- Experiment with phoneme settings, audio quality, and inference improvements

---

## 🛠️ Core Features

- ✅ **Tacotron2 + HiFi-GAN**: Neural TTS stack for clear speech synthesis  
- ✅ **LJSpeech-compatible Formatting**: Flexible with `metadata.csv`  
- ✅ **Custom Voice Training**: Easily fine-tune using your own recordings  
- ✅ **Configurable Output**: Adjust all model, training, and audio parameters via `config.json`  
- ✅ **Test Sentences**: Quickly generate inference output from predefined sentences  
- ✅ **Supports English Phonemizer**: For improved pronunciation control  

---

## 📦 Requirements

- Python 3.7+
- PyTorch with GPU support recommended
- FFmpeg installed and accessible in PATH

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Example `config.json` snippet:

```json
{
  "model": "Tacotron2",
  "generator_model": "HiFi-GAN",
  "audio_config": {
    "sample_rate": 22050,
    "fft_size": 1024,
    "hop_length": 256
  },
  "training_config": {
    "epochs": 100,
    "batch_size": 16,
    "learning_rate": 0.001
  },
  "datasets": [
    {
      "formatter": "ljspeech",
      "path": "dataset/",
      "meta_file_train": "metadata.csv",
      "language": "English",
      "phonemizer": "English"
    }
  ]
}
```

💡 **Important**: Make sure the `"language"` is explicitly set to `"English"` — the model will error out otherwise.

---

## 🧪 Usage

### 🔊 Generate Speech

```bash
python main.py
```

This will generate a sample file like:

```
output/test-output.wav
```

---

### 🧬 Train / Fine-Tune Model

```bash
python train_tts.py --config_path config.json --output_path output/
```

Training progress is saved to:

```
output/checkpoints/
output/logs/
```

You can resume training with:

```bash
python train_tts.py --config_path config.json --continue_path output/
```

---

## 📁 Project Structure

```
greg-ai/
├── config.json           # Main configuration
├── main.py               # Synthesis entry point
├── train_tts.py          # Training script
├── dataset/              # Custom audio and metadata
│   ├── metadata.csv
│   └── wavs/
├── output/               # Checkpoints, logs, generated audio
├── .venv/                # Python virtual environment
```

---

## 🗃️ Dataset Format

The dataset folder should follow this format:

```
dataset/
├── metadata.csv    # Format: filename|transcript
├── wavs/
│   ├── clip1.wav
│   ├── clip2.wav
```

- All audio files must be mono WAV format
- Use a sample rate of **22050 Hz**
- Match filenames exactly to `metadata.csv` entries

---

## 🐞 Troubleshooting

### ❌ `ValueError: The dataset language must be set to 'English'`

Ensure that `"language": "English"` is set in the config and dataset section. Also make sure the phonemizer is valid for English or left out if unused.

---

## 🙌 Credits

- 🗣️ [Tacotron2](https://arxiv.org/abs/1712.05884)  
- 🎵 [HiFi-GAN](https://arxiv.org/abs/2010.05646)  
- 🎤 [LJSpeech Dataset](https://keithito.com/LJ-Speech-Dataset/)  
- 🧠 [Coqui TTS](https://github.com/coqui-ai/TTS) — the library powering this repo

---

## 📄 License

MIT — free to use, modify, and share. See [LICENSE](./LICENSE) file for details.

---

## 💬 Contact

Built by **Adam** — [adam@ajstudios.dev](mailto:adam@ajstudios.dev)  
Project repo: [github.com/uxillary/greg-ai](https://github.com/uxillary/greg-ai)

---

## 🚧 Future Plans

- XTTS v2 support for multi-speaker synthesis  
- Dataset augmentation via phoneme control  
- Real-time inference UI using Streamlit or Gradio  
- Voice personality tuning and expression embedding
