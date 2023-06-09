# Audio extraction and transcription
## Getting Started
This guide assumes that you already have Python installed. If you do not have it installed you can follow this [link](https://www.python.org/downloads/?ref=news-tutorials-ai-research) to find the Python installation file for your operating system.
You can follow along using this (guide)[https://www.assemblyai.com/blog/how-to-run-openais-whisper-speech-recognition-model/] to get everything with Whisper setup.

1. Run ```python -m venv venv```
2. Run ```pip install -r requirements.txt``` This will install the dependencies we need for the U.I application and the Whisper which will be responsible for the audio transcription.
3. Run ```python gui.py```
4. Follow this part of the (guide)[https://www.assemblyai.com/blog/how-to-run-openais-whisper-speech-recognition-model/#:~:text=Step%201%3A%20Install,closed%20captioning.]
5. When installing Whisper make sure to select the CPU version if you do not have a powerful GPU on your machine.
6. Click anywhere in the window and select a video whose audio file is to be extracted.
7. When the audio extraction is done, you can find the audio file in the same directory as the video you selected.
8. Follow the steps under this to continue.

## I have the audio already, I want to get the transcription.
Well this is easy, assuming you got Whisper running you can just open up a terminal / command prompt window in the folder where the file is and run ```whisper audio.wav```

NOTE: This implementation of Whisper uses the CPU to do the processing, this can be slower and take some time.