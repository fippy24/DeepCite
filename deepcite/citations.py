# This will use regex to create an object composed of possible citations
import re
from WebCrawler import *

generalMLA = re.compile(r'[A-Za-z ]+\.[A-Za-z ]+\..+,')

for x, y in htmlPage.items():
    try:
        print(y)
    except UnicodeEncodeError:
        raise
