import requests

#from dotenv import load_dotenv
import pprint

#load_dotenv()

url = "https://fakerapi.it/api/v1/credit_cards?_quantity=60&_local=es_ES"

headers = {
    "content_type":"application/json",
}

response = requests.get(url, headers=headers)

pprint.pprint(response.json())