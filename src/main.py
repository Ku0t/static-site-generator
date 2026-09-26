import os, shutil
from copystatic import copy_files_recursive
from generate import generate_page, generate_pages_recursive

src_path_static = "./static"
dest_path_public = "./public"
content = "./content"
template_html = "./template.html"
dest_path = "./public"
# content_md = "./content/index.md"
# template_html = "./template.html"
# dest_path_index = "./public/index.html"

# glorfindel_md = "./content/blog/glorfindel/index.md"
# majesty_md = "./content/blog/majesty/index.md"
# tom_md = "./content/blog/tom/index.md"
# contact_md = "./content/contact/index.md"

# dest_path_glorfindel = "./public/blog/glorfindel/index.html"
# dest_path_majesty = "./public/blog/majesty/index.html"
# dest_path_tom = "./public/blog/tom/index.html"
# dest_path_contact = "./public/contact/index.html"


def main() -> None:
    print("Deleting public directory...")
    if os.path.exists(dest_path_public):
        shutil.rmtree(dest_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(src_path_static, dest_path_public)
    generate_pages_recursive(content, template_html, dest_path)
    # generate_page(content_md, template_html, dest_path_index)
    # generate_page(glorfindel_md, template_html, dest_path_glorfindel)
    # generate_page(majesty_md, template_html, dest_path_majesty)
    # generate_page(tom_md, template_html, dest_path_tom)
    # generate_page(contact_md, template_html, dest_path_contact)

if __name__ == "__main__":
    main()
