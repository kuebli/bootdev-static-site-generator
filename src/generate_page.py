from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f_md:
        md = f_md.read()

        with open(template_path) as f_template:
            template_html = f_template.read()

            html_node = markdown_to_html_node(md)
            title = extract_title(md)

            template_html = template_html.replace("{{ Title }}", title)
            template_html = template_html.replace("{{ Content }}", html_node.to_html())
            template_html = template_html.replace('href="/', f'href="{basepath}')
            template_html = template_html.replace('src="/', f'src="{basepath}')

            with open(dest_path, "x") as f_html:
                f_html.write(template_html)
