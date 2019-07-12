import urllib.request
from bs4 import BeautifulSoup


r = urllib.request.urlopen('http://www.habit.ru/35/177.html')
soup = BeautifulSoup(r.read(), features="lxml")
tables = soup.find_all('table', cellpadding="3")

elements = {}


for row in tables[0].find_all('tr')[2:]:
  elements[str(row.find('td').text)] = [float(str(row.find_all('th')[0].text).replace(',', '.').replace('–', '-'))*1000,
                                              float(str(row.find_all('th')[1].text).replace(',', '.').replace('–', '-')),
                                              float(str(row.find_all('th')[2].text).replace(',', '.').replace('–', '-'))*1000]
print(elements)

for row in tables[1].find_all('tr')[2:]:
  elements[str(row.find_all('td'))[5: -6]] = {'удельная теплоемкость': float(str(row.find_all('th')[0].text).replace(',', '.').replace('–', '-'))*1000,
                                              'темпиратура кипения': float(str(row.find_all('th')[1].text).replace(',', '.').replace('–', '-')),
                                              'удельная теплота парообразования': float(str(row.find_all('th')[2].text).replace(',', '.').replace('–', '-'))*1000000}
