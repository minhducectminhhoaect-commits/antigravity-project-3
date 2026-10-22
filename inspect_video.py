import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

try:
    with open('video_info.json', 'r', encoding='utf-16') as f:
        data = json.load(f)
except Exception:
    with open('video_info.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

with open('summary_info.txt', 'w', encoding='utf-8') as out:
    out.write(f"Title: {data.get('title')}\n")
    out.write(f"Duration: {data.get('duration')} seconds ({data.get('duration')//60}m {data.get('duration')%60}s)\n")
    out.write(f"Uploader: {data.get('uploader')}\n")
    out.write(f"Upload Date: {data.get('upload_date')}\n")
    out.write(f"Chapters count: {len(data.get('chapters') or [])}\n")
    if data.get("chapters"):
        for c in data["chapters"]:
            out.write(f"  {c.get('start_time')}s - {c.get('title')}\n")
    out.write(f"Subtitles: {list((data.get('subtitles') or {}).keys())}\n")
    out.write(f"Automatic captions: {list((data.get('automatic_captions') or {}).keys())}\n")
    out.write("\n--- Description ---\n")
    out.write(data.get("description") or "")

print("Saved to summary_info.txt")
