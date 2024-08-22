# Speech Recognition App

This is a simple speech recognition application built with Streamlit and the Whisper model from Hugging Face. It allows users to record their voice and transcribe it to text.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 3.7 or later.
* You have a working microphone connected to your device.

## Installation

To install the Speech Recognition App, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/speech-recognition-app.git
   cd speech-recognition-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Speech Recognition App, follow these steps:

1. Ensure you're in the project directory and your virtual environment is activated (if you're using one).

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Your default web browser should open automatically with the app running. If it doesn't, you can open a browser and go to the URL shown in the terminal (usually http://localhost:8501).

4. Click the "🎤 Record" button to start recording your voice. The app will record for 5 seconds.

5. After recording, the app will process your audio and display the transcribed text.

## Usage Notes

- The app uses the "tiny" version of the Whisper model, which is optimized for English language transcription.
- Each recording session is limited to 5 seconds.
- Make sure your microphone is properly connected and configured on your device.
- The app may take a moment to load initially as it downloads the necessary model files.

## Troubleshooting

If you encounter any issues:

- Ensure all dependencies are correctly installed.
- Check that your microphone is properly connected and has necessary permissions.
- If you're having trouble with PyTorch, make sure you've installed the correct version for your system.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.