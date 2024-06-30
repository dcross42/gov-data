# GovData

## Project Description

The goal of this project is to create a centralized package to access a wide variety of US Govenment APIs. The project has classes that make it easy to pull data from an API and get the data back in a pandas DataFrame. 

This project relies on requests and pandas under the hood. The classes are based on publicly available documentation for the APIs that are implemented. 

## Installation

**TODO**

## User Guide

### Authentication

In order to simplify and standardize how classes authenticate, the project implements a `GovDataAPIKey` class. Each API class requires a `GovDataAPIKey` object in order to make requests.

There are two ways to authenticate with `GovDataAPIKey`:

1. **Environment Variables**

In this scenario, the user must store the API key as an environment variable named GOVDATA_<API_NAME>_API_KEY. Then when creating the `GovDataAPIKey` object, the `api_name` argument must be the same as the value of <API_NAME>.

For example: 
``` bash
export GOVDATA_FED_API_KEY=abcdefg1234
```
``` python
from gov_data.authentication import GovDataAPIKey

api_key = GovDataAPIKey(api_name='FED')
```

2. API Key as Argument

In this scenario, the user must provide the API key as a string with the `api_key` argument. In this scenario, the `api_name` argument should be left blank. 
**Users should beware of storing their API Keys in version control, as that is insecure.**

``` python
from gov_data.authentication import GovDataAPIKey

api_key = GovDataAPIKey(api_key='abcd1234')
```

### Federal Reserve Data

There are several ways this project allows users to access Federal Reserve Data from the St. Louis Fed's [FRED API](https://fred.stlouisfed.org/docs/api/fred/).

#### High-Level API
The easiest way is to use one of the pre-built classes for specific datasets, like `FederalReserveCPI` to access CPI data.

The high-level API returns data from the 'series/observations' API. It also allows users to attach metadata about the series and most recent release.

These classes accept the following arguments:

1. `GovDataAPIKey` api_key: Valid API Key for the FRED API
2. `params`: Dictionary of parameters to the specific API, typically a `realtime_start` and `realtime_end` date range (specifics depend on the API, see the FRED Docs).
3. `include_series_info` : Boolean flag indicating whether you want to query the 'series' API
4. `include_series_release`
5. `file_type` : return type of the data. FRED allows JSON and XML. **XML NOT CURRENTLY IMPLEMENTED**
6. `timeout` : timeout for the FRED API

The following example will return the entirety of the CPI dataset available from the FRED API with all metadata attached.

``` python
from gov_data.fed.prices import FederalReserveCPI

client = FederalReserveCPI(
    api_key=api_key, 
    params={},
    include_series_info=True,
    include_series_release=True
)

df = client.get_data()
```

df will be a pandas DataFrame. The metadata about the series and the most recent release are stored in `df.attrs`.

#### Mid-Level API

The High-Level APIs rely on calls to mid-Level APIs.

The mid-level APIs are `FederalReserveSeries`, `FederalReserveSeriesObservations`, `FederalReserveSeriesInformation`, `FederalReserveSeriesRelease`. 

`FederalReserveSeries` takes a `series_id`, `params`, and two flags to return observations, series information, and series releases from the FRED API. The class allows any arbitrary `series_id` that exists in the FRED system. It relies on the other 3 classes to build the dataset that is returned.

`FederalReserveSeriesObservations` pulls the actual observations data from the FRED system. If you just want the data from a series, this class will return it.

`FederalReserveSeriesInformation` pulls the metadata about the data like the name of the dataset, a description, etc.

`FederalReserveSeriesRelease` pulls the metadata about the release of the data, which is the specific update to the data, typically on a monthly or quarterly cadence depending on the data.

The parameters to these classes follow the same paradigm as the high-level API.

#### Low-Level API

All of the above APIs rely on the `FederalReserveAPI` which inherits from the `BaseGovDataAPI`. This class wraps calls to the FRED API. The mid-level and high-level APIs are currently focussed on series data. If you want to pull other kinds of information from FRED, use this class to call all the different endpoints of the FRED API.

To see a full list of FRED endpoints, you can either go to the FRED API docs or see the list in the base.py file in the fed folder.

## Credit

All credit really goes to the teams of engineers, statisticians, and scientists that make this data available for public use.