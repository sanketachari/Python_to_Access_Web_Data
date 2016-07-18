import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_286829.xml'

data = urllib.urlopen(url).read();

tree = ET.fromstring(data)
counts = tree.findall('.//count')
numlist = list()
for count in counts:
	num = count.text
	numlist.append(int(num))

print(sum(numlist))

