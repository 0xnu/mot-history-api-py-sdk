"""MOT Data API Client package.

The package allows a client to interact with the MOT History API.
It requires a client ID, client secret, and API key for authentication.
"""

from .motdata import MOTDataClient, VehicleData, BulkData, CredentialsManager, MOTHistoryAPI

__all__ = [
    "MOTDataClient",
    "VehicleData",
    "BulkData",
    "CredentialsManager",
    "MOTHistoryAPI"
]

__version__ = "1.0.0"
