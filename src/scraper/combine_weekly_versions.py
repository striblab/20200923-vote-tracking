import re
import os
import json
import math
import datetime

VERSION_DIR = 'json/versions'

filename_regex = re.compile('county-list_(\d{4}-\d+-\d+)_.*\.json')
matching_files = [f for f in os.listdir(VERSION_DIR) if re.search(filename_regex, f)]

# Get the unique data dates in the folder, then sort them
unique_dates = sorted(list(set([re.search(filename_regex, d).group(1) for d in matching_files])))
# print(matching_files, unique_dates)

def weeks_away(input_str):
    election_week_start = datetime.datetime.strptime('2020-10-31', '%Y-%m-%d')
    data_date = datetime.datetime.strptime(input_str, '%Y-%m-%d')
    # print(math.ceil((election_week_start - data_date).days / 7))
    weeks_away = math.ceil((election_week_start - data_date).days / 7)
    return weeks_away

most_recent_updates = []
for date in unique_dates:
    regex = re.compile('{}_\d+.json'.format(date))
    most_recent = sorted(list(filter(regex.search, matching_files)), reverse=True)[0]
    # print(most_recent)
    most_recent_updates.append(most_recent)

out_obj = {'ts_statewide': []}
for file in most_recent_updates:
    with open(os.path.join(VERSION_DIR, file), 'r') as version:
        version_obj = json.loads(version.read())
        # First create counties if needed
        for county, data in version_obj['counties'].items():
            if county not in out_obj:
                out_obj[county] = {'ts': []}
                # out_obj[county]['ts'] = []

        # Now come back and update data
        for county, data in version_obj['counties'].items():
            out_obj[county]['date_latest'] = version_obj['data_date']
            out_obj[county]['apps_submitted_latest'] = data['apps_submitted']
            out_obj[county]['ballots_accepted_latest'] = data['ballots_accepted']

            ts_record = {
                'date': version_obj['data_date'],
                'weeks_away': weeks_away(version_obj['data_date']),
                'apps_submitted': data['apps_submitted'],
                'ballots_accepted': data['ballots_accepted'],
            }

            out_obj[county]['ts'].append(ts_record)

            ts_statewide_date = [date for date in out_obj['ts_statewide'] if date['date'] == version_obj['data_date']]
            if len(ts_statewide_date) == 0:
                out_obj['ts_statewide'].append(ts_record)
            else:
                # ts_statewide_date[0]['weeks_away'] += weeks_away(version_obj['data_date'])
                ts_statewide_date[0]['apps_submitted'] += data['apps_submitted']
                ts_statewide_date[0]['ballots_accepted'] += data['ballots_accepted']

print(json.dumps(out_obj))
