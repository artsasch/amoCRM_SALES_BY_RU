import requests
import json


with open('resource/access_token.json', 'r') as json_file:
    data = json.load(json_file)
    access_token = data.get("access_token")
    pipeline_id = data.get("pipeline_id")

headers = {
    'Accept': 'application/json',
    'Authorization': f"Bearer {access_token}",
}


def get_pipeline_statuses_dict():
    statuses_url = f"https://advaga.amocrm.ru/api/v4/leads/pipelines/{pipeline_id}/statuses"
    statuses = requests.get(statuses_url, headers=headers).json()
    with open(f'assets/statuses.json', 'w') as f:
        json.dump(statuses, f, indent=3)
    statuses_dict = {i['id']: i['name'] for i in statuses['_embedded']['statuses']}
    del statuses_dict[143]
    return statuses_dict


def get_leads_url_filters_by_status_id(pipeline_statuses_list):
    leads_url_filters_by_status_id = ''
    enumerated_statuses_dict = dict(enumerate(pipeline_statuses_list))
    for i, status_id in enumerated_statuses_dict.items():
        leads_url_filters_by_status_id += f'filter[statuses][{i}][pipeline_id]={pipeline_id}&filter[statuses][{i}][status_id]={status_id}&'
    return leads_url_filters_by_status_id
