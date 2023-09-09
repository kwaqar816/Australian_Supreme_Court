from cmath import inf
import datetime
from datetime import timedelta, date
from itertools import count
import requests
import json

start_date = datetime.datetime(2021, 1, 1).date()
end_date = datetime.datetime(2021, 12, 31).date()
daydiff = timedelta(days=1)
d = []
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
    data = str(r.text)
    # print(type(r.status_code))
    if data != '[]' and (day_name in court_working_days) and r.status_code == 200:
        print(counter, r.status_code)
        d.append(r.status_code)
        counter += 1
        info = json.loads(data)
        print(info[0]["pid"])
        info_2 = json.dumps(info)
        with open('JSON Output/{}.json'.format(day+'_'+month+'_'+year), 'w') as outfile:
            outfile.writelines(info_2)
            outfile.close()
    start_date += daydiff

print()
print()
print()
print()
print('==============================')
print(len(d))
print('==============================')
