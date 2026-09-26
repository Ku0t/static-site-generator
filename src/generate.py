import os
from pathlib import Path

from markdown_blocks import markdown_to_html_node, extract_title

def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    
    with open(from_path) as md:
        index_md = md.read()
    md.close()

    with open(template_path) as html:
        template = html.read()
    html.close()
    
    html_nodes = markdown_to_html_node(index_md)
    content_html = html_nodes.to_html()
    page_title = extract_title(index_md)

    new_title = template.replace("{{ Title }}", page_title)
    new_content = new_title.replace("{{ Content }}", content_html)
    new_content = new_content.replace('href="/', f'href="{basepath}')
    new_content = new_content.replace('src="/', f'src="{basepath}')

    if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as index_html:
        index_html.write(new_content)
    index_html.close()

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str) -> None:
    
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        print(f" ' {item_path} -> {dest_path}")
        if os.path.isfile(item_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(item_path, template_path, dest_path, basepath)
        else: 
            generate_pages_recursive(item_path, template_path, dest_path, basepath)


