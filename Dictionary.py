import requests
from bs4 import BeautifulSoup

#Rudementary dictionary python
word = input('What word do you want to search up?: ')
url = 'https://www.dictionary.com/browse/'+word
req = requests.get(url)

data = BeautifulSoup(req.text, 'lxml')
temp_definition = data.findAll('meta', content=True, limit=1)
definition_ = str(temp_definition[0])

print(definition_[33::])
