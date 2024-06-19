""" Pull data on Interest Rates from the Federal Reserve API """
from ..authentication import GovDataAPIKey
from .base import FederalReserveSeries


class FederalReserveFederalFundsRate(FederalReserveSeries):
    """ Make requests to Federal Reserve Observations API for Federal Funds Rate data """

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
            'FEDFUNDS',
            params,
            include_series_info,
            include_series_release,
            file_type,
            timeout
        )
