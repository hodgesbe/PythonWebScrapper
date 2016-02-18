__author__ = 'bHodges'
import urllib2
from HTMLParser import HTMLParser
import sys


#htmlFile = urllib2.urlopen(sys.argv[1]).read()

htmlFile = urllib2.urlopen("http://www.cs.unca.edu/brock/classes/Spring2015/csci373/homework/home03.html")
htmlText=htmlFile.read()
#print htmlText


class LinkFinder(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.link = None
        self.text = None
        self.lasttag = None
        self.isLink = False
    def handle_starttag(self, tag, attrs):
        self.isLink = False
        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    self.link = value
                    self.text = self.get_starttag_text()
                    self.lasttag = tag
                    self.isLink = True

    def handle_endtag(self, tag):
        if tag == 'a':
            self.isLink = True

    def handle_data(self, data):
        if self.lasttag == 'a' and self.isLink:
            print self.text
            print self.link


parser = LinkFinder()
parser.feed(htmlText)
