from bs4 import BeautifulSoup
import requests

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

url = 'https://www.nationalgeographic.com/animals/mammals/facts/cabybara-facts'
response = requests.get(url)
content = response.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')
list = soup.find_all('p')

print(list)


# url ='https:..www.google.com'
# res = requests.get(url)
# print (res)

# with open('index.html') as fp:
#     soup = BeautifulSoup(fp)

# soup = BeautifulSoup("<html>data</html>")