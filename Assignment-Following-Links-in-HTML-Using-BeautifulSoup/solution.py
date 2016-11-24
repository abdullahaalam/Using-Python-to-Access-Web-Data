import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

for _ in xrange(0, count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup.findAll('a')
    print "Retrieving: ", url

    for tag in tags:
        url = tag.get('href')
        url = tags[position - 1].get('href')
    
print "Retrieving: ", url

