import urllib
import json

#Gets the current temperature of a city requested by the user.
#Uses API from http:http://openweathermap.org/ to get weather information in JSON format and parses it to get current temperature
# personal id key provided by the above website has to be supplied in the 'id' field for the program to execute

url='http://api.openweathermap.org/data/2.5/weather?q='
id='xxxxxxxxxx'#personal app id from http://openweathermap.org/
city= raw_input('enter city')
url=url+city.strip()+'&APPID='+id
try:
	uh = urllib.urlopen(url)
	data = uh.read()
	info=json.loads(data)
	temp_in_k=info['main']['temp']#API returns data in Kelvin
	temp_in_C=temp_in_k-273 
	print "Current temperature at "+city.strip()+" : "+str(temp_in_C)+" C"
except:
	print "Invalid city!"


