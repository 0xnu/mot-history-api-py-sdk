import requests
import os

class CheckMOTAPI:
    base_url = "https://beta.check-mot.service.gov.uk/trade/vehicles/mot-tests"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_headers(self):
        return {"x-api-key": self.api_key}

    def make_request(self, url, params=None):
        headers = self.get_headers()
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()


class Registration(CheckMOTAPI):
    def get_data(self, registration):
        url = f"{self.base_url}?registration={registration}"
        return self.make_request(url)


class Page(CheckMOTAPI):
    def get_data(self, page):
        url = f"{self.base_url}?page={page}"
        return self.make_request(url)


class Date(CheckMOTAPI):
    def get_data(self, date, page):
        url = f"{self.base_url}?date={date}&page={page}"
        return self.make_request(url)


class VehicleID(CheckMOTAPI):
    def get_data(self, vehicle_id):
        url = f"{self.base_url}?vehicleId={vehicle_id}"
        return self.make_request(url)
