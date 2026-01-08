import os

path = r"Data\imbalanced"

with open(r"meta\classes.txt", "w") as file:
    for root, dirs, files in os.walk(path):
        if root != path:
            class_name = os.path.basename(root)
            file.write(f"{class_name}\n")