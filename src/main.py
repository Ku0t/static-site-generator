from asyncio import base_subprocess
import os, shutil, sys
from copystatic import copy_files_recursive
from generate import generate_pages_recursive

src_path_static: str = "./static"
dest_path_public: str = "./docs"
content_path: str = "./content"
template_path: str = "./template.html"
default_basepath: str = "/"


def main() -> None:
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath: str = sys.argv[1]
    
    print("Deleting public directory...")
    if os.path.exists(dest_path_public):
        shutil.rmtree(dest_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(src_path_static, dest_path_public)

    print("Generating content...")
    generate_pages_recursive(content_path, template_path, dest_path_public, basepath)

if __name__ == "__main__":
    main()
