import boto3
import datetime
import re
import urllib3
urllib3.disable_warnings()

client = boto3.client('ce', region_name='ap-south-1', verify=False)

response = client.get_cost_and_usage(
    TimePeriod={
        'Start': '2022-02-01',
        'End': '2022-03-02'
    },
    Granularity='MONTHLY',
    Metrics=[
        'BlendedCost',
    ],
    GroupBy = [
    {
        'Type': 'TAG',
        'Key': 'Project'
    }
    ]
)

print(response)

response1 = client.get_cost_and_usage(
    TimePeriod={
        'Start': '2022-01-01',
        'End': '2022-02-02'
    },
    Granularity='MONTHLY',
    Metrics=[
        'BlendedCost',
    ],
    GroupBy = [
    {
        'Type': 'TAG',
        'Key': 'Project'
    }
    ]
)

print(response1)

# recurring_month = response1["ResultsByTime"][0]["Groups"]
# rec_mnt_value = recurring_month['Metrics']['BlendedCost']['Amount']
# rec_final_val = float(rec_mnt_value)
tsv_lines = []
for project in response["ResultsByTime"][0]["Groups"]:
    namestring = project['Keys'][0]
    print(namestring)
    name = re.search("\$(.*)", namestring).group(1)
    if name is None or name == "":
        name = "Mastbazaar"
    amount = project['Metrics']['BlendedCost']['Amount']
    amount = float(amount)
    line = "{}\t${:,.2f}".format(name, amount)
    print(line)
    tsv_lines.append(line)

