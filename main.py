from methods import *
import sqlalchemy
import pandas as pd


pipeline_statuses_list = list(get_pipeline_statuses_dict().keys())
pipeline_statuses_dict = get_pipeline_statuses_dict()

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

df['lead_created_at'] = pd.to_datetime(df['lead_created_at'], unit='s')
df['lead_created_at'] = df['lead_created_at'].dt.strftime('%Y-%m-%d')

df['lead_updated_at'] = pd.to_datetime(df['lead_updated_at'], unit='s')
df['lead_updated_at'] = df['lead_updated_at'].dt.strftime('%Y-%m-%d')

df['lead_closed_at'] = pd.to_datetime(df['lead_closed_at'], unit='s')
df['lead_closed_at'] = df['lead_closed_at'].dt.strftime('%Y-%m-%d')

df['lead_link'] = 'https://advaga.amocrm.ru/leads/detail/' + df['lead_id'].astype(str)

df.to_csv(f'assets/leads.csv', index=False)


# df = pd.read_csv('assets/leads.csv')
# table_name = 'sales_leads'
# engine = sqlalchemy.create_engine("mariadb+mariadbconnector://all:yaro1997dobrg*M@localhost:3306/amoCRM")
# inspector = sqlalchemy.inspect(engine)
# if not inspector.has_table(table_name):
#     df.head(0).to_sql(table_name, engine, if_exists='replace', index=False)
# df.to_sql(table_name, engine, if_exists='replace', index=False)
# print(f'{table_name} loaded to database')
