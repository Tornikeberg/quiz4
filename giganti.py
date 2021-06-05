import requests
import bs4
import csv
from time import sleep
from random import randint

file = open('toksonnn.csv','w', encoding='UTF-8',newline='\n')
item = 1
file_obj = csv.writer(file)
file_obj.writerow(['model', 'price'])



while item < 6:
    url = f'https://gigant.ge/საყოფაცხოვრებო-ტექნიკა/მსხვილი-ტექნიკა/მაცივარი/page-{item}/'
    answer = requests.get(url)
    con = answer.text
    soup = bs4.BeautifulSoup(con, 'html.parser')
    all = soup.find('div', {'class': 'grid-list g_grid_list'})
    one = all.find_all('div', {'class': 'ty-column3'})
    for e in one:
        name = e.find('div', {'class': 'ty-grid-list__item-name'})
        last_name = name.a.text
        price = e.find('span', {'class': 'ty-price-num'})
        last_price = price.text
        file_obj.writerow([last_name,last_price])

    item+=1
    sleep(randint(15,20))
