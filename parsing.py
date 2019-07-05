import urllib.request
from bs4 import BeautifulSoup


r = urllib.request.urlopen('http://www.habit.ru/35/177.html')
soup = BeautifulSoup(r.read(), features = "lxml")
tables = soup.find_all('table', cellpadding="3")

elements = {}

for row in tables[0].find_all('tr')[2:]:
  elements[str(row.find_all('td'))[5: -6]] = {'удельная теплоемкость': float(str(row.find_all('th')[0])[4: -5].replace(',', '.').replace('–', '-')),
                                              'темпиратура плавления': float(str(row.find_all('th')[1])[4: -5].replace(',', '.').replace('–', '-')),
                                              'удельная теплоа плавления': float(str(row.find_all('th')[2])[4: -5].replace(',', '.').replace('–', '-'))}

for row in tables[1].find_all('tr')[2:]:
  elements[str(row.find_all('td'))[5: -6]] = {'удельная теплоемкость': float(str(row.find_all('th')[0])[4: -5].replace(',', '.').replace('–', '-')),
                                              'темпиратура кипения': float(str(row.find_all('th')[1])[4: -5].replace(',', '.').replace('–', '-')),
                                              'удельная теплота парообразования': float(str(row.find_all('th')[2])[4: -5].replace(',', '.').replace('–', '-'))}
