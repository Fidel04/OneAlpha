import os

path = r"Data\imbalanced"

with open(r"meta\labels.txt", "w") as file:
    for root, dirs, files in os.walk(path):
        if root != path:
            label_name = os.path.basename(root)
            label = label_name.replace("_", " ")
            file.write(f"{label}\n")
