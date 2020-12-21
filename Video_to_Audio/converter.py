import moviepy.editor
from tkinter.filedialog import *

# Ask user for the video file
video = askopenfilename()

# apply the editor method on the video variable
video = moviepy.editor.VideoFileClip(video)

# since editing method is initialized on video, we will extract the audio
audio = video.audio

# save the extracted audio
audio.write_audiofile("sample.mp3")

print("Video Conversion Completed!")
