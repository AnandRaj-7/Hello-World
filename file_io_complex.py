import os
import glob
path = "Images"
# print(os.listdir(path))
# glob.glob("*.png")
for current_folder, subfolders, file_names in os.walk(path):
    for file_name in file_names:
        print(os.path.join(current_folder, file_name))
        if file_name.endswith(".png"):
            new_name = os.path.join(current_folder, file_name)
            os.rename(new_name, new_name[:-4] + "_backup.png")
for current_folder, subfolders, file_names in os.walk(path):
    for file_name in file_names:
        if(os.path.exists(os.path.join(current_folder, file_name))):
            print(os.path.join(current_folder, file_name))