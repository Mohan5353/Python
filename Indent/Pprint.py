from pprint import pprint

my_dict = {"name": "John",
           "age": 30,
           "address": {"street": "Main Street",
                       "city": "Boston",
                       "state": "MA",
                       "zip": 12345},
           "contacts": {"123-456-7890",
                        "123-456-7891",
                        "123-456-7892"},
           "hobbies": ["basketball", "reading", "sleeping", "coding"]}
pprint(my_dict)

# Example 2

# import requests
#
#
# def get_geocode(address):
#     url = "https://maps.googleapis.com/maps/api/geocode/json"
#     resp = requests.get(url, params={"address": address})
#     return resp.json()
#
#
# out = get_geocode("Indian gate, New Delhi, India")
# pprint(out)
