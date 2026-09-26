import os
import shutil

def copy_files_recursive(src: str, dest: str) -> None:
    if not os.path.exists(dest):
        os.mkdir(dest)
        
    for item in os.listdir(src):
        item_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        print(f" ' {item_path} -> {dest_path}")
        if os.path.isfile(item_path):
            shutil.copy(item_path, dest)
        else: 
            copy_files_recursive(item_path, dest_path)