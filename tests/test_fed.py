""" 
Test the Fed API Connector
"""

import pytest

from gov_data.authentication import GovDataAPIKey
from gov_data.fed.fed import FederalReserveAPI


# From pytest docs: prevent requests from remote operations
@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """ Prevent requests from making remote calls """
    monkeypatch.delattr("requests.sessions.Session.request")

@pytest.fixture
def mock_api_key():
    """ Fake API key for testing """
    return GovDataAPIKey(api_name='test', api_key="test_API_key")

class TestFederalReserveAPI:
    """ Test the Federal Reserve API class """
    # TODO: Add tests for every endpoint
    # TODO: Add tests that should not be accepted by the class
    def test_fed_api_category_init(self, mock_api_key):
        """ Test the Federal Reserve API class initialization"""
        client = FederalReserveAPI(
            api_key=mock_api_key,
            endpoint="category",
            params={"category_id": 125}
        )
        assert client.endpoint == "category"
        assert client.params == {"category_id": 125}
        assert client.file_type == "json"
        assert client.timeout == 5

    def test_fed_api_category_build_url(self, mock_api_key):
        """ Test the Federal Reserve API class build_url method """
        client = FederalReserveAPI(
            api_key=mock_api_key,
            endpoint="category",
            params={"category_id": 125}
        )
        url = client.build_url()
        ans = "https://api.stlouisfed.org/fred/category?api_key=test_API_key&file_type=json&category_id=125"
        assert url == ans
