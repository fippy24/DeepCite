# import PageParser as pp
from deepcite.text_parser import *

from deepcite.compare import *
from deepcite.visualize import visualize

max_it = 5
start_text = ''


def be_all_end_all(node, iteration):
    parser = Parser(node.site)
    source = prepare_source(start_text)
    page = get_info(parser)
    children = find_closest(source, page, compute_smallest_distance())
    if (iteration < max_it and children is not None):
        for child in children:
            visualize(children)
            be_all_end_all(child, iteration + 1)
    else:  # TODO: need a better ending
        if (children is None):
            return [node]
        else:
            return children


# Call pytest from this folder to run it.
def test_main():
    start_site = 'http://www.aauw.org/research/' \
                 'the-simple-truth-about-the-gender-pay-gap/'
    start_text = 'As a result, women who complete college degree ' \
                 'are less able to pay off their student loans promptly, ' \
                 'leaving them paying more and for a longer time than men.'
    iteration = 0
    be_all_end_all(node(start_text, start_site), iteration)
