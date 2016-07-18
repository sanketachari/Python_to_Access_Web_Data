import urllib
from BeautifulSoup import*

url = 'http://python-data.dr-chuck.net/comments_286832.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')

numlist = list()
for tag in tags:
	num = tag.contents[0]
	numlist.append(int(num))

print sum(numlist)

