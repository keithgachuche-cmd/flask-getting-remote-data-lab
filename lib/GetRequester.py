import requests
import json


class GetRequester:
    '''Takes a URL, fetches it with an HTTP GET, and parses JSON responses.'''

    def __init__(self, url):
        # Store the endpoint this requester will query
        self.url = url

    def get_response_body(self):
        # Send a GET request to the endpoint and return the raw response body (bytes)
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # Convert the response body into Python data (a list of dicts)
        return json.loads(self.get_response_body())