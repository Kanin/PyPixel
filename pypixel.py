"""
PyPixel wrapper by @WireSegal
With help from @TheDestruc7i0n
You may use this code, as long as you give credit
https://thedestruc7i0n.ca/pypixel

Allows you to make calls to the Hypixel API through python.
"""
from __future__ import print_function

import json
import urllib2
import time

# If you want to use a custom printer function, you can overwrite pypixel.printer.
printer = print

class Player:
	"""
	A class which wraps player info.
	string -> Player object for that username
	string, HypixelAPI|MultiKeyAPI -> Player object with that api for that username
	string, HypixelAPI|MultiKeyAPI, string -> Player object with that api for that username, using that url to get the uuid
	"""
	def __init__(self, name, api=None, url=None):
		self.name = name
		if isinstance(api, HypixelAPI):
			self.api = api
		else:
			self.api = None
		if url is not None:
			self.uuid = getUUID(name, url)
		else:
			self.uuid = getUUID(name)
	def friends(self, api=None):
		"""
		nothing -> friends of this player
		HypixelAPI|MultiKeyAPI -> friends of this player, using that api instance
		"""
		if api and isinstance(api, HypixelAPI):
			return api.friends(self)
		elif self.api:
			return self.api.friends(self)
		else:
			return {}
	def info(self, api=None):
		"""
		nothing -> info on this player
		HypixelAPI|MultiKeyAPI -> info on this player, using that api instance
		"""
		if api and isinstance(api, HypixelAPI):
			return api.userByUUID(self)
		elif self.api:
			return self.api.userByUUID(self)
		else:
			return {}
	def guild(self, api=None):
		"""
		nothing -> guild of this player
		HypixelAPI|MultiKeyAPI -> guild of this player, using that api instance
		"""
		if api and isinstance(api, HypixelAPI):
			return api.guildByID(api.guildByMemberUUID(self).get("guild"))
		elif self.api:
			return self.api.guildByID(self.api.guildByMemberUUID(self).get("guild"))
		else:
			return {}
	def session(self, api=None):
		"""
		nothing -> session of this player
		HypixelAPI|MultiKeyAPI -> session of this player, using that api instance
		"""
		if api and isinstance(api, HypixelAPI):
			return api.session(self)
		elif self.api:
			return self.api.session(self)
		else:
			return {}

def getType(inp):
	"""
	int -> 0 for UUID, 1 for USERNAME
	"""
	UUID = 0
	USERNAME = 1
	
	if len(inp) == 32: return UUID
	return USERNAME

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
	
def getUUID(username, url="https://api.mojang.com/users/profiles/minecraft/%s", returnthis="id"):
	"""
	string -> get UUID from USERNAME
	string, string -> get UUID from username via different API
	string, string, string -> return another dictionary element from result
	"""
	return json.loads(urlopen(url % username, {"at":str(int(time.time()))})).get(returnthis)
	
def hasPaid(username, url="https://mcapi.ca/other/haspaid/%s", returnthis="premium"):
	"""
	string -> if USERNAME has a premium account
	string, string -> get has paid via different API
	string, string, string -> return another dictionary element from result
	"""
	return json.loads(urlopen(url % username)).get(returnthis)

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
		
	def leaderboards(self):
		"""
		nothing -> gets list of leaderboards
		"""
		return self.main("leaderboards")

	def friends(self, username):
		"""
		string -> dict of friends of the player USERNAME
		Player -> dict of friends of the player
		"""
		if isinstance(username, Player): username = username.name
		if getType(username): username = getUUID(username)
		return self.main("friends", {"player": username})

	def guildByMember(self, username):
		"""
		string -> dict of a hypixel guild containing player USERNAME
		Player -> dict of a hypixel guild containing the player
		"""
		if isinstance(username, Player): username = username.name
		if getType(username): return self.guildByMemberUUID(getUUID(username))
		
	def guildByMemberUUID(self, uuid):
		"""
		string -> dict of a hypixel guild containing player UUID
		Player -> dict of a hypixel guild containing the player
		"""
		if isinstance(uuid, Player): uuid = uuid.uuid
		return self.main("findGuild", {"byUuid": uuid})

	def guildByName(self, name):
		"""
		string -> dict of a hypixel guild named NAME
		"""
		return self.main("findGuild", {"byName": name})

	def guildByID(self, guildID):
		"""
		string -> dict of a hypixel guild with id GUILDID
		"""
		if guildID: return self.main("guild", {"id": guildID}).update({"id": guildID})
		return {"guild": None, "success": False}

	def session(self, username):
		"""
		string -> dict of USERNAME's session
		Player -> dict of player's session
		"""
		if isinstance(username, Player): username = username.name
		if getType(username): username = getUUID(username)
		return self.main("session", {"player": username})

	def userByUUID(self, uuid):
		"""
		string -> information about player with uuid UUID
		Player -> information about the player
		"""
		if isinstance(uuid, Player): uuid = uuid.uuid
		return self.main("player", {"uuid": uuid})
		
	def userByName(self, name):
		"""
		string -> information about player with name NAME
		Player -> information about the player
		"""
		if isinstance(name, Player): name = name.name
		if getType(username): return self.userByUUID(getUUID(username))

	def main(self, action, args={}):
		"""
		string -> result of api call ACTION
		string, dict -> result of api call ACTION with arguments ARGS
		"""
		url = self.base + action
		params = dict(args, **self.baseParams)
		return json.loads(urlopen(url, params))


class MultiKeyAPI(HypixelAPI):
	"""
	A class that handles using multiple keys for more requests-per-minute. 
	Acts exactly like HypixelAPI for making API calls.
	list -> api class
	list, int -> api class with delay of int seconds
	list, int, bool -> api with delay of int seconds with debug mode in bool
	"""
	def __init__(self, keys, delay = 5, debug = False):
		if not keys:
			raise TypeError("No keys provided!")
		self.apis = [HypixelAPI(i) for i in keys]
		self.apii = 0
		self.api = self.apis[self.apii]
		self.baseParams = self.api.baseParams
		self.key = self.api.key

		self.delay = delay
		self.debug = debug

	def _changeInstance(self):
		self.apii = (self.apii+1) % len(self.apis)
		self.api = self.apis[self.apii]
		self.baseParams = self.api.baseParams
		self.key = self.api.key

	def main(self, action, args={}):
		loaded = self.api.main(action, args)
		if "throttle" in loaded:
			for i in self.apis:
				if self.debug: 
					printer("Throttled, changing instance")
				time.sleep(self.delay)
				self._changeInstance()
				loaded = self.api.main(action, args)
				if "throttle" not in loaded:
					return loaded
		return loaded

