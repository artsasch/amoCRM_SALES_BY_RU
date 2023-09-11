from methods import *


pipeline_statuses_list = get_pipeline_statuses_list()
leads_url_filters_by_status_id = get_leads_url_filters_by_status_id(pipeline_statuses_list)

leads_url = f"https://advaga.amocrm.ru/api/v4/leads?{leads_url_filters_by_status_id}page=1&limit=250"
leads = requests.get(leads_url, headers=headers).json()
with open(f'assets/leads.json', 'w') as f:
    json.dump(leads, f, indent=3)
