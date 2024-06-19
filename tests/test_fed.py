""" 
Test the Fed API Connector
"""

import pytest

from gov_data.authentication import GovDataAPIKey
from gov_data.fed.base import FederalReserveAPI
from gov_data.fed.employment import FederalReserveUnemployment
from gov_data.fed.interest_rates import FederalReserveFederalFundsRate
from gov_data.fed.national_accounts import FederalReserveGDP
from gov_data.fed.prices import FederalReserveCPI


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

    def test_fed_api_cpi_init(self, mock_api_key):
        """ Test the Federal Reserve API class initialization"""
        client = FederalReserveCPI(
            api_key=mock_api_key,
            params={},
        )
        assert client.observations_client.endpoint == "series/observations"
        assert client.observations_client.params == {"series_id": "CPIAUCSL"}
        assert client.observations_client.file_type == "json"
        assert client.observations_client.timeout == 5

        assert client.information_client.endpoint == "series"
        assert client.information_client.params == {"series_id": "CPIAUCSL"}
        assert client.information_client.file_type == "json"
        assert client.information_client.timeout == 5

        assert client.release_client.endpoint == "series/release"
        assert client.release_client.params == {"series_id": "CPIAUCSL"}
        assert client.release_client.file_type == "json"
        assert client.release_client.timeout == 5

        assert client.include_series_info is False
        assert client.include_series_release is False

    def test_fed_api_unemployment_init(self, mock_api_key):
        """ Test the Federal Reserve API class initialization"""
        client = FederalReserveUnemployment(
            api_key=mock_api_key,
            params={},
        )
        assert client.observations_client.endpoint == "series/observations"
        assert client.observations_client.params == {"series_id": "UNRATE"}
        assert client.observations_client.file_type == "json"
        assert client.observations_client.timeout == 5

        assert client.information_client.endpoint == "series"
        assert client.information_client.params == {"series_id": "UNRATE"}
        assert client.information_client.file_type == "json"
        assert client.information_client.timeout == 5

        assert client.release_client.endpoint == "series/release"
        assert client.release_client.params == {"series_id": "UNRATE"}
        assert client.release_client.file_type == "json"
        assert client.release_client.timeout == 5

        assert client.include_series_info is False
        assert client.include_series_release is False

    def test_fed_api_fed_funds_init(self, mock_api_key):
        """ Test the Federal Reserve API class initialization"""
        client = FederalReserveFederalFundsRate(
            api_key=mock_api_key,
            params={},
        )
        assert client.observations_client.endpoint == "series/observations"
        assert client.observations_client.params == {"series_id": "FEDFUNDS"}
        assert client.observations_client.file_type == "json"
        assert client.observations_client.timeout == 5

        assert client.information_client.endpoint == "series"
        assert client.information_client.params == {"series_id": "FEDFUNDS"}
        assert client.information_client.file_type == "json"
        assert client.information_client.timeout == 5

        assert client.release_client.endpoint == "series/release"
        assert client.release_client.params == {"series_id": "FEDFUNDS"}
        assert client.release_client.file_type == "json"
        assert client.release_client.timeout == 5

        assert client.include_series_info is False
        assert client.include_series_release is False

    def test_fed_api_gdp_init(self, mock_api_key):
        """ Test the Federal Reserve API class initialization"""
        client = FederalReserveGDP(
            api_key=mock_api_key,
            params={},
        )
        assert client.observations_client.endpoint == "series/observations"
        assert client.observations_client.params == {"series_id": "GDP"}
        assert client.observations_client.file_type == "json"
        assert client.observations_client.timeout == 5

        assert client.information_client.endpoint == "series"
        assert client.information_client.params == {"series_id": "GDP"}
        assert client.information_client.file_type == "json"
        assert client.information_client.timeout == 5

        assert client.release_client.endpoint == "series/release"
        assert client.release_client.params == {"series_id": "GDP"}
        assert client.release_client.file_type == "json"
        assert client.release_client.timeout == 5

        assert client.include_series_info is False
        assert client.include_series_release is False