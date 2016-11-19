import re

name = raw_input("Enter file: ")
handle = open(name)
x = list()

for line in handle:
    y = re.findall('[0-9]+', line)
    x = x + y

sum = 0
for i in x:
    sum = sum + int(i)
print sum
    
