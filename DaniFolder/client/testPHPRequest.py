import requests
import json

def makeRequest(url):
	return requests.post(url)

url = 'http://192.168.3.2/?userId=%22A2304D2%22'
response = makeRequest(url)
print(response.text.encode('utf-8'))
