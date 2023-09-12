import json
import pandas as pd
from methods import *


with open('assets/leads.json', 'r') as json_file:
    leads = json.load(json_file)['_embedded']['leads']


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
pipeline_statuses_dict = get_pipeline_statuses_dict()


for lead in leads:
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
    except:
        pass

    df = df.append(lead_dict, ignore_index=True)

df.to_csv('leads.csv', index=False)
