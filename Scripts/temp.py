import os

path = r"Data\imbalanced"

for root, dirs, files in os.walk(path):
    if root != path:
        new_path = root.replace(" ", "_")
        os.rename(root, new_path)