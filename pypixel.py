# By WireSegal  (with help from TheDestruc7i0n)
# You may use the code with credit
# Tarball is at https://cdnme.ga/pypixel/PyPixel-1.0.tar.gz
# https://thedestruc7i0n.ca/pypixel

import json
import urllib2

def expandUrlData(data):
	string = "?" # the base for any url
	dataStrings = []
	for i in data:
		dataStrings.append(i+"="+data[i])
	string += "&".join(dataStrings)
	return string


def urlopen(url, params):
	url += expandUrlData(params)
	req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' }) # lol spoofed the user agent as firefox, seems legit
	html = urllib2.urlopen(req).read()
	return html

class HypixelAPI:
	base = "https://api.hypixel.net/"
	def __init__(self, key):
		self.key = key
		self.baseParams = {"key": self.key}

	def keyRequest(self):
		url = self.base + "key"
		params = self.baseParams
		return json.loads(urlopen(url, params))

	def friends(self, username):
		url = self.base + "friends"
		params = self.baseParams
		params["player"] = username
		return json.loads(urlopen(url, params))

	def guildByMember(self, username):
		url = self.base + "findGuild"
		params = self.baseParams
		params["byPlayer"] = username
		return json.loads(urlopen(url, params))

	def guildByName(self, name):
		url = self.base + "findGuild"
		params = self.baseParams
		params["byName"] = name
		return json.loads(urlopen(url, params))

	def guildByID(self, guildId):
		url = self.base + "guild"
		params = self.baseParams
		params["id"] = guildID
		return json.loads(urlopen(url, params))

	def session(self, username):
		url = self.base + "session"
		params = self.baseParams
		params["player"] = username
		return json.loads(urlopen(url, params))

	def userByUUID(self, uuid):
		url = self.base + "player"
		params = self.baseParams
		params["uuid"] = uuid
		return json.loads(urlopen(url, params))
		
	def userByName(self, name):
		url = self.base + "player"
		params = self.baseParams
		params["name"] = name
		return json.loads(urlopen(url, params))


