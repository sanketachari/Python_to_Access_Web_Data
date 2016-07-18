import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_286833.json'

data = urllib.urlopen(url).read()
jsonData = json.loads(data)

# print json.dumps(jsonData, indent= 4)
numlist = list()

for i in range(0,len(jsonData["comments"])):
	num = jsonData['comments'][i]['count']
	numlist.append(int(num))


print sum(numlist)
