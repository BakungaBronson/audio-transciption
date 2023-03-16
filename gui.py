import tkinter as tk
from tkinter import filedialog
import moviepy.editor as mp

# Define the function to extract the audio from the video file
def extract_audio(video_file):
    # Load the video file using MoviePy
    video_clip = mp.VideoFileClip(video_file)

    # Extract the audio from the video clip
    audio_clip = video_clip.audio

    # Set the output file name and path
    output_file = video_file.split(".")[0] + ".mp3"

    # Save the audio clip as an MP3 file
    audio_clip.write_audiofile(output_file)

    # Close the clips
    audio_clip.close()
    video_clip.close()

    # Print a message to indicate the extraction is complete
    print("Audio extraction complete.")

# Define the function to handle the form submission
def submit_form():
    # Open a file dialog to choose the video file
    video_file = filedialog.askopenfilename(initialdir="/", title="Select Video File", filetypes=(("Video Files", "*.mp4;*.avi;*.mov"), ("All Files", "*.*")))

    # Extract the audio from the video file
    extract_audio(video_file)

# Create the Tkinter window
window = tk.Tk()
window.title("Video Audio Extractor")

# Create the form elements
tk.Label(window, text="Video File Path").grid(row=0, column=0)
video_path_entry = tk.Entry(window)
video_path_entry.grid(row=0, column=1)
submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.grid(row=1, column=0, columnspan=2)

# Run the window loop
window.mainloop()
