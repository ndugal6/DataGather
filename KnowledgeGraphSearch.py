"""Example of Python client calling Knowledge Graph Search API."""
import json
import urllib.parse
import requests

api_key = open('.api_key').read()
query = 'Taylor Swift'
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
    'query': query,
    'limit': 10,
    'indent': True,
    'key': api_key,
    'type': 'Person', # this can be any of https://schema.org/docs/full.html
}
url = service_url + '?' + urllib.parse.urlencode(params)
response = requests.get(url).json()
# reference for this api https://developers.google.com/knowledge-graph/reference/rest/v1/
for element in response['itemListElement']:
  print(element['result']['name'] + ' (' + str(element['resultScore']) + ')')