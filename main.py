from methods import *


pipeline_statuses_list = get_pipeline_statuses_list()

leads_url = f"https://advaga.amocrm.ru/api/v4/leads?\
filter[statuses][0][pipeline_id]={pipeline_id}&filter[statuses][0][status_id]=51721522\
&filter[statuses][1][pipeline_id]={pipeline_id}&filter[statuses][1][status_id]=54387386\
&filter[statuses][2][pipeline_id]={pipeline_id}&filter[statuses][2][status_id]=51721528\
&filter[statuses][3][pipeline_id]={pipeline_id}&filter[statuses][3][status_id]=59023070\
&filter[statuses][4][pipeline_id]={pipeline_id}&filter[statuses][4][status_id]=51721531\
&filter[statuses][5][pipeline_id]={pipeline_id}&filter[statuses][5][status_id]=56604890\
&filter[statuses][6][pipeline_id]={pipeline_id}&filter[statuses][6][status_id]=55910390\
&filter[statuses][7][pipeline_id]={pipeline_id}&filter[statuses][7][status_id]=51721843\
&filter[statuses][8][pipeline_id]={pipeline_id}&filter[statuses][8][status_id]=55910386\
&filter[statuses][9][pipeline_id]={pipeline_id}&filter[statuses][9][status_id]=51721849\
&filter[statuses][10][pipeline_id]={pipeline_id}&filter[statuses][10][status_id]=57100782\
&filter[statuses][11][pipeline_id]={pipeline_id}&filter[statuses][11][status_id]=51721852\
&filter[statuses][12][pipeline_id]={pipeline_id}&filter[statuses][12][status_id]=142\
&page=1&limit=250"
leads = requests.get(leads_url, headers=headers).json()
with open(f'assets/leads.json', 'w') as f:
    json.dump(leads, f, indent=3)
