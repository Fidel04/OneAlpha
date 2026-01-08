import os

path = r"Data\new_data\val"
img_count = 0
total_count = 0
with open(r"Data\new_data\count_val.txt", "w") as file:
    for root, dirs, files in os.walk(path):
        if root != path:
            class_name = os.path.basename(root)
            print(f"currently in: {class_name}".ljust(50), end="\r")
            file.write(f"{class_name} - {len(files)}\n")
            total_count += len(files)
    file.write(f"Total image: {total_count}\n")