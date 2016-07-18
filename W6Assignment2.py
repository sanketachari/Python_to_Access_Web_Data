import json
import urllib

secureurl = 'http://python-data.dr-chuck.net/geojson?'
# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = raw_input('Enter address - ')
if len(address)> 0:
	encodedUrl = urllib.urlencode({'sensor':'false', 'address': address})
	url = secureurl + encodedUrl

	print 'Retrieving URL', url
	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved',len(data),'characters'

	try: js = json.loads(str(data))
	except: js = None

	if 'status' not in js or js['status']!= 'OK':
		print '==== Failure To Retrieve ===='
		print data

	print json.dumps(js, indent=4)
	print js['results'][0]['place_id']

else:
	print 'Invalid Address'

