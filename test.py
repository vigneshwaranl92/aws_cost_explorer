import boto3
from datetime import *
import re
import urllib3
urllib3.disable_warnings()
from datetime import date, timedelta

first_day_of_current_month = date.today().replace(day=1)
print(first_day_of_current_month)
last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)
print(last_day_of_previous_month)

print("Previous month:", last_day_of_previous_month.month)


# client = boto3.client('ce', region_name='ap-south-1', verify=False)
#
# response1 = client.get_cost_and_usage(
#     TimePeriod={
#         'Start': '2022-01-01',
#         'End': '2022-02-02'
#     },
#     Granularity='MONTHLY',
#     Metrics=[
#         'BlendedCost',
#     ],
#     GroupBy = [
#     {
#         'Type': 'TAG',
#         'Key': 'Project'
#     }
#     ]
# )
#
# print(response1)
# current_month_fl = response1["ResultsByTime"][0]["Groups"][0]["Metrics"]["BlendedCost"]["Amount"]
# current_month = int(float(current_month_fl))
# print(f'current_month = ${current_month}')

current_date = date.today()
print(current_date)
