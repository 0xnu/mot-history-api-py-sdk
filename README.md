# MOT History API Python SDK

The SDK provides convenient access to the [MOT History API](https://dvsa.github.io/mot-history-api-documentation/) for applications written in the Python programming language.

## Requirements

Python 2.7 and later.

## Setup

You can install this package by using the pip tool and installing:

```python
pip install mot-history-api-py-sdk

## OR

easy_install mot-history-api-py-sdk
```

Install from source with:

```python
python setup.py install --user

## or `sudo python setup.py install` to install the package for all users
```

## Usage Example

```python
from motapi.motdata import *
from dotenv import load_dotenv
import os

api_key = "<your-api-key>" # your api key
registration = "ML58FOU" # example of a vehicle registration
page = 1 # pagination
date = "20230201" # date must be five weeks from the current date
vehicle_id = "<enter your vehicle id here>" # unique vehicle ID for vehicles that have had an MOT test

reg = Registration(api_key)
reg_data = reg.get_data(registration)
print(reg_data)

p = Page(api_key)
page_data = p.get_data(page)
print(page_data)

d = Date(api_key)
date_data = d.get_data(date, page)
print(date_data)

v = VehicleID(api_key)
vehicle_data = v.get_data(vehicle_id)
print(vehicle_data)
```

## Setting up a MOT History API

You can use this support form to request an [API Key](https://www.smartsurvey.co.uk/s/MOT_History_TradeAPI_Access_and_Support?).


## Using the MOT History API

You can read the [API documentation](https://dvsa.github.io/mot-history-api-documentation/) to understand what's possible with the MOT History API. If you need further assistance, don't hesitate to [contact the DVSA](https://www.smartsurvey.co.uk/s/MOT_History_TradeAPI_Access_and_Support?).


## License

This project is licensed under the [MIT License](./LICENSE).


## Copyright

(c) 2023 [Finbarrs Oketunji](https://finbarrs.eu).

The MOT History API Python SDK is Licensed under the [Open Government Licence v3.0](
https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)