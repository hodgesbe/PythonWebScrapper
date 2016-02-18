__author__ = 'Brett Hodges'
import urllib2
from HTMLParser import HTMLParser
import sys


htmlFile = urllib2.urlopen(sys.argv[1]).read()

#Overwritten HTMLParser
class LinkFinder(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.isLink=False
        self.lasttag = None
        self.link = None

#handles <a> tags and seperates there attributes
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for val, value in attrs:
                if val == 'href':
                    self.isLink = True
                    self.lasttag = tag
                    self.link = value

#checks to see if last tag seen was an <a> to determine if still inside tag
    def handle_endtag(self, tag):
        if tag == 'a':
            self.isLink = False

#prints data seperated from handled tags
    def handle_data(self, data):
        if self.lasttag =='a' and self.isLink:
            print data
            print self.link
            



#Creates an HTMLParser and calls it on file entered by user
parser = LinkFinder()
parser.feed(htmlFile)
