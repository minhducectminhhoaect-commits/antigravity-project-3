import subprocess
import os

for s in [153, 154, 155, 156, 157, 158, 159]:
    cmd = [
        "ffmpeg", "-y", "-ss", str(s), "-i", "video.mp4",
        "-vframes", "1", "-q:v", "2", f"screenshots/custom_machine_{s}s.png"
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("Custom machine frames extracted.")
