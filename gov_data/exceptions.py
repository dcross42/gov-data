""" List of exceptions for the gov_data package. """

class InvalidURL(Exception):
    """ Exception for invalid URLs """
    def __init__(self, provided_url: str):
        self.provided_url = provided_url
        super().__init__(f"Invalid URL: {provided_url}")

class InvalidAPIKey(Exception):
    """ Exception for invalid API keys """
    def __init__(self, api_name: str):
        self.api_name = api_name
        super().__init__(f"Invalid API key for {api_name}")
