""" Classes to pull Monetary data from the Federal Reserve API. """

from ..authentication import GovDataAPIKey
from .base import FederalReserveSeries


class FederalReserveTotalAssets(FederalReserveSeries):
    """ Make requests to Federal Reserve Observations API for Total Assets data """
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
            'WALCL',
            params,
            include_series_info,
            include_series_release,
            file_type,
            timeout
        )

class FederalReserveM2(FederalReserveSeries):
    """ Make requests to Federal Reserve Observations API for M2 data """
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
            'M2SL',
            params,
            include_series_info,
            include_series_release,
            file_type,
            timeout
        )

class FederalReserveOvernightReserveRepurchaseAgreements(FederalReserveSeries):
    """ Make requests to Federal Reserve Observations API for Overnight Reverse Repurchase Agreements data """
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
            'RRPONTSYD',
            params,
            include_series_info,
            include_series_release,
            file_type,
            timeout
        )
