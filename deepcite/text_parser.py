from nltk.tokenize import sent_tokenize, word_tokenize
from .utils import *
import numpy as np
import nltk
import urllib.request
from bs4 import BeautifulSoup


# TODO: create class that includes both the text and the links as lists and
# put this into all following functions
class Parser:
    def __init__(self, site):
        file = urllib.request.urlopen(site)
        html = file.read()
        file.close()
        soup = BeautifulSoup(html, 'html.parser').find_all('p')
        content = [tag.contents for tag in soup]

        # TODO: It may be faster for this to be:
        # [[text, link],[text],[text,link]]
        self.page_text = []
        self.page_links = {}
        i = 0
        for tag in content:
            for part in tag:
                if (hasattr(part, 'attrs') and 'href' in part.attrs):
                    self.page_links[i] = part.attrs['href']

                # TODO: what about the \xa0 values
                if part.string:
                    self.page_text.append(part.string)
                    i += 1


def get_info(parser):
    sectioned = section_text(parser)
    return node(clean(sectioned.text), sectioned.site)


# split into sentences or paragraphs or places in between text and retain
# which sections the links point to
def section_text(parser):
    # get the position of each link when all text is combined
    text = ''
    links = {}
    for i, section in enumerate(parser.page_text):
        text += section
        if (parser.page_links.get(i)):
            links[len(text) - 1] = parser.page_links[i]

    sentences = sent_tokenize(text)
    new_links = {}
    # TODO: when sent_token runs it removes some values so finding the location
    # by index does not automatically work
    start_index = 0
    for i, sent in enumerate(sentences):
        end_index = start_index + len(sent) + 1
        keys = list(links)
        for key in keys:
            if key < end_index and key > start_index:
                new_links[i] = links[key]
                del links[key]

        start_index = end_index

    return node(sentences, new_links)
