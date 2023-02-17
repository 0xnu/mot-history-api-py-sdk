from motapi.motdata import *

api_key = "<your-api-key>" # your api key
registration = "ML58FOU" # example of a vehicle registration
page = 1 # pagination
date = "20230201" # date must be five weeks from the current date
vehicle_id = "<enter your vehicle id here>" # unique vehicle id for vehicles that have had an MOT test

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
