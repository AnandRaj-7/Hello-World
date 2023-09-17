import os
path  = "little pics"
for folder, sub_folder, file_names in os.walk(path):
    for file_name in file_names:
        # str1 = "to be deleted.jpg"
        # str2 = "definitely has to go.jpg"
        if((os.path.getsize(os.path.join(folder, file_name))) <= 5000 and (file_name.endswith("definitely has to go.jpg") or file_name.endswith("to be deleted.jpg"))):
            os.remove(os.path.join(folder, file_name))