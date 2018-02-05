#Python3
import requests, bs4, csv
from bs4 import BeautifulSoup
page = requests.get('https://www.pharmaceuticalconferences.com/')
soup = BeautifulSoup(page.content, 'html.parser')

with open('index.csv', 'a') as csv_file:  
        writer = csv.writer(csv_file)
        writer.writerow(['Subject', 'Start Date', 'Start Time','End Date',"End Time","All Day Event", 'Description', 'Location'])

h3 = soup.find_all("div", class_="col-md-4 col-sm-6 confer")

outfile = open('output.txt', 'a')

for div in h3:
    ename_box = div.find('h3')
    ename = ename_box.get_text()
    ename = ename[1:]
    einfo_box = div.find(class_='infoColumn')
    einfo = einfo_box.get_text()
    einfo = einfo[1:]
    edate_box = div.find(class_='dates')
    edate = edate_box.get_text()
    edate = edate[1:]
    elocale_box = div.find(class_='cityCountry')
    elocale = elocale_box.get_text()
    elocale = elocale[1:]
    
    
    Events = {'Event name':str(ename), 'location': str(elocale), 'date': str(edate)}
    outfile.write(str(Events))
    outfile.write("\n")

    with open('index.csv', 'a') as csv_file:  
        writer = csv.writer(csv_file)
        writer.writerow([ename, edate, "09:00", "","17:00", 'TRUE', 'https://www.pharmaceuticalconferences.com/', elocale])

outfile.close()
    