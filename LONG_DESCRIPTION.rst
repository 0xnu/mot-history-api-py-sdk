mot-history-api-py-sdk
======================

.. image:: https://badge.fury.io/py/mot-history-api-py-sdk.svg
    :target: https://badge.fury.io/py/mot-history-api-py-sdk
    :alt: MOT History API Python SDK

The SDK provides convenient access to the `MOT History API`_ functionality from applications written in the Python programming language.

.. _MOT History API: https://documentation.history.mot.api.gov.uk/


Requirements
------------

Python 2.7 and later.


Setup
------

You can install this package by using the pip tool and installing:

.. code-block:: bash

	pip install mot-history-api-py-sdk

Or:

.. code-block:: bash

	easy_install mot-history-api-py-sdk

Install from source with:

.. code-block:: bash

    python setup.py install --user

Or, `sudo python setup.py install` to install the package for all users.

Tests
------

Export environment variables:

.. code-block:: bash
    export MOT_CLIENT_ID=
    export MOT_CLIENT_SECRET=
    export MOT_API_KEY=

Now, you can execute this command: `python3 -m test`

Unset the environment variables after completing the tests:

.. code-block:: bash
    unset MOT_CLIENT_ID && unset MOT_CLIENT_SECRET && unset MOT_API_KEY

Developers/Engineers can run tests in two scenarios:

+ **With real credentials**: They set the environment variables, and the tests use the live API connection.

+ **Without credentials**: The tests run using a mock client, allowing basic functionality checks without a live API connection.

The flexibility supports real integration testing and quick, credential-free checks during development.

Request MOT History API Key
---------------------------

You can use this support form to request an `API Key`_.

.. _API Key: https://documentation.history.mot.api.gov.uk/mot-history-api/register


Using the MOT History API Key
-----------------------------

You can read the `API documentation`_ to understand what's possible with MOT History API Key. If you need further assistance, don't hesitate to `contact the DVSA`_.

.. _API documentation: https://documentation.history.mot.api.gov.uk/
.. _contact the DVSA: https://documentation.history.mot.api.gov.uk/mot-history-api/support

License
--------

This project is licensed under the `MIT License`_.

.. _MIT License: https://gist.github.com/0xnu/d11da49c85eeb7272517a9010bbdf1ab


Copyright
---------

Copyright |copy| 2023 - 2024 `Finbarrs Oketunji`_.

The MOT History API Python SDK is Licensed under the `Open Government Licence v3.0`_

.. |copy| unicode:: 0xA9 .. copyright sign
.. _Finbarrs Oketunji: https://finbarrs.eu
.. _Open Government Licence v3.0: https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
