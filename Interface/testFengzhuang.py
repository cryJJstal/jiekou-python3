#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import hashlib
import json

import requests
from Public.test_requests import requ
reques=requ()
class TestApi(object):
	def __init__(self,url,connent,type):
		self.url=url
		self.connent=connent
		self.type=type
		

	def testapi(self):
		if self.type=='POST':
			self.parem = {self.connent}
			self.response=reques.post(self.url,self.parem)
		elif self.type=='GET':
			self.parem = {self.connent}
			self.response = reques.get(url=self.url,params=self.parem)
		return self.response
	def getJson(self):
		json_data = self.testapi()
		print(json_data)
		# json_print = json.dumps(json_data,sort_keys=True, indent=4, separators=(',', ':'))
		return json_data