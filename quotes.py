import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(page.content, 'html.parser')
quotes = soup.find_all(class_='quote')

print(quotes[0].find(class_='author').get_text())
print(quotes[0].find(class_='text').get_text())

names = [item.find(class_='author').get_text() for item in quotes]
words = [item.find(class_='text').get_text() for item in quotes]
print(names)
print(words)

table = pd.DataFrame(
    {
        'Author': names,
        'Quote': words,
    })

print(table)

table.to_csv('quotes.csv')