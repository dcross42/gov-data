"""
Base class for interacting with Government data APIs
"""

from abc import ABC, abstractmethod

from .authentication import GovDataAPIKey


class BaseGovDataAPI(ABC):
    """ Base class for interacting with Government data APIs """
    def __init__(self, api_key : GovDataAPIKey):
        if api_key is None:
            raise ValueError("API key must be provided")
        self.api_key = api_key

    @property
    @abstractmethod
    def base_url(self):
        """ Base URL for the API """

    @abstractmethod
    def build_url(self, **kwargs):
        """ Build the URL to interact with the API """

    @abstractmethod
    def get_data(self, **kwargs):
        """ Get data from the API """
