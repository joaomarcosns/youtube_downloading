from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
import re
import os


links = [
    "https://youtu.be/D_ouc1v2SoQ",
    "https://youtu.be/SocNHBVC1KI",
    "https://youtu.be/edjih_b_NBQ",
    "https://youtu.be/FtHBS6WLsfo",
    "https://youtu.be/lf-KK2iWVkE",
    "https://youtu.be/OnSnZ7CGPz0",
    "https://youtu.be/ePjtnSPFWK8",
    "https://youtu.be/FQgZAj45ojY",
    "https://youtu.be/-UUe7g8-E0k",
    "https://youtu.be/JNzI4R7qZvc",
    "https://youtu.be/JvaU1ZKDDX0",
    "https://youtu.be/bHT5GvYi6io",
    "https://youtu.be/GnoTgMEckDs",
    "https://youtu.be/QxZFjShiXhA",
]
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audios')

for link in links:
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution().download(output_path=path)
    for file in os.listdir(path):
        if re.search("mp4", file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0] + ".mp3")
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
            print(f"Conversion completed for {file}")

print("All conversions completed.")
