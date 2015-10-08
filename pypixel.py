"""
PyPixel wrapper by @WireSegal
With help from @TheDestruc7i0n
You may use this code, as long as you give credit
https://thedestruc7i0n.ca/pypixel

Allows you to make calls to the Hypixel API through python.
"""

import json
import urllib2
import time

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
	req = urllib2.Request(url, headers={ 'User-Agent': 'application/json' })
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
		return self.main("key")
		
	def boosters(self):
		"""
		nothing -> gets list of boosters
		"""
		return self.main("boosters")
		
	def boosters(self):
		"""
		nothing -> gets list of leaderboards
		"""
		return self.main("leaderboards")

	def friends(self, username):
		"""
		string -> dict of friends of the player USERNAME
		"""
		return self.main("friends", {"player": username})

	def guildByMember(self, username):
		"""
		string -> dict of a hypixel guild containing player USERNAME
		"""
		return self.main("findGuild", {"byPlayer": username})

	def guildByName(self, name):
		"""
		string -> dict of a hypixel guild named NAME
		"""
		return self.main("findGuild", {"byName": name})

	def guildByID(self, guildID):
		"""
		string -> dict of a hypixel guild with id GUILDID
		"""
		return self.main("guild", {"id": guildID})

	def session(self, username):
		"""
		string -> dict of USERNAME's session
		"""
		return self.main("session", {"player": username})

	def userByUUID(self, uuid):
		"""
		string -> information about player with uuid UUID
		"""
		return self.main("player", {"uuid": uuid})
		
	def userByName(self, name):
		"""
		string -> information about player with name NAME
		"""
		return self.main("player", {"name": name})

	def main(self, action, args={}):
		"""
		string -> result of api call ACTION
		string, dict -> result of api call ACTION with arguments ARGS
		"""
		url = self.base + action
		params = dict(args, **baseParams)
		return json.loads(urlopen(url, params))


class MultiKeyAPI:
	"""
	A class that handles using multiple keys for more requests-per-minute. 
	Acts exactly like HypixelAPI for making API calls.
	list -> api class
	list, int -> api class with delay of int seconds
	list, int, bool -> api with delay of int seconds with debug mode in bool
	"""
	def __init__(self, keys, delay = 5, debug = False):
		self.apis = [HypixelAPI(i) for i in keys]
		self.apii = 0
		self.api = self.apis[self.apii]
		self.delay = delay
		self.debug = debug

	def _changeInstance(self):
		self.apii += 1
		self.apii %= len(self.apis)
		self.api = self.apis[self.apii]

	def _throttleproofAPICall(self, callType, *args):
		loaded = getattr(self.api, callType)(*args)
		while "throttle" in loaded:
			if self.debug: 
				print("Throttled, changing instance")
			time.sleep(self.delay)
			self._changeInstance()
			loaded = getattr(self.api, callType)(*args)
		return loaded

	def keyRequest(self):               return self._throttleproofAPICall("keyRequest")
	def boosters(self):                 return self._throttleproofAPICall("boosters")
	def friends(self, username):        return self._throttleproofAPICall("friends", username)
	def guildByMember(self, username):  return self._throttleproofAPICall("guildByMember", username)
	def guildByName(self, name):        return self._throttleproofAPICall("guildByName", name)
	def guildByID(self, guildID):       return self._throttleproofAPICall("guildByID", guildID)
	def session(self, username):        return self._throttleproofAPICall("session", username)
	def userByUUID(self, uuid):         return self._throttleproofAPICall("userByUUID", uuid)
	def userByName(self, name):         return self._throttleproofAPICall("userByName", name)
	def main(self, action, args={}):    return self._throttleproofAPICall("main", action, args)

