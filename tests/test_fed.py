""" 
Test the Fed API Connector
"""

import pytest

from gov_data.authentication import GovDataAPIKey
from gov_data.fed.base import FederalReserveAPI
from gov_data.fed.employment import (FederalReserveLaborForceParticipation,
                                     FederalReserveUnemployment)
from gov_data.fed.exchange_rates import FederalReserveDollarIndex
from gov_data.fed.interest_rates import (FederalReserve10YR2YRTreasurySpread,
                                         FederalReserve10YR3YRTreasurySpread,
                                         FederalReserve30YRFixedMortgageRate,
                                         FederalReserveFederalFundsRate)
from gov_data.fed.monetary import (
    FederalReserveM2, FederalReserveOvernightReserveRepurchaseAgreements,
    FederalReserveTotalAssets)
from gov_data.fed.national_accounts import (FederalReserveDebtToGDPRatio,
                                            FederalReserveFederalDebt,
                                            FederalReserveFederalDeficit,
                                            FederalReserveGDP)
from gov_data.fed.prices import FederalReserveCPI, FederalReservePCE


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

    series_test_data = [
        (FederalReserveCPI, {}, "CPIAUCSL"),
        pytest.param(FederalReserveCPI, {}, "", marks=pytest.mark.xfail),
        (FederalReservePCE, {}, "PCEPI"),
        (FederalReserveUnemployment, {}, "UNRATE"),
        (FederalReserveLaborForceParticipation, {}, "CIVPART"),
        (FederalReserveGDP, {}, "GDP"),
        (FederalReserveFederalDebt, {}, "GFDEBTN"),
        (FederalReserveDebtToGDPRatio, {}, "GFDEGDQ188S"),
        (FederalReserveFederalFundsRate, {}, "FEDFUNDS"),
        (FederalReserve10YR2YRTreasurySpread, {}, "T10Y2Y"),
        (FederalReserve10YR3YRTreasurySpread, {}, "T10Y3M"),
        (FederalReserve30YRFixedMortgageRate, {}, "MORTGAGE30US"),
        (FederalReserveDollarIndex, {}, "DTWEXBGS"),
        (FederalReserveTotalAssets, {}, "WALCL"),
        (FederalReserveM2, {}, "M2SL"),
        (FederalReserveOvernightReserveRepurchaseAgreements, {}, "RRPONTSYD")
    ]
    @pytest.mark.parametrize(
        "fed_client, params, series_id", series_test_data       
    )
    def test_series_endpoints(self, fed_client, params, series_id, mock_api_key):
        """ Test Federal Reserve Series derived classes """
        client = fed_client(
            api_key=mock_api_key,
            params=params,
        )

        assert client.observations_client.endpoint == "series/observations"
        assert client.observations_client.params == {"series_id": series_id}
        assert client.observations_client.file_type == "json"
        assert client.observations_client.timeout == 5

        assert client.information_client.endpoint == "series"
        assert client.information_client.params == {"series_id": series_id}
        assert client.information_client.file_type == "json"
        assert client.information_client.timeout == 5

        assert client.release_client.endpoint == "series/release"
        assert client.release_client.params == {"series_id": series_id}
        assert client.release_client.file_type == "json"
        assert client.release_client.timeout == 5

        assert client.include_series_info is False
        assert client.include_series_release is False
