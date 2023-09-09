from cmath import inf
import datetime
from datetime import timedelta, date
from pydoc import describe
from re import A
import requests
import json
import pandas as pd

start_date = datetime.datetime(2021, 1, 1).date()
end_date = datetime.datetime(2021, 12, 31).date()
daydiff = timedelta(days=1)
each_row = []
court_working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
counter = 1
while start_date <= end_date:
    day = start_date.strftime('%d')
    month = start_date.strftime('%m')
    year = start_date.strftime('%Y')
    day_name = datetime.date(int(year), int(month), int(day))
    day_name = day_name.strftime("%A")
    r = requests.get(
        'https://www.supremecourt.vic.gov.au/dhl/get_list.json?keyword=&judicial=&division=&date={}%2F{}%2F{}'.format(day, month, year))
    print(r.status_code)
    data = str(r.text)
    if data != '[]' and (day_name in court_working_days) and r.status_code == 200:

        json_output = json.loads(data)
        print(type(json_output))
        json_length = len(json_output)
        # pid = json_output[1]
        # print(type(pid))
        # print(pid)
        print('json_length: - ', json_length)
        if json_length != 0:
            for i in range(json_length):
                pid = json_output[i]["pid"]
                case_date = json_output[i]["date"]
                time = json_output[i]["time"]
                court_type = json_output[i]["court_type"]
                division = json_output[i]["division"]
                judicial_officer = json_output[i]["judicial_officer"]
                case_number = json_output[i]["case_number"]
                description = json_output[i]["description"]
                court_address = json_output[i]["court_address"]
                summary = json_output[i]["summary"]
                maps_url = json_output[i]["maps_url"]
                print(pid)
                print(case_date)
                print(time)
                print(court_type)
                print(division)
                print(judicial_officer)
                print(case_number)
                print(description)
                print(court_address)
                print(summary)
                print(maps_url)
                single_row = [pid, case_date, time, court_type, division, judicial_officer,
                              case_number, description, court_address, summary, maps_url]
                each_row.append(single_row)

        else:
            pid = json_output[0]["pid"]
            case_date = json_output[0]["date"]
            time = json_output[0]["time"]
            court_type = json_output[0]["court_type"]
            division = json_output[0]["division"]
            judicial_officer = json_output[0]["judicial_officer"]
            case_number = json_output[0]["case_number"]
            description = json_output[0]["description"]
            court_address = json_output[0]["court_address"]
            summary = json_output[0]["summary"]
            maps_url = json_output[0]["maps_url"]
            print(pid)
            print(case_date)
            print(time)
            print(court_type)
            print(division)
            print(judicial_officer)
            print(case_number)
            print(description)
            print(court_address)
            print(summary)
            print(maps_url)
            single_row = [pid, case_date, time, court_type, division, judicial_officer,
                          case_number, description, court_address, summary, maps_url]
            each_row.append(single_row)
        print('|||||||||', counter, '||||||||||')
        counter += 1
        print()
        print()
        print('-------------------------------------------------------')
        print()
        print()

    start_date += daydiff


df = pd.DataFrame(each_row, columns=['pid', 'case_date', 'time', 'court_type', 'division', 'judicial_officer',
                                     'case_number', 'description', 'court_address', 'summary', 'maps_url'])
df.to_csv('Final_Data.csv')


# AfXqv6xmtZc7kLqU9G+Lw6mHreuDRL0svmhesDV
# AKIAUI4HPKFNXYQYJBXS

# AWS CREDS
# k6AcNTg9KDJhkWyfvmrJVD0ZmXvXgK8gYlUagqHj
# AKIAUI4HPKFN45JKVKFX
# @lptGn|Y8tMG}jh
