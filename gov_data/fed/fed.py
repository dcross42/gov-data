"""
Class to handle requests to Federal Reserve API (FRED)
"""
import requests

from ..authentication import GovDataAPIKey
from ..base import BaseGovDataAPI

ENDPOINTS = {
    'category' : ['category_id'],
    'category/children' : ['category_id', 'realtime_start', 'realtime_end'],
    'category/related' : ['category_id', 'realtime_start', 'realtime_end'],
    'category/series' : [
        'category_id', 'realtime_start', 'realtime_end', 
        'limit', 'offset', 'order_by', 'sort_order', 
        'filter_variable', 'filter_value', 'tag_names', 
        'exclude_tag_names'
    ],
    'category/tags' : [
        'category_id', 'realtime_start', 'realtime_end', 
        'tag_names', 'tag_group_id', 'search_text', 
        'limit', 'offset', 'order_by', 
        'sort_order'
    ],
    'category/related_tags' : [
        'category_id', 'realtime_start', 'realtime_end', 
        'tag_names', 'exclude_tag_names', 'tag_group_id', 
        'search_text', 'limit', 'offset', 'order_by', 
        'sort_order'
    ],
    'releases' : ['realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order'],
    'releases/dates' : [
        'realtime_start', 'realtime_end', 'limit', 
        'offset', 'order_by', 'sort_order', 
        'include_release_dates_with_no_data'
    ],
    'release' : ['release_id', 'realtime_start', 'realtime_end'],
    'release/dates' : [
        'release_id', 'realtime_start', 'realtime_end', 
        'limit', 'offset', 'sort_order', 
        'include_release_dates_with_no_data'
    ],
    'release/series' : [
        'release_id', 'realtime_start', 'realtime_end', 
        'limit', 'offset', 'order_by', 'sort_order', 
        'filter_variable', 'filter_value', 'tag_names', 
        'exclude_tag_names'
    ],
    'release/sources' : ['release_id', 'realtime_start', 'realtime_end'],
    'release/tags' : [
        'release_id', 'realtime_start', 'realtime_end', 
        'tag_names', 'tag_group_id', 'search_text', 
        'limit', 'offset', 'order_by', 
        'sort_order'
    ],
    'release/related_tags' : [
        'release_id', 'realtime_start', 'realtime_end', 
        'tag_names', 'exclude_tag_names', 'tag_group_id', 
        'search_text', 'limit', 'offset', 
        'order_by', 'sort_order'
    ],
    'release/tables' : [
        'release_id', 'element_id', 'include_observation_values', 
        'observation_date'
    ],
    'series' : ['series_id', 'realtime_start', 'realtime_end'],
    'series/categories' : ['series_id', 'realtime_start', 'realtime_end'],
    'series/observations' : [
        'series_id', 'realtime_start', 'realtime_end', 
        'limit', 'offset', 'sort_order', 
        'observation_start', 'observation_end', 'units', 
        'frequency', 'aggregation_method', 'output_type', 
        'vintage_dates'
    ],
    'series/release' : ['series_id', 'realtime_start', 'realtime_end'],
    'series/search' : [
        'search_text', 'search_type', 'realtime_start', 
        'realtime_end', 'limit', 'offset', 
        'order_by', 'sort_order', 'filter_variable', 
        'filter_value', 'tag_names', 'exclude_tag_names'
    ],
    'series/search/tags' : [
        'series_search_text', 'realtime_start', 'realtime_end', 
        'tag_names', 'tag_group_id', 'tag_search_text', 
        'limit', 'offset', 'order_by', 
        'sort_order'
    ],
    'series/search/related_tags' : [
        'series_search_text', 'realtime_start', 'realtime_end', 
        'tag_names', 'exclude_tag_names', 'tag_group_id', 
        'tag_search_text', 'limit', 'offset', 
        'order_by', 'sort_order'
    ],
    'series/tags' : [
        'series_id', 'realtime_start', 'realtime_end', 'order_by', 'sort_order'],
    'series/updates' : [
        'realtime_start', 'realtime_end', 'limit', 
        'offset', 'filter_value', 'start_time', 
        'end_time'
    ],
    'series/vintagedates' : [
        'series_id', 'realtime_start', 'realtime_end', 'limit', 'offset', 'sort_order'],
    'sources' : ['realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order'],
    'source' : ['source_id', 'realtime_start', 'realtime_end'],
    'source/releases' : [
        'source_id', 'realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order'],
    'tags' : [
        'realtime_start', 'realtime_end', 'tag_names', 
        'tag_group_id', 'search_text', 'limit', 
        'offset', 'order_by', 'sort_order'
    ],
    'related_tags' : [
        'realtime_start', 'realtime_end', 'tag_names', 
        'exclude_tag_names', 'tag_group_id', 'search_text', 
        'limit', 'offset', 'order_by', 
        'sort_order'
    ],
    'tags/series' : [
        'tag_names', 'exclude_tag_names', 'realtime_start', 
        'realtime_end', 'limit', 'offset', 
        'order_by', 'sort_order'
    ],
}


class FederalReserveAPI(BaseGovDataAPI):
    """ Class to handle requests to Federal Reserve API (FRED) """
    def __init__(
            self,
            api_key : GovDataAPIKey,
            endpoint: str,
            params: dict,
            file_type : str = "json",
            timeout : int = 5):
        """ Initialize the API Connector with endpoint, file type, and parameters """
        super().__init__(api_key)
        # Set Base URL
        self._base_url = "https://api.stlouisfed.org/fred"
        # Validate endpoint argument and set endpoint
        if endpoint not in ENDPOINTS:
            raise ValueError(f"Invalid endpoint: {endpoint}")
        self.endpoint = endpoint
        # Validate params argument and set params 
        for key, _ in params.items():
            if key not in ENDPOINTS[endpoint]:
                raise ValueError(f"Invalid parameter for {endpoint}: {key}")
        self.params = params
        # Validate file_type argument and set file_type
        if file_type not in ["json", "xml"]:
            raise ValueError(f"Invalid file type: {file_type}")
        self.file_type = file_type

        # Validate and set timeout
        if not isinstance(timeout, int) or timeout < 0:
            raise ValueError("Timeout must be a positive integer")
        self.timeout = timeout


    @property
    def base_url(self):
        """ Base URL for the API"""
        return self._base_url

    def build_url(self):
        """ Build the URL to interact with the API """
        compiled_url = f"{self.base_url}/{self.endpoint}"
        compiled_url = f"{compiled_url}?api_key={self.api_key}&file_type={self.file_type}"
        for key, value in self.params.items():
            compiled_url += f"&{key}={value}"
        return compiled_url

    def get_data(self):
        """ Get data from the API """
        url = self.build_url()
        response = requests.get(url, timeout=self.timeout)
        if response.status_code != 200:
            error = f"Request failed with status code: {response.status_code}: {response.reason}"
            raise ValueError(error)
        return response.json()
