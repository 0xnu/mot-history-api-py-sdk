mot-history-api-py-sdk
======================

.. image:: https://badge.fury.io/py/mot-history-api-py-sdk.svg
    :target: https://badge.fury.io/py/mot-history-api-py-sdk
    :alt: MOT History API Python SDK

The SDK provides convenient access to the `MOT History API`_ functionality from applications written in the Python programming language.

.. _MOT History API: https://dvsa.github.io/mot-history-api-documentation/


Requirements
------------

Python 2.7 and later.


Setup
------

You can install this package by using the pip tool and installing:

.. code-block:: bash

	$ pip install mot-history-api-py-sdk

Or:

.. code-block:: bash

	$ easy_install mot-history-api-py-sdk


Usage Example
-------------

.. code-block:: python

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


Request MOT History API Key
---------------------------

You can use this support form to request an `API Key`_.

.. _API Key: https://www.smartsurvey.co.uk/s/MOT_History_TradeAPI_Access_and_Support?


Using the MOT History API Key
-----------------------------

You can read the `API documentation`_ to understand what's possible with MOT History API Key. If you need further assistance, don't hesitate to `contact the DVSA`_.

.. _API documentation: https://dvsa.github.io/mot-history-api-documentation/
.. _contact the DVSA: https://www.smartsurvey.co.uk/s/MOT_History_TradeAPI_Access_and_Support?

License
--------

This project is licensed under the `MIT License`_.  

.. _MIT License: https://gist.github.com/0xnu/d11da49c85eeb7272517a9010bbdf1ab


Copyright
---------

Copyright |copy| 2023 `Finbarrs Oketunji`_.

The MOT History API Python SDK is Licensed under the `Open Government Licence v3.0`_

.. |copy| unicode:: 0xA9 .. copyright sign
.. _Finbarrs Oketunji: https://www.gov.uk/dvsa
.. _Open Government Licence v3.0: https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/