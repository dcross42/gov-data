""" Handlers for pulling Employment data from the Fed API """
from ..authentication import GovDataAPIKey
from .base import FederalReserveSeries


class FederalReserveUnemployment(FederalReserveSeries):
    """ Make requests to Federal Reserve Observations API for Unemployment data """

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
            'UNRATE',
            params,
            include_series_info,
            include_series_release,
            file_type,
            timeout
        )

class FederalReserveLaborForceParticipation(FederalReserveSeries):
    """ Make requests to Federal Reserve Observations API for Labor Force Participation data """

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
            'CIVPART',
            params,
            include_series_info,
            include_series_release,
            file_type,
            timeout
        )
