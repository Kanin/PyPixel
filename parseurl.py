
import json

def parseURL(url):
	url = url.split("?")[1]
	parseable = "{\"" + url.replace("=", "\": \"").replace("&", "\", \"") + "\"}"
	return json.loads(parseable)