#Python3
import requests,bs4
import csv
from bs4 import BeautifulSoup
page = requests.get('https://www.pharmaceuticalconferences.com/')
soup = BeautifulSoup(page.content, 'html.parser')
eventname = soup.find_all('h3')
eventinfo = soup.find_all('h3', class_='infoColumn')
eventdate = soup.find_all('h3', class_='dates')
eventlocation = soup.find_all('h3', class_='cityCountry')

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([eventname, eventinfo, eventdate, eventlocation)
close('index.csv')
