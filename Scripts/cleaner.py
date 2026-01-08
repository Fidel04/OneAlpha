import os
from PIL import Image
from pathlib import Path

total_checked = 0
corrupted = 0

path = "imbalanced"
for root, dirs, files in os.walk(path):
    for name in files:
        total_checked += 1
        print(f"Checking [{total_checked}]: {name}", end="\r")
        file_path = os.path.join(root, name)
        try:
            if os.path.getsize(file_path) < 1024:
                os.remove(file_path)
                corrupted += 1
            else:
                with Image.open(file_path) as img:
                    img.verify()
        except (IOError, SyntaxError, OSError):
            if os.path.exists(file_path):
                os.remove(file_path)
                corrupted +=1

print(f"\n--- Process Finished ---")
print(f"Total files checked: {total_checked}")
print(f"Corrupted files deleted: {corrupted}")
            
