 🎙️ Google Colab Microphone Recorder

This project demonstrates how to **record audio directly from your browser microphone in Google Colab**, save it as a `.wav` file, and play it back — all without requiring local hardware access or installing external packages.

 📌 Features

* Record audio from the browser microphone.
* Save the recording as a `.wav` file in Colab.
* Playback directly in the notebook.
* No external Python packages or installations required.

 🚀 Getting Started

1. Open the notebook in **Google Colab**.
2. Run all cells in sequence.
3. Grant microphone access when prompted.
4. Your audio will be recorded and saved as `recorded.wav`.

🧠 How It Works

* Uses **JavaScript** in the notebook to capture audio from the browser.
* Converts audio to **base64** and sends it to Python.
* Python decodes and saves it as a `.wav` file.
* An audio player is displayed to play the recording.

 📁 File Structure

Google_Colab_Microphone_Recorder/
│
├── record_audio_colab.ipynb     # Main notebook
└── recorded.wav                 # Saved audio file (created at runtime)

✅ Requirements

No installation needed — works directly in Google Colab.

If running outside Colab, you need:


pip install numpy scipy

📷 Demo

![demo\_gif](demo.gif) *(You can add a screen recording if available)*


Start a 5-second recording
record(5)

📌 Use Cases

* Audio recording for ML datasets
* Voice command prototyping
* Educational demos for speech/audio processing
* Simple voice memos in the cloud

 🛠️ Future Ideas

* Add waveform or spectrogram visualization
* Support for MP3 format
* Integrate with speech-to-text APIs

🤝 Contributing

Pull requests and feature ideas are welcome! Feel free to open an issue or fork the repo.

 📄 License

This project is open-source and available under the MIT License.

⚠️ Disclaimer & Usage
* This notebook is provided for educational and research purposes only.
* Commercial use, redistribution, or direct reproduction without permission is not allowed.
* Please cite the source or provide attribution if referencing this work in your own project.



https://github.com/user-attachments/assets/c87471d1-9421-400f-8b56-79a044985d1a  
Minor Update
Second Update
