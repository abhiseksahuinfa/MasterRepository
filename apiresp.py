import requests
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url,context=ctx)
response.json()
