#!/usr/bin/python

#########################################################################
# Author	 : Austin Dubina					#
# Date 		 : 3/6/2013						#
# Description: Small python script that querys PuppetLabs Inc. server	#
# and returns the value of X-Answer header.			  	#
# Reference  : http://docs.python.org/2/library/httplib.html		#
#########################################################################

import sys
import httplib
import urllib

class Main():
	def __init__(self):
		pass

	# Establish a connection to PuppetLabs Inc. server
	def openConnection(self, url, port):
		self.conn = httplib.HTTPConnection(url, port)

	# Request a response from server
	def sendRequest(self, param):
		try:
			# Convert mapping object (param) to "percent-encoded" string
			self.param = "/?%s" %urllib.urlencode({"email" : param})
			self.conn.request("GET", self.param)
			self.response = self.conn.getresponse()
	
		except Exception as e:
			print "Error: %s" % sys.exit(e)

	#Print response values
	def printResponse(self):
		print "SERVER STATUS:", self.response.status, self.response.reason
		print "X-ANSWER VALUE:", self.response.getheader('X-Answer')
		print "LAST MODIFIED:", self.response.getheader('Last-modified')
		print "RESPONSE:", self.response.read()
		print self.response.getheaders()

	#Clean-up
	def closeConnection(self):
		try:
			self.conn.close()
		except Exception as e:
			print "Error: %s" % sys.exit(e)

if __name__ == "__main__":
	m = Main()
	m.openConnection("updates.puppetlabs.com", 9091)
	m.sendRequest("austin.dubina@gmail.com")
	m.printResponse()
	m.closeConnection()
