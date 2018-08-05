#!/usr/bin/env python3

from html.parser import HTMLParser
from urllib import request
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.flag=0
        self.logdata=0
        self.information = []
        self.__dataname = 0
    def handle_starttag(self, tag, attrs):
        if tag=='ul'  and attrs[0][1] == 'list-recent-events menu':
            print('find a ul:', attrs)
            self.flag=1
        if self.flag==1:
            if tag=='a' and attrs[0][0] == 'href':
                print('\nTitle: ', end='')
                self.logdata=1
            elif tag=='time':
                print('Time: ', end='')
                self.logdata=2
            elif tag=='span' and self.logdata==2:
                self.logdata=1
            elif tag=='span' and attrs[0][1]=='event-location':
                print('Location: ', end='')
                self.logdata=1
        #pass #print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        if tag=='ul' and self.flag==1:
            self.flag=0
            print('encountered ul end')
       #pass #print("Encountered an end tag:", tag)

    def handle_data(self, data):
        if self.flag == 1:
            if self.logdata==1:
                self.logdata=0
                print(data)
            elif self.logdata==2:
                print(data, end=' ')
        pass #print("Encountered some data:", data)


parser = MyHTMLParser()
#parser.feed('<html><head><title>Test</title></head>')
print('Feed some text to the parser. It is processed insofar as it consists of complete elements; incomplete data is buffered until more data is fed or close() is called. data must be str.')
#parser.feed('<body><h1>Parse me!</h1></body></html>')

URL='https://www.python.org/events/python-events/'
with request.urlopen(URL) as f:
    data = f.read().decode('utf-8')
print(data)
parser.feed(data)
