from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))
#html = urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, "html.parser")
innerurl=list()
# Retrieve all of the anchor tags
print(f"Retrieving:{url}")
for i in range(count):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    for tag in tags:
        innerurl.append(tag.get('href', None))
    print(f"Retrieving:{innerurl[position-1]}")
    url=innerurl[position-1]
    innerurl.clear()
