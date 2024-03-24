"""
Base class for interacting with Government data APIs
"""

from abc import ABC, abstractmethod
from typing import Optional


class BaseGovDataAPI(ABC):
    """ Base class for interacting with Government data APIs """
    def __init__(self, base_url: str, api_key : str | Optional[None] = None):
        if api_key is not None:
            self.api_key = api_key
        self.base_url = base_url

    @abstractmethod
    def build_url(self, **kwargs):
        """ Build the URL to interact with the API """
        pass
    
    @abstractmethod
    def get_data(self, **kwargs):
        """ Get data from the API """
        pass

