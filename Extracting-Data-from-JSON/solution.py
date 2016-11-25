import urllib
import json

address = raw_input('Enter location: ')
print 'Retrieving', address

uh = urllib.urlopen(address)
data = uh.read()
print 'Retrieved', len(data), 'characters'

info = json.loads(data)
print 'Count:', len(info['comments'])

total = 0

for i in range(len(info['comments'])):
    total += int(info['comments'][i]['count'])
print "Sum:", total
