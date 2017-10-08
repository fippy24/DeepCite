from .utils import *


# returns the closest sections of text and their respective links,
# TODO: draw a social network map
def find_closest(source, page, max_dist):
    closest = []
    most = 0.0
    for i, sent in enumerate(page.text):
        dist = cosign_dist(source, sent)
        if dist > most:
            most = dist
        if dist >= max_dist:
            closest.append(node(sent, page.site.get(i, '')))
    return closest


# TODO: what if the source is multiple sentences
def prepare_source(text):
    return clean([text])[0]
