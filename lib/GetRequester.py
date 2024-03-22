#!usr/bin/env python

import requests
import json


url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'

class GetRequester:

    def __init__(self, url):
        self.url = url
       
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        return json.loads(self.get_response_body())

# Instantiate the GetRequester class with the URL
requester = GetRequester(url)

# Call the load_json method to load and print the JSON data
json_data = requester.load_json()
print(json_data)
