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

sys.path.insert(0,
                os.path.abspath('../'))  # Source code dir relative to this file

project = 'geocat-tutorials'
current_year = datetime.datetime.now().year
copyright = u'{}, University Corporation for Atmospheric Research'.format(
    current_year)
author = 'GeoCAT'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    'myst_nb',
    "nbsphinx",
    "sphinx_design",
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
}

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_title = ""

html_theme_options = dict(
    repository_url="https://github.com/NCAR/geocat-tutorials",
    repository_branch="main",
    path_to_docs="docs",
    use_edit_page_button=True,
    use_repository_button=True,
    home_page_in_toc=False,
    navbar_footer_text="",
    extra_footer=
    "<em>The National Center for Atmospheric Research is sponsored by the National Science Foundation. Any opinions, findings and conclusions or recommendations expressed in this material do not necessarily reflect the views of the National Science Foundation.</em>",
)

html_favicon = '../images/logos/GeoCAT_square.svg'
html_logo = '../images/logos/GeoCAT_nsf.svg'
html_static_path = ['_static']


# turn off notebook execution
# set to "auto" for default behavior
nb_execution_mode = "off"

# pull in the notebooks from the source directory
if os.path.exists("./notebooks/"):
    os.system("rm -rf ./notebooks/")
os.system("mkdir ./notebooks/")
os.system("cp -r ../notebooks/*/*.ipynb ./notebooks/")
