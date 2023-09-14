import requests

url = 'https://intranet.rguktn.ac.in/SMS/'
usr_name = "N200125"
usr_pass = '8TU89'
print(requests.get(url, auth=(usr_name, usr_pass)).content)
