""" Classes to pull Exchange Rate data from the Federal Reserve API. """

from ..authentication import GovDataAPIKey
from .base import FederalReserveSeries


class FederalReserveDollarIndex(FederalReserveSeries):
    """ Make requests to Federal Reserve API for Nominal Broad US Dollar Index """
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
            'DTWEXBGS',
            params,
            include_series_info,
            include_series_release,
            file_type,
            timeout
        )
