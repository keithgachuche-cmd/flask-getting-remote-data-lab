import requests
import json


class GetRequester:
    """Fetches data from a remote URL and parses JSON responses."""

    def __init__(self, url):
        # Store the endpoint so every method can reuse it
        self.url = url

    def get_response_body(self):
        # Send an HTTP GET request and return the raw response body (bytes)
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # Fetch the body, then parse it into Python lists/dicts
        return json.loads(self.get_response_body())