import os
import shutil

path = input("Enter folder path: ")

items = os.listdir(path)

for item in items:
    item_path = os.path.join(path, item)

    if os.path.isfile(item_path):
        filename, ext = os.path.splitext(item)

        ext = ext[1:]

        if ext == "":
            ext = "no_extension"

        folder_name = os.path.join(path, ext)

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        shutil.move(item_path, os.path.join(folder_name, item))

print("Files organized successfully ✅")