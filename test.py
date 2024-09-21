"""Test script for MOT Data API Client.

It tests all the main functionalities of the MOT Data API Client,
including handling various VIN lengths.
"""

import os
import sys
from pprint import pprint
from typing import Optional
from unittest.mock import Mock

# It attempts to import MOTDataClient
# but falls back to a mock if it is not present.
try:
    from motapi import MOTDataClient
except ImportError:
    MOTDataClient = Mock()

# Retrieve credentials from environment variables
CLIENT_ID: Optional[str] = os.environ.get("MOT_CLIENT_ID")
CLIENT_SECRET: Optional[str] = os.environ.get("MOT_CLIENT_SECRET")
API_KEY: Optional[str] = os.environ.get("MOT_API_KEY")

# Initialize the client
if all([CLIENT_ID, CLIENT_SECRET, API_KEY]):
    client = MOTDataClient(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        api_key=API_KEY
    )
else:
    print("Warning: Using mock client as credentials are not set.")
    client = Mock()
    # Setup mock responses
    client.get_vehicle_data.return_value = {"mock": "vehicle data"}
    client.get_bulk_download_info.return_value = {"mock": "bulk download info"}
    client.renew_client_secret.return_value = "mock_new_secret"

def test_get_vehicle_data_by_registration():
    """Test retrieving vehicle data by registration number."""
    print("\nTesting get_vehicle_data with a registration number:")
    try:
        data = client.get_vehicle_data("ML58FOU")
        print("Vehicle data retrieved:")
        pprint(data)
    except Exception as e:
        print(f"Error retrieving vehicle data: {e}")

def test_get_vehicle_data_by_vin():
    """Test retrieving vehicle data by VIN (17 characters)."""
    print("\nTesting get_vehicle_data with a 17-character VIN:")
    try:
        data = client.get_vehicle_data("WVWZZZ1JZXW000010")
        print("Vehicle data retrieved:")
        pprint(data)
    except Exception as e:
        print(f"Error retrieving vehicle data: {e}")

def test_get_vehicle_data_by_short_vin():
    """Test retrieving vehicle data by short VIN (5-13 characters)."""
    print("\nTesting get_vehicle_data with a short VIN:")
    try:
        data = client.get_vehicle_data("12345")  # 5-character VIN
        print("Vehicle data retrieved:")
        pprint(data)
    except Exception as e:
        print(f"Error retrieving vehicle data: {e}")

def test_get_bulk_download_info():
    """Test retrieving bulk download information."""
    print("\nTesting get_bulk_download_info:")
    try:
        data = client.get_bulk_download_info()
        print("Bulk download info retrieved:")
        pprint(data)
    except Exception as e:
        print(f"Error retrieving bulk download info: {e}")

def test_renew_client_secret():
    """Test renewing client secret."""
    print("\nTesting renew_client_secret:")
    try:
        new_secret = client.renew_client_secret("firstname.lastname@example.com")
        print(f"New client secret received: {new_secret[:5]}...")  # Print only first 5 chars for security
    except Exception as e:
        print(f"Error renewing client secret: {e}")

def test_invalid_vehicle_identifier():
    """Test handling of invalid vehicle identifier."""
    print("\nTesting invalid vehicle identifier:")
    try:
        client.get_vehicle_data("INVALID123!")
    except ValueError as e:
        print(f"Correctly raised ValueError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def test_edge_case_vins():
    """Test handling of edge case VINs."""
    print("\nTesting edge case VINs:")
    edge_cases = ["12345", "123456", "1234567890123", "12345678901234567"]
    for vin in edge_cases:
        try:
            data = client.get_vehicle_data(vin)
            print(f"Data retrieved for VIN {vin}:")
            pprint(data)
        except Exception as e:
            print(f"Error retrieving data for VIN {vin}: {e}")

if __name__ == "__main__":
    print("Starting MOT Data API Client tests...")

    test_get_vehicle_data_by_registration()
    test_get_vehicle_data_by_vin()
    test_get_vehicle_data_by_short_vin()
    test_get_bulk_download_info()
    test_renew_client_secret()
    test_invalid_vehicle_identifier()
    test_edge_case_vins()

    print("\nAll tests completed.")
