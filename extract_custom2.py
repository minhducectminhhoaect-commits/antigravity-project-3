import subprocess

for s in range(157, 165):
    cmd = [
        "ffmpeg", "-y", "-ss", str(s), "-i", "video.mp4",
        "-vframes", "1", "-q:v", "2", f"screenshots/custom_machine_{s}s.png"
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("Frames 157-164 extracted.")
