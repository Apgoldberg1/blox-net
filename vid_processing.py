import os
import subprocess

# Input and output directories
input_folder = 'data/high_res'
output_folder = 'data/playback'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)
        
        # Run the ffmpeg command to resize the video
        subprocess.run([
            'ffmpeg', 
            '-i', input_file,   # Input file
            '-vf', 'scale=960:540',   # Set resolution to 960x540
            '-c:a', 'copy',     # Copy the audio as is
            output_file         # Output file
        ])
