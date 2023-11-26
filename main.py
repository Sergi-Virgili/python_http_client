import os
from dotenv import load_dotenv
import requests

load_dotenv()


response = requests.get(os.getenv('ENDPOINT'))

# print(response.text)