import requests
import json


with open('resource/access_token.json') as json_file:
    access_token = json.load(json_file)["access_token"]
headers = {
    'Accept': 'application/json',
    'Authorization': f"Bearer {access_token}",
}
pipeline_id = 5930839


def get_pipeline_statuses_list():
    statuses_url = f"https://advaga.amocrm.ru/api/v4/leads/pipelines/{pipeline_id}/statuses"
    statuses = requests.get(statuses_url, headers=headers).json()
    with open(f'assets/statuses.json', 'w') as f:
        json.dump(statuses, f, indent=3)
    statuses_dict = {i['id']: i['name'] for i in statuses['_embedded']['statuses']}
    del statuses_dict[143]
    statuses_keys_list = list(statuses_dict.keys())
    return statuses_keys_list


def get_leads_url_filters_by_status_id(pipeline_statuses_list):
    return leads_url_filters_by_status_id
