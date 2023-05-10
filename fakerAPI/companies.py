import requests
#import os
#from dotenv import load_dotenv
import pprint

#load_dotenv()

url = "https://fakerapi.it/api/v1/companies?_quantity=20"

headers = {
    "content_type":"application/json",
}

response = requests.get(url, headers=headers)

pprint.pprint(response.json())