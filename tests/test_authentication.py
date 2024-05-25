""" Test authentication module."""

import pytest

from gov_data.authentication import GovDataAPIKey


@pytest.fixture
def mock_env_api_key(monkeypatch):
    """ Mock the environment variable for the API key """
    monkeypatch.setenv("GOVDATA_test_API_KEY", "test_API_KEY")


class TestGovDataAPIKey:
    """ Test the GovDataAPIKey class """
    def test_gov_data_authentication_env(self, mock_env_api_key):
        """ Test the GovDataAPIKey class """
        api_key = GovDataAPIKey("test")
        assert api_key.get_api_key() == "test_API_KEY"

    def test_gov_data_authentication_arg(self):
        """ Test the GovDataAPIKey class """
        api_key = GovDataAPIKey(api_name="test", api_key="test_API_KEY")
        assert api_key.get_api_key() == "test_API_KEY"

    def test_gov_data_authentication_env_error(self, mock_env_api_key):
        """ Test the GovDataAPIKey class """
        with pytest.raises(ValueError):
            GovDataAPIKey("not_test")

    def test_gov_data_authentication_no_args_error(self):
        """ Test the GovDataAPIKey class """
        with pytest.raises(ValueError):
            GovDataAPIKey(None, None)