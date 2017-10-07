from nltk.tokenize import sent_tokenize, word_tokenize
import re
import math
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter


class node():
    def __init__(self, text, site):
        self.text = text
        self.site = site


def clean(text):
    cleaned = []  # TODO: if I overwrite the input it would save space
    for sent in text:
        cleaned_sent = []
        # sent = re.sub(r'[^\x00-\x7F]', ' ', sent)
        for word in word_tokenize(sent):
            word = str(re.sub(r'\W+', ' ', word)).lower()
            if word not in stopWordList:
                cleaned_sent.append(porter.stem(word))
        cleaned.append(cleaned_sent)
    return cleaned


porter = PorterStemmer()
stopWordList = stopwords.words('english') + [' ']


def get_vector(text):
    return Counter(text)


def compute_smallest_distance():
    return .5


def cosign_dist(text1, text2):
    vec1 = get_vector(text1)
    vec2 = get_vector(text2)

    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator
