"""
PyPixel wrapper by @WireSegal
With help from @TheDestruc7i0n
You may use this code, as long as you give credit
https://thedestruc7i0n.ca/pypixel

Allows you to make calls to the Hypixel API through python.
"""

import json
import urllib2

def expandUrlData(data):
	"""
	dict -> a param string to add to a url
	"""
	string = "?" # the base for any url
	dataStrings = []
	for i in data:
		dataStrings.append(i+"="+data[i])
	string += "&".join(dataStrings)
	return string


def urlopen(url, params={}):
	"""
	string, dict -> data from the url
	"""
	url += expandUrlData(params)
	req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' }) # lol spoofed the user agent as firefox, seems legit
	html = urllib2.urlopen(req).read()
	return html

class HypixelAPI:
	"""
	A class that allows you to make hypixel api calls.
	string -> api class
        """
	base = "https://api.hypixel.net/"
	def __init__(self, key):
		self.key = key
		self.baseParams = {"key": self.key}

	def keyRequest(self):
		"""
		nothing -> dict of stats for your api key
		"""
		url = self.base + "key"
		params = self.baseParams
		return json.loads(urlopen(url, params))

	def friends(self, username):
		"""
		string -> dict of friends of the player USERNAME
		"""
		url = self.base + "friends"
		params = self.baseParams
		params["player"] = username
		return json.loads(urlopen(url, params))

	def guildByMember(self, username):
		"""
		string -> dict of a hypixel guild containing player USERNAME
		"""
		url = self.base + "findGuild"
		params = self.baseParams
		params["byPlayer"] = username
		return json.loads(urlopen(url, params))

	def guildByName(self, name):
		"""
		string -> dict of a hypixel guild named NAME
		"""
		url = self.base + "findGuild"
		params = self.baseParams
		params["byName"] = name
		return json.loads(urlopen(url, params))

	def guildByID(self, guildID):
		"""
		string -> dict of a hypixel guild with id GUILDID
		"""
		url = self.base + "guild"
		params = self.baseParams
		params["id"] = guildID
		return json.loads(urlopen(url, params))

	def session(self, username):
		"""
		string -> dict of USERNAME's session
		"""
		url = self.base + "session"
		params = self.baseParams
		params["player"] = username
		return json.loads(urlopen(url, params))

	def userByUUID(self, uuid):
		"""
		string -> information about player with uuid UUID
		"""
		url = self.base + "player"
		params = self.baseParams
		params["uuid"] = uuid
		return json.loads(urlopen(url, params))
		
	def userByName(self, name):
		"""
		string -> information about player with name NAME
		"""
		url = self.base + "player"
		params = self.baseParams
		params["name"] = name
		return json.loads(urlopen(url, params))


