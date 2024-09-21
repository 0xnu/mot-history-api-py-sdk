## MOT History API Python SDK

[![PyPI version](https://badge.fury.io/py/mot-history-api-py-sdk.svg)](https://badge.fury.io/py/mot-history-api-py-sdk)

The SDK provides convenient access to the [MOT History API](https://documentation.history.mot.api.gov.uk/) for applications written in the Python programming language.

### Requirements

Python 2.7 and later.

### Setup

You can install this package by using the pip tool and installing:

```python
pip install mot-history-api-py-sdk

## OR ##

easy_install mot-history-api-py-sdk
```

Install from source with:

```python
python setup.py install --user

## or `sudo python setup.py install` to install the package for all users
```

### Tests

Export environment variables:

```sh
export MOT_CLIENT_ID=
export MOT_CLIENT_SECRET=
export MOT_API_KEY=
```

Now, you can execute this command: `python3 -m test`

Unset the environment variables after completing the tests:

```sh
unset MOT_CLIENT_ID && unset MOT_CLIENT_SECRET && unset MOT_API_KEY
```

Developers/Engineers can run tests in two scenarios:

+ **With real credentials**: They set the environment variables, and the tests use the live API connection.

+ **Without credentials**: The tests run using a mock client, allowing basic functionality checks without a live API connection.

The flexibility supports real integration testing and quick, credential-free checks during development.

### Setting up a MOT History API

You can use this support form to request an [API Key](https://documentation.history.mot.api.gov.uk/mot-history-api/register).


### Using the MOT History API

You can read the [API documentation](https://documentation.history.mot.api.gov.uk/) to understand what's possible with the MOT History API. If you need further assistance, don't hesitate to [contact the DVSA](https://documentation.history.mot.api.gov.uk/mot-history-api/support).


### License

This project is licensed under the [MIT License](./LICENSE).


### Copyright

(c) 2023 - 2024 [Finbarrs Oketunji](https://finbarrs.eu).

The MOT History API Python SDK is Licensed under the [Open Government Licence v3.0](
https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
