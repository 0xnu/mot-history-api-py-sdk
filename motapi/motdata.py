"""MOT Data API Client for interacting with the MOT history API."""

from typing import Dict, Optional
from .ratelimit import limits, sleep_and_retry, RateLimitExceeded
import requests
import time

class MOTHistoryAPI:
    """Base class for interacting with the MOT history API."""

    BASE_URL = "https://history.mot.api.gov.uk/v1/trade/vehicles"
    TOKEN_URL = "https://login.microsoftonline.com/a455b827-244f-4c97-b5b4-ce5d13b4d00c/oauth2/v2.0/token"
    SCOPE_URL = "https://tapi.dvsa.gov.uk/.default"

    # Rate Limiting
    QUOTA_LIMIT = 500000  # Maximum number of requests per day
    BURST_LIMIT = 10  # Maximum number of requests in a short burst
    RPS_LIMIT = 15  # Average number of requests per second

    def __init__(self, client_id: str, client_secret: str, api_key: str):
        """
        Initialise the MOT History API client.

        Args:
            client_id (str): The client ID for authentication.
            client_secret (str): The client secret for authentication.
            api_key (str): The API key for authentication.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_key = api_key
        self.access_token = self._get_access_token()
        self.request_count = 0
        self.last_request_time = time.time()

    def _get_access_token(self) -> str:
        """
        Obtain an access token from the OAuth2 endpoint.

        Returns:
            str: The access token.

        Raises:
            requests.exceptions.HTTPError: If the token request fails.
        """
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": self.SCOPE_URL,
        }
        response = requests.post(self.TOKEN_URL, data=data)
        response.raise_for_status()
        return response.json()["access_token"]

    def _get_headers(self) -> Dict[str, str]:
        """
        Generate headers for API requests.

        Returns:
            Dict[str, str]: Headers for API requests.
        """
        return {
            "Authorization": f"Bearer {self.access_token}",
            "X-API-Key": self.api_key,
        }

    @sleep_and_retry
    @limits(calls=BURST_LIMIT, period=1)
    @limits(calls=QUOTA_LIMIT, period=86400)
    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Make a GET request to the API with rate limiting.

        Args:
            endpoint (str): The API endpoint.
            params (Optional[Dict]): Query parameters for the request.

        Returns:
            Dict: JSON response from the API.

        Raises:
            requests.exceptions.HTTPError: If the API request fails.
            RateLimitExceeded: If the rate limit is exceeded.
        """
        # RPS Limiting
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < 1 / self.RPS_LIMIT:
            sleep_time = (1 / self.RPS_LIMIT) - time_since_last_request
            raise RateLimitExceeded("RPS limit exceeded", sleep_time)

        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()

        self.request_count += 1
        self.last_request_time = time.time()

        return response.json()

class VehicleData(MOTHistoryAPI):
    """Class for retrieving vehicle data."""

    def get_by_registration(self, registration: str) -> Dict:
        """
        Get MOT tests for a single vehicle by registration number.

        Args:
            registration (str): Vehicle registration number.

        Returns:
            Dict: Vehicle data including MOT tests.
        """
        return self._make_request(f"registration/{registration}")

    def get_by_vin(self, vin: str) -> Dict:
        """
        Get MOT tests for a single vehicle by VIN.

        Args:
            vin (str): Vehicle Identification Number.

        Returns:
            Dict: Vehicle data including MOT tests.
        """
        return self._make_request(f"vin/{vin}")

class BulkData(MOTHistoryAPI):
    """Class for retrieving bulk MOT history data."""

    def get_bulk_download(self) -> Dict:
        """
        Get MOT history data in bulk.

        Returns:
            Dict: Bulk and delta file information.
        """
        return self._make_request("bulk-download")

class CredentialsManager(MOTHistoryAPI):
    """Class for managing API credentials."""

    def renew_client_secret(self, email: str) -> str:
        """
        Request a new client secret.

        Args:
            email (str): Email address associated with the account.

        Returns:
            str: New client secret.

        Raises:
            requests.exceptions.HTTPError: If the API request fails.
        """
        url = f"{self.BASE_URL.rsplit('/', 1)[0]}/credentials"
        data = {
            "awsApiKeyValue": self.api_key,
            "email": email,
        }
        response = requests.put(url, headers=self._get_headers(), json=data)
        response.raise_for_status()
        return response.json()["clientSecret"]

class MOTDataClient:
    """Main client class for interacting with the MOT history API."""

    def __init__(self, client_id: str, client_secret: str, api_key: str):
        """
        Initialise the MOT Data Client.

        Args:
            client_id (str): The client ID for authentication.
            client_secret (str): The client secret for authentication.
            api_key (str): The API key for authentication.
        """
        self.vehicle_data = VehicleData(client_id, client_secret, api_key)
        self.bulk_data = BulkData(client_id, client_secret, api_key)
        self.credentials_manager = CredentialsManager(client_id, client_secret, api_key)

    def get_vehicle_data(self, identifier: str) -> Dict:
        """
        Get vehicle data by registration number or VIN.

        Args:
            identifier (str): Vehicle registration number or VIN.

        Returns:
            Dict: Vehicle data including MOT tests.

        Raises:
            ValueError: If the identifier is not a valid registration number or VIN.
        """
        identifier = identifier.strip().upper()

        # Check if the identifier is a VIN
        if 5 <= len(identifier) <= 17 and identifier.isalnum():
            return self.vehicle_data.get_by_vin(identifier)

        # Check if the identifier is a registration number
        if len(identifier) <= 8 and all(c.isalnum() or c.isspace() for c in identifier):
            return self.vehicle_data.get_by_registration(identifier)

        raise ValueError("Invalid identifier. Please provide a valid registration number or VIN.")

    def get_bulk_download_info(self) -> Dict:
        """
        Get bulk download file information.

        Returns:
            Dict: Bulk and delta file information.
        """
        return self.bulk_data.get_bulk_download()

    def renew_client_secret(self, email: str) -> str:
        """
        Request a new client secret.

        Args:
            email (str): Email address associated with the account.

        Returns:
            str: New client secret.
        """
        return self.credentials_manager.renew_client_secret(email)
