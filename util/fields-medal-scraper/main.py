import csv
import requests
from bs4 import BeautifulSoup
import os

def obtain_data():
    url = "https://stats.areppim.com/listes/list_fieldsxmedal.htm"
    url = requests.get(url)
    base = BeautifulSoup(url.content, "html.parser")
    get_fields_medal_year(base)

    url = "https://www.mathunion.org/imu-awards/fields-medal"
    url = requests.get(url)
    base = BeautifulSoup(url.content, "html.parser")
    get_fields_medal(base)

def get_fields_medal_year(base):
    skip = False
    dirty_data = []
    base_data = base.select("tr > td")
    for text in base_data:
        text = text.text
        if text.isdigit():
            dirty_data.append(text)
    for text in dirty_data:
        if not skip:
            awarded.append(text)
            skip = True
            continue
        if skip:
            skip = False
            continue

def get_fields_medal(base):
    for item in base.find_all('li', class_='blue-link'):
        item = item.text
        item = item.replace('Fields Medals', '')
        for char in item:
            if char.isdigit():
                item = item.replace(char, '')
        recipient.append(item)

def merge(recipient, awarded):
    final_result = [(recipient[i], awarded[i]) for i in range(0, len(recipient))]
    return final_result

def create_csv(recipient, awarded):
    row_name = ['Name', 'Year']
    with open('fields-medal.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(row_name)
        write.writerows(merge(recipient, awarded))

if __name__ == "__main__":
    recipient, awarded = [], []
    obtain_data()
    create_csv(recipient, awarded)

    try:
        SOME_SECRET = os.environ["SOME_SECRET"]
    except KeyError:
        SOME_SECRET = "Token not available!"
