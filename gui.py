import tkinter as tk
from tkinter import filedialog
import os
import moviepy.editor as mp
from tkinter import ttk
import whisper
import json

def submit_form():
    # Define the allowed file types
    filetypes = [("Video files", "*.mp4;*.avi;*.flv;*.wmv;*.mov")]
    
    # Get the video file path from the user
    file_path = filedialog.askopenfilename(title="Select Video File", filetypes=filetypes)
    
    if file_path:
        if os.path.isfile(audio_path):
            status_label.configure(text="Audio file already exists!")
        # Show the loading animation
        status_label.configure(text="Extracting audio...")
        progress_bar.start(10)

        # Extract the audio from the video file
        video = mp.VideoFileClip(file_path)
        audio = video.audio
        audio_path = os.path.splitext(file_path)[0] + ".mp3"
        sub_audio = audio.subclip(0, video.duration)
        sub_audio.write_audiofile(audio_path)

        # Display a success message to the user
        status_label.configure(text="Audio extracted successfully!")
        progress_bar.stop()
        progress_bar["value"] = 0
        
        status_label.configure(text="Getting audio transcription...!")
        
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        
        # Save the transcription to a text file with the same name as the audio file
        transcription_file = os.path.splitext(audio_path)[0] + ".txt"
        with open(transcription_file, "w") as f:
            f.write(result["text"])

        status_label.configure(text="Transcription saved to {transcription_file}!")



def update_progress_bar(progress, duration):
    # Update the progress bar
    progress_bar["value"] = progress
    progress_bar.update_idletasks()

# Create the Tkinter window
window = tk.Tk()
window.title("Video Audio Extractor")
window.geometry("400x450")

# Create a canvas with a blue and purple gradient background
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Create a rounded white button
submit_button = tk.Button(window, text="Submit", command=submit_form, bg="white", fg="black", bd=0, relief="flat", font=("Arial", 14), padx=20, pady=10, borderwidth=0)
submit_button.place(relx=0.5, rely=0.5, anchor="center")
submit_button.configure(width=12, height=1)
submit_button.update_idletasks()
rounded_size = min(submit_button.winfo_width(), submit_button.winfo_height())
submit_button.configure(width=rounded_size, height=rounded_size, bd=0, relief="flat")
submit_button.place(relx=0.5, rely=0.6, anchor="center")

# Create a progress bar to display the status of the audio extraction
progress_bar = tk.ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
progress_bar.place(relx=0.5, rely=0.7, anchor="center")

# Create a label to display the status message
status_label = tk.Label(window, text="")
status_label.place(relx=0.5, rely=0.85, anchor="center")

# Start the Tkinter event loop
window.mainloop()
