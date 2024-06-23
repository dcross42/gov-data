""" Pull CPI data from FRED API """

from ..authentication import GovDataAPIKey
from .base import FederalReserveSeries


class FederalReserveCPI(FederalReserveSeries):
    """ Get CPI data from the FRED API """

    def __init__(
            self,
            api_key: GovDataAPIKey,
            params : dict,
            include_series_info : bool = False,
            include_series_release : bool = False,
            file_type : str = "json",
            timeout : int = 5):
        """ Initialize the Federal Reserve CPI class """
        super().__init__(
            api_key,
            'CPIAUCSL',
            params,
            include_series_info,
            include_series_release,
            file_type,
            timeout
        )

class FederalReservePCE(FederalReserveSeries):
    """ Get PCE data from the FRED API """

    def __init__(
            self,
            api_key: GovDataAPIKey,
            params : dict,
            include_series_info : bool = False,
            include_series_release : bool = False,
            file_type : str = "json",
            timeout : int = 5):
        """ Initialize the Federal Reserve CPI class """
        super().__init__(
            api_key,
            'PCEPI',
            params,
            include_series_info,
            include_series_release,
            file_type,
            timeout
        )
