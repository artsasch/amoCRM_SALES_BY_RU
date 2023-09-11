import pandas as pd
import requests
import time
import sqlalchemy
import datetime
import json
from progressBar import progressbar


with open('resource/access_token.json') as json_file:
    access_token = json.load(json_file)["access_token"]

headers = {
    'Accept': 'application/json',
    'Authorization': f"Bearer {access_token}",
}
pipeline_id = 5930839


statuses_url = f"https://advaga.amocrm.ru/api/v4/leads/pipelines/{pipeline_id}/statuses"
statuses = requests.get(statuses_url, headers=headers).json()
with open(f'assets/statuses.json', 'w') as f:
    json.dump(statuses, f, indent=3)


# leads_url = f"https://advaga.amocrm.ru/api/v4/leads?filter[pipeline_id]={pipeline_id}&page=4&limit=250"
# leads = requests.get(leads_url, headers=headers).json()
# with open(f'assets/leads.json', 'w') as f:
#     json.dump(leads, f, indent=3)