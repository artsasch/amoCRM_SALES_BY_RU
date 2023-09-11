import sqlalchemy
import pandas as pd


df_leads_write = pd.read_csv('leads_write.csv', index_col=0)
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://all:yaro1997dobrg*M@localhost:3306/amoCRM")
with engine.begin() as connection:
    connection.execute('''TRUNCATE TABLE ''' + '''pm_budget''')
    df_leads_write.to_sql('pm_budget', con=connection, if_exists='replace', index=bool)
engine.dispose()


df_leads_write = pd.read_csv('filtered_leads.csv', index_col=0)
table_name = 'financial_report'
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://all:yaro1997dobrg*M@localhost:3306/amoCRM")
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table(table_name):
    df_leads_write.head(0).to_sql(table_name, engine, if_exists='replace', index=False)
df_leads_write.to_sql(table_name, engine, if_exists='replace', index=False)
