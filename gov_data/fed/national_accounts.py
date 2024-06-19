""" Pull data relating to National Accounts from FED API"""
from ..authentication import GovDataAPIKey
from .base import FederalReserveSeries


class FederalReserveGDP(FederalReserveSeries):
    """ Make requests to Federal Reserve Observations API for GDP data """

    def __init__(
            self,
            api_key: GovDataAPIKey,
            params : dict,
            include_series_info: bool = False,
            include_series_release: bool = False,
            file_type : str = "json",
            timeout : int = 5):
        super().__init__(
            api_key,
            'GDP',
            params,
            include_series_info,
            include_series_release,
            file_type,
            timeout
        )
