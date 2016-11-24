import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter location: ')
print 'Retrieving', address
uh = urllib.urlopen(address)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

count = 0
total = 0
counts = tree.findall('comments/comment')

for i in counts:
    x = i.find('count').text
    total += int(x)
    count += 1
print 'Count:', count
print 'Sum:', total
