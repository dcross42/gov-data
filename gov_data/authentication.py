""" Handle import of API keys """

import os


class GovDataAPIKey:
    """ Handle import of API keys """
    def __init__(self, api_name: str, api_key: str):
        # TODO: Add logic to ensure only implemented APIs are allowed
        if api_name is not None and api_key is None:
            env_var = f"GOVDATA_{api_name}_API_KEY"
            self.api_key = os.environ[env_var]
        elif api_name is None and api_key is not None:
            self.api_key = api_key
        else:
            raise ValueError("Either api_name or api_key must be provided")

    def get_api_key(self):
        """ Get the API key """
        return self.api_key