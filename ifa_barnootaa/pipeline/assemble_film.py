
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "outputs"
ASSETS = ROOT / "assets"

master = OUTPUT / "film_master_no_subtitles.mp4"
audio = ASSETS / "audio" / "final_audio_mix.wav"
subtitles = ASSETS / "subtitles" / "english_subtitles.srt"

vertical = OUTPUT / "ifa_barnootaa_vertical_9x16.mp4"
horizontal = OUTPUT / "ifa_barnootaa_horizontal_16x9.mp4"
radio = OUTPUT / "ifa_barnootaa_radio_cut.mp4"

for file in [master, audio, subtitles]:
    if not file.exists():
        raise FileNotFoundError(f"Missing input: {file}")

def run(command):
    subprocess.run(command, check=True)

vertical_style = (
    "FontName=DejaVu Sans,FontSize=22,"
    "PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
    "BorderStyle=1,Outline=2,Shadow=1,Alignment=2,MarginV=55"
)

horizontal_style = (
    "FontName=DejaVu Sans,FontSize=24,"
    "PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
    "BorderStyle=1,Outline=2,Shadow=1,Alignment=2,MarginV=35"
)

run([
    "ffmpeg", "-y", "-i", str(master), "-i", str(audio),
    "-vf", f"subtitles='{subtitles}':force_style='{vertical_style}'",
    "-af", "apad=pad_dur=3",
    "-c:v", "libx264", "-preset", "ultrafast", "-crf", "23",
    "-c:a", "aac", "-b:a", "192k",
    "-pix_fmt", "yuv420p", "-shortest", str(vertical)
])

filter_graph = (
    "[0:v]split=2[bg][fg];"
    "[bg]scale=1280:720:force_original_aspect_ratio=increase,"
    "crop=1280:720,boxblur=20:10[background];"
    "[fg]scale=-2:720[foreground];"
    "[background][foreground]overlay=(W-w)/2:(H-h)/2,"
    f"subtitles='{subtitles}':force_style='{horizontal_style}'[vout]"
)

run([
    "ffmpeg", "-y", "-i", str(master), "-i", str(audio),
    "-filter_complex", filter_graph,
    "-map", "[vout]", "-map", "1:a",
    "-af", "apad=pad_dur=3",
    "-c:v", "libx264", "-preset", "ultrafast", "-crf", "23",
    "-c:a", "aac", "-b:a", "192k",
    "-pix_fmt", "yuv420p", "-shortest", str(horizontal)
])

run([
    "ffmpeg", "-y",
    "-f", "lavfi", "-i", "color=c=black:s=720x1280:r=24:d=70",
    "-i", str(audio),
    "-c:v", "libx264", "-preset", "ultrafast",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    "-shortest", str(radio)
])

print("FILM EXPORTS COMPLETED")
for file in [vertical, horizontal, radio]:
    print(file.name, round(file.stat().st_size / (1024*1024), 2), "MB")
