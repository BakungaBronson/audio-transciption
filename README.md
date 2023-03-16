# Audio extraction and transcription
## Getting Started
This guide assumes that you already have Python installed. If you do not have it installed you can follow this [link](https://www.python.org/downloads/?ref=news-tutorials-ai-research) to find the Python installation file for your operating system.
You can follow along using this (guide)[https://www.assemblyai.com/blog/how-to-run-openais-whisper-speech-recognition-model/] to get everything with Whisper setup.

1. Run ```python -m venv venv```
2. Run ```bash pip install -r requirements.txt``` This will install the dependencies we need for the U.I application and the Whisper which will be responsible for the audio transcription.
3. Run ```python python gui.py```
4. Click anywhere in the window and select a video whose audio file is to be extracted.
5. When the audio extraction is done, you can find the audio file in the same directory as the video you selected.
