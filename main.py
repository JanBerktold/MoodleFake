#!/usr/bin/env python
#

import webapp2
import requests
import re
import thread

from google.appengine.api import urlfetch

urlfetch.set_default_fetch_deadline(60)

## CHANGE
username = "XX"
password = "XX"

## FINGER WEG

def handleLogin(self):
	session = requests.Session()

	def login():
		global cookies

		request = session.post("http://aeg-schulnetz.de/login/index.php", {"username":username, "password":password})
		responseText = request.text.encode('utf-8')

	def loadKurse():
		request = session.get("http://aeg-schulnetz.de/my/")
		responseText = request.text.encode('utf-8')

		# forced to use a dictionary, because the urls are listed multipli times
		dict = {}
		for result in re.finditer("http://aeg-schulnetz.de/course/view.php\?id=[0-9]+", responseText):
			dict[result.group()] = True

		return dict

	def getKurse(Kurse):
		for url in Kurse:
			self.response.out.write(url + '\n')
			session.get(url)

	if login():
		getKurse(loadKurse())

class MainHandler(webapp2.RequestHandler):
	def get(self):
		handleLogin(self)

app = webapp2.WSGIApplication([
	('/handler', MainHandler)
], debug=True)
