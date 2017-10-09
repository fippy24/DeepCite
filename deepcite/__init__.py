# Not usually good practice to put code in the __init__.py,
# but this will save us form needing to download nltk data all the time.
import os
import nltk
PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
nltk.data.path.append(os.path.join(PACKAGE_DIR, "..", "nltk_data"))