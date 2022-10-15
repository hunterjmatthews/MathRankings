import csv
import requests
from bs4 import BeautifulSoup
import os
import re

def obtain_data():
    base_url = "http://www.ams.org/cgi-bin/fellows/fellows.cgi"
    base_url = requests.get(base_url)
    base = BeautifulSoup(base_url.content, "html.parser")
    base_data = base.find_all("ul", id="fellows")
    # Calls the function 'fellow_data' to obtain the AMS fellow name.
    fellow_data(base_data)
    # Calls the function 'university_data' to obtain the university information of the fellow.
    university_data(base_data)
    # Calls the function
    year_data(base_data)

# Function: Obtains AMS fellow name.
def fellow_data(base_data):
    for base_data in base_data:
        for line in base_data:
            dirty_fellow_data = line.get_text(strip=True)
            if ',' in dirty_fellow_data:
                start = dirty_fellow_data.find(",")
                cleaning_fellow_data = dirty_fellow_data[start+1:-1]
                end = cleaning_fellow_data.find(",")
                name = dirty_fellow_data[0:start] + cleaning_fellow_data[0:end]
                fellow.append(name)

# Function: Obtains university information of the fellow.
def university_data(base_data):
    for base_data in base_data:
        # Obtain University Data
        dirty_university_data = base_data.find_all("em")
        # Clean Obtained University Data
        for tag in dirty_university_data:
            # Remove <em></em> tag.
            unclean_university_data = tag.text
            # Remove comma and replace with dash.
            clean_university_data = unclean_university_data.replace(',', ' -')
            # Append data to list
            university.append(clean_university_data)

# Function: Obtains year the fellow was elected to AMS.
def year_data(base_data):
    for base_data in base_data:
        # Obtain '<span>' class containing the desired information.
        dirty_year_data = base_data.find_all("span")
        for tag in dirty_year_data:
            unclean_year_data = tag.text
            match = re.compile('\d\d\d\d')
            cleaning_year_data = match.findall(unclean_year_data)
            for n in cleaning_year_data:
                if n.isdigit():
                    year.append(n)

def merge(fellow, university, year):
    final_result = [(fellow[i], university[i], year[i]) for i in range(0, len(fellow))]
    return final_result

def create_csv(fellow, university, year):
    row_name = ['Name', 'University', 'Year']
    with open('ams-fellows.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(row_name)
        write.writerows(merge(fellow, university, year))

if __name__ == "__main__":
    # Stores the fellows name + university information
    fellow, university, year = [], [], []
    # Calls the function 'obtain_data' to obtain the fellow + university information.
    obtain_data()
    # Calls the function 'create_csv' to create a .csv file for export.
    create_csv(fellow, university, year)

    try:
        SOME_SECRET = os.environ["SOME_SECRET"]
    except KeyError:
        SOME_SECRET = "Token not available!"
