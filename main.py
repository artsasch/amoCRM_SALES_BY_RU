from methods import *


pipeline_statuses_list = list(get_pipeline_statuses_dict().keys())
leads_url_filters_by_status_id = get_leads_url_filters_by_status_id(pipeline_statuses_list)

leads_url = f"https://advaga.amocrm.ru/api/v4/leads?{leads_url_filters_by_status_id}page=1&limit=250"
leads = requests.get(leads_url, headers=headers).json()

with open(f'assets/leads.json', 'w') as f:
    json.dump(leads, f, indent=3)

i = 1

try:
    while leads['_links']['next']['href']:
        leads_next_url = leads['_links']['next']['href']
        leads = requests.get(leads_next_url, headers=headers).json()
        with open(f'assets/leads_{i}.json', 'w') as f:
            json.dump(leads, f, indent=3)
        i += 1
except KeyError as e:
    print(e)
