import re

def clean_vtt(vtt_file):
    with open(vtt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    entries = []
    current_time = ""
    current_text = []
    
    time_pattern = re.compile(r'(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}\.\d{3})')
    
    for line in lines:
        line = line.strip()
        m = time_pattern.search(line)
        if m:
            if current_time and current_text:
                entries.append((current_time, " ".join(current_text)))
                current_text = []
            current_time = f"{m.group(1)} --> {m.group(2)}"
        elif line and not line.startswith("WEBVTT") and not line.startswith("Kind:") and not line.startswith("Language:"):
            # strip xml tags like <c> </c>
            clean_line = re.sub(r'<[^>]+>', '', line).strip()
            if clean_line and (not current_text or current_text[-1] != clean_line):
                current_text.append(clean_line)
                
    if current_time and current_text:
        entries.append((current_time, " ".join(current_text)))
        
    return entries

entries = clean_vtt('video.en.vtt')
with open('transcript_cleaned.txt', 'w', encoding='utf-8') as out:
    for t, text in entries:
        out.write(f"[{t}] {text}\n")

print(f"Total entries: {len(entries)}")
