import requests
#import os
#from dotenv import load_dotenv
import pprint

#load_dotenv()

url = "https://fakerapi.it/api/v1/custom?customfield1=name&customfield2=pokemon&customfield3=website&_quantity=10"

headers = {
    "content_type":"application/json",
}

response = requests.get(url, headers=headers)

pprint.pprint(response.json())