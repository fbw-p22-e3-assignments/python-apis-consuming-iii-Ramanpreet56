import requests
#import os
#from dotenv import load_dotenv
import pprint

#load_dotenv()

url = "https://fakerapi.it/api/v1/persons?_quantity=50&_birthday_start=1994-01-01"

headers = {
    "content_type":"application/json",
}

response = requests.get(url, headers=headers)

pprint.pprint(response.json())