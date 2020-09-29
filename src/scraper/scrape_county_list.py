import re
import json
import datetime
import requests
from bs4 import BeautifulSoup

COUNTY_ENDPOINT = 'https://www.sos.state.mn.us/election-administration-campaigns/data-maps/absentee-data/'

def int_or_none(input):
    try:
        return int(input.replace(',', ''))
    except:
        return None

r = requests.get(COUNTY_ENDPOINT)
if r.ok:
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')

    # Get data date
    data_date_node = soup.find(text=re.compile("Accepted ballots \(\d+/\d+/\d+\)"))
    # data_date = datetime.datetime.strptime((re.search(r'(\d+/\d+/\d+)', data_date_node).group(1)), '%m/%d/%y').date()
    # Temp for dummy data
    # data_date = datetime.datetime.strptime('10/02/20', '%m/%d/%y').date()
    # print(data_date)

    county_table = soup.find('table')  # First table

    county_data = {}

    for row in county_table.find_all('tr'):
        if row.find('th').text != 'County':
            county_name = row.find('th').text.strip()
            apps_submitted = int_or_none(row.find_all('td')[0].text.strip())
            ballots_accepted = int_or_none(row.find_all('td')[1].text.strip())

            county_data[county_name] = {
                # 'county_name': county_name,
                'apps_submitted': apps_submitted,
                'ballots_accepted': ballots_accepted,
            }

    with open('json/versions/county-list_{}_{}.json'.format(data_date.strftime('%Y-%m-%d'), datetime.datetime.now().strftime('%Y%m%d%H%M%S')), 'w') as outfile:
        file_contents = json.dumps({'data_date': data_date.strftime('%Y-%m-%d'), 'counties': county_data})
        outfile.write(file_contents)
        outfile.close()
