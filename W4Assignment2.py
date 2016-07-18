import urllib
from BeautifulSoup import*

nxtUrl = 'http://python-data.dr-chuck.net/known_by_Maja.html '
nameList = list()

for i in range(1,8):
	html = urllib.urlopen(nxtUrl).read()
	soup = BeautifulSoup(html)
	tags = soup('a')

	nxtUrl = tags[17].get('href',None)
	nameList.append(str(tags[17].contents[0]));

print nameList[6]


