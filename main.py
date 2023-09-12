from methods import *
import pandas as pd


pipeline_statuses_list = list(get_pipeline_statuses_dict().keys())
leads_url_filters_by_status_id = get_leads_url_filters_by_status_id(pipeline_statuses_list)
df_columns = [
    'lead_id',
    'lead_name',
    'lead_status_id',
    'lead_status_name',
    'lead_created_at',
    'lead_updated_at',
    'lead_closed_at',
    'custom_field_lead_pm'
]
df = pd.DataFrame(columns=df_columns)


leads_url = f"https://advaga.amocrm.ru/api/v4/leads?{leads_url_filters_by_status_id}page=1&limit=250"
leads = requests.get(leads_url, headers=headers).json()
for lead in leads['_embedded']['leads']:
    lead_id = lead['id']
    lead_name = lead['name']
    lead_status_id = lead['status_id']
    lead_status_name = pipeline_statuses_dict[lead_status_id]
    lead_created_at = lead['created_at']
    lead_updated_at = lead['updated_at']
    lead_closed_at = lead['closed_at']

    custom_fields = lead['custom_fields_values']
    for custom_field in custom_fields:
        custom_field_id = custom_field['field_id']
        if custom_field_id == 2101979:
            custom_field_lead_pm = custom_field['values']['value']

    lead_dict = {"lead_id": lead_id,
                 "lead_name": lead_name,
                 "lead_status_id": lead_status_id,
                 "lead_status_name": lead_status_name,
                 "lead_created_at": lead_created_at,
                 "lead_updated_at": lead_updated_at,
                 "lead_closed_at": lead_closed_at}
    try:
        lead_dict["custom_field_lead_pm"] = custom_field_lead_pm
    except Exception as e:
        pass

    df = df._append(lead_dict, ignore_index=True)

with open(f'assets/leads_0.json', 'w') as f:
    json.dump(leads, f, indent=3)


i = 1
try:
    while leads['_links']['next']['href']:
        leads_next_url = leads['_links']['next']['href']
        leads = requests.get(leads_next_url, headers=headers).json()
        with open(f'assets/leads_{i}.json', 'w') as f:
            json.dump(leads, f, indent=3)
        i += 1

        for lead in leads['_embedded']['leads']:
            lead_id = lead['id']
            lead_name = lead['name']
            lead_status_id = lead['status_id']
            lead_status_name = pipeline_statuses_dict[lead_status_id]
            lead_created_at = lead['created_at']
            lead_updated_at = lead['updated_at']
            lead_closed_at = lead['closed_at']

            custom_fields = lead['custom_fields_values']
            try:
                for custom_field in custom_fields:
                    custom_field_id = custom_field['field_id']
                    if custom_field_id == 2101979:
                        custom_field_lead_pm = custom_field['values']['value']
            except Exception as e:
                pass

            lead_dict = {"lead_id": lead_id,
                         "lead_name": lead_name,
                         "lead_status_id": lead_status_id,
                         "lead_status_name": lead_status_name,
                         "lead_created_at": lead_created_at,
                         "lead_updated_at": lead_updated_at,
                         "lead_closed_at": lead_closed_at}
            try:
                lead_dict["custom_field_lead_pm"] = custom_field_lead_pm
            except Exception as e:
                pass

            df = df._append(lead_dict, ignore_index=True)

except Exception as e:
    print(e)

df.to_csv(f'assets/leads.csv', index=False)
