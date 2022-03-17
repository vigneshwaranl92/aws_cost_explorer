import boto3
from datetime import *
import urllib3
urllib3.disable_warnings()

client = boto3.client('ce', region_name='ap-south-1', verify=False)
today = date.today()


class Ce:
    def __init__(self, start_str, end_str):
        self.start_date = start_str
        self.end_date = end_str

    def curr_month(self):
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': f'{self.start_date}',
                'End': f'{self.end_date}'
            },
            Granularity='MONTHLY',
            Metrics=[
                'BlendedCost',
            ],
            GroupBy=[
                {
                    'Type': 'TAG',
                    'Key': 'Project'
                }
            ]
        )
        current_month_fl = response["ResultsByTime"][0]["Groups"][0]["Metrics"]["BlendedCost"]["Amount"]
        current_month = int(float(current_month_fl))
        print(f'The Current month({today.strftime("%B")}) Mastbazaar bill is ${current_month}')

    def previous_month(self):
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': f'{self.start_date}',
                'End': f'{self.end_date}'
            },
            Granularity='MONTHLY',
            Metrics=[
                'BlendedCost',
            ],
            GroupBy=[
                {
                    'Type': 'TAG',
                    'Key': 'Project'
                }
            ]
        )
        current_month_fl = response["ResultsByTime"][0]["Groups"][0]["Metrics"]["BlendedCost"]["Amount"]
        current_month = int(float(current_month_fl))
        print(f'Previous month({today.strftime("%B")}) Mastbazaar bill is ${current_month}')


usage = Ce('2022-01-01', '2022-02-02')
usage.curr_month()
usage.previous_month()
