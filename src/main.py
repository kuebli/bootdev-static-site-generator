from copy_static_to_public import copy_static_to_public
from os import path

static_path = path.abspath("") + "/static/"
public_path = path.abspath("") + "/public/"
copy_static_to_public(static_path, public_path)
