from copy_static_to_public import copy_static_to_public
from generate_pages_recursive import generate_pages_recursive
from os import path

static_path = path.abspath("") + "/static/"
public_path = path.abspath("") + "/public/"

copy_static_to_public(static_path, public_path)

content_path = path.abspath("") + "/content/"
template_path = path.abspath("") + "/template.html"

generate_pages_recursive(content_path, template_path, public_path)
