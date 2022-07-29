import requests
import json

class GetData(object):
	"""docstring for GetData"""
	def __init__(self, year, id):
		super(GetData, self).__init__()
		self.year = year
		self.id = id
	
	def _getLink(self):
		return f"https://dantri.com.vn/thpt/1/0/99/{self.id}/{self.year}/0.2/search-gradle.htm"

	def rawData(self):
		url = self._getLink()
		response = requests.get(url)
		data = response.json()
		# print(data["student"])
		return data["student"]
