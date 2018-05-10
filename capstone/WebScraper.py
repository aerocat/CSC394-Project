from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.cdm.depaul.edu/academics/Pages/Current/Requirements-MS-in-Computer-Science.aspx')
content = r.content
soup = BeautifulSoup(content, "html5lib")
print(soup.prettify())