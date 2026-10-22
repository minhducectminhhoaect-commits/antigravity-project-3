import os
from PIL import Image

image_dir = "final_screenshots"
files = sorted([f for f in os.listdir(image_dir) if f.endswith(".png")])

print(f"Total screenshots in {image_dir}: {len(files)}")
for f in files:
    path = os.path.join(image_dir, f)
    with Image.open(path) as img:
        print(f"{f}: {img.size} ({img.format})")
