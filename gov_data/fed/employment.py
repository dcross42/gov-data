""" Handlers for pulling Employment data from the Fed API """

import pandas as pd

from ..authentication import GovDataAPIKey
from .fed import FederalReserveAPI


class FederalReserveUnemployment(FederalReserveAPI):
    """ Make requests to Federal Reserve Observations API for Unemployment data """

    def __init__(
            self,
            api_key: GovDataAPIKey,
            params : dict,
            file_type : str = "json",
            timeout : int = 5):
        params['series_id'] = 'UNRATE'
        super().__init__(api_key, 'series/observations', params, file_type, timeout)
        self.params = params

    def get_dataframe(self) -> pd.DataFrame:
        """ Return a DataFrame with the Unemployment data """
        data = self.get_data()
        df = pd.DataFrame(data['observations'])
        df['date'] = pd.to_datetime(df['date'])
        df['value'] = df['value'].astype(float)
        df['units'] = data['units']
        return df
