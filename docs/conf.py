# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
import datetime
from sphinx.application import Sphinx

# print path
print(sys.path)

project = 'geocat-tutorials'
current_year = datetime.datetime.now().year
copyright = u'{}, University Corporation for Atmospheric Research'.format(
    current_year)
author = 'GeoCAT'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "nbsphinx",
    "sphinx_design",
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
}

html_sourcelink_suffix = ''

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_title = ""

html_theme_options = {
    "repository_url":
        "https://github.com/NCAR/geocat-tutorials",
    "repository_branch":
        "main",
    "path_to_docs":
        "docs",
    "use_edit_page_button":
        True,
    "use_repository_button":
        True,
    "use_issues_button":
        True,
    "home_page_in_toc":
        False,
    "show_prev_next":
        False,
    "navbar_footer_text":
        "",
    "logo": {
        "image_light": "NSF_NCAR_light.png",
        "image_dark": "NSF_NCAR_dark.png",
    },
    "extra_footer":
        "<em>The NSF National Center for Atmospheric Research (NSF NCAR) is sponsored by the U.S. National Science Foundation. Any opinions, findings and conclusions or recommendations expressed in this material do not necessarily reflect the views of the U.S. National Science Foundation.</em>",
}

html_favicon = "./_static/GeoCAT_square.svg"

# turn off notebook execution
# set to "auto" for default behavior
nb_execution_mode = "auto"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ["style.css"]

# Allow for changes to be made to the css in the theme_overrides file
def setup(app):
    app.add_css_file('theme_overrides.css')
