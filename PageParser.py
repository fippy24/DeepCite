import urllib.request
from html.parser import HTMLParser
from topics import *


#The dictionary below contains all of the html tags and their associated data
#in the following (key : pair) format. (pageIndex : data) 
#Currently this dictionary does not contain the Attributes of the tags
htmlPage = {}

#Ditionary containing (pageIndex : hyperlink)
links = {}


class MyHTMLParser(HTMLParser):

    #This is the global index for htmlPage and links
    pageIndex = 0

    def handle_starttag(self, tag, attrs):
        #increment the page index for every tag seen 
        self.pageIndex += 1
        for a in attrs:
            if re.search(r'href', a[0]): # TODO: the numerical links are not href's
                links[self.pageIndex] = a # TODO: link is associated with the text after, not before

    def handle_data(self, data):
        #check if there are words in the data and there is an index
        if re.search(r'\w+', data) and self.pageIndex:
            htmlPage[self.pageIndex] = trimSentence(data)
            #print(trimSentence(data))

    def handle_comment(self, data):
        #comments are assumed useless
        #however if the comments are not caught by the parser they are interpreted as data
        pass

parser = MyHTMLParser()
with urllib.request.urlopen('https://academic.oup.com/nar/article/38/suppl_2/W214/1126704/The-GeneMANIA-prediction-server-biological-network#20150589') as f:
    parser.feed(f.read().decode('utf-8'))

text = "The two non-adaptive methods are the most conservative options and work well on small gene lists"
most=0.0
for i in htmlPage.keys():
    dist = cosign_dist(trimSentence(text),htmlPage[i])
    if not dist==0.0:
        # print(htmlPage[i])
        # print(dist)
        if dist > most:
            most = dist
            print(htmlPage[i])
            print(dist)
            print(links.get(i))