# Configuration file for the Sphinx documentation builder

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add paths here if your source files or extensions live elsewhere
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'How to Log in to Quicken'
copyright = '2025'
author = 'Your Name or Company'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output settings ----------------------------------------------------

html_title = "How to Log in to Quicken – Complete Guide"
html_short_title = "Quicken Login Help"
html_favicon = 'favicon.ico'

# Theme (default is fine, or choose one you prefer)
# html_theme = 'sphinx_rtd_theme'  # Uncomment if you want ReadTheDocs style
# html_theme = 'alabaster'        # Simple and lightweight
# html_theme = 'furo'             # Modern and responsive

html_show_sourcelink = False
html_allow_unsafe = True

html_theme_options = {
    'show_powered_by': False,
}

# Static files (only needed if you use custom CSS or JS)
# html_static_path = ['_static']
