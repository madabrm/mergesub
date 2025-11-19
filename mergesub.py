import os
import subprocess
import re

source_folder = os.getcwd()  # otomatis di folder aktif
output_folder = os.path.join(source_folder, "output")
os.makedirs(output_folder, exist_ok=True)

# Format file yang didukung
video_exts = ['.mkv', '.mp4', '.webm', '.avi', '.mov']
subtitle_exts = ['.srt', '.ass', '.ssa', '.sub', '.vtt', '.tiff']

# Mapping kode bahasa ke format mkvmerge
def langcode(suffix):
    mapping = {
        'ID': 'ind',
        'IN': 'ind',
        'EN': 'eng',
        'FR': 'fra',
        'JP': 'jpn',
        'ES': 'spa',
        'DE': 'deu',
    }
    return mapping.get(suffix.upper(), 'und')  # 'und' untuk undefined

# Deteksi semua file video
video_files = [f for f in os.listdir(source_folder) 
               if any(f.endswith(ext) for ext in video_exts)]

for video in video_files:
    base = os.path.splitext(video)[0]
    # Subtitle yang cocok dengan nama video, format apa saja
    subtitle_candidates = []
    for f in os.listdir(source_folder):
        if f.startswith(base) and any(f.endswith(ext) for ext in subtitle_exts):
            subtitle_candidates.append(f)

    tracks = []
    default_added = False
    for sub in subtitle_candidates:
        # Deteksi bahasa berdasarkan nama: base[_XX].ext
        # 'XX' adalah kode bahasa seperti EN, FR, dsb
        match = re.match(rf"^{re.escape(base)}(?:_([A-Za-z]+))?\.[^.]+$", sub)
        if match:
            suffix = match.group(1)
            if suffix is None and not default_added:
                lang = 'ind'     # Default indonesia jika tanpa suffix
                default_added = True
            else:
                lang = langcode(suffix if suffix else 'ID')
            tracks.append(("--language", f"0:{lang}", os.path.join(source_folder, sub)))

    if not tracks:
        print(f"Subtitle tidak ditemukan untuk {video}, lewati.")
        continue

    output_path = os.path.join(output_folder, video)
    cmd = ["mkvmerge", "-o", output_path, os.path.join(source_folder, video)]
    for track in tracks:
        cmd.extend(track)

    print("Menjalankan:", " ".join(cmd))
    subprocess.run(cmd)

print("Selesai proses.")
