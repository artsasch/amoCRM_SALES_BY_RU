# AmoCRM Leads Data Extractor

This Python script extracts data from the AmoCRM API related to leads and saves it in a structured format. The script utilizes the AmoCRM API, the `requests` library, and data processing with `pandas`.

## Prerequisites

Before running the script, ensure you have the required libraries installed:

```bash
pip install requests pandas
```

## Configuration

1. Import required methods from the `methods` module.
   
   ```python
   from methods import *
   ```

2. Set up your AmoCRM API headers.

   ```python
   headers = {
       "Authorization": "Bearer your_api_token",
       "Content-Type": "application/json"
   }
   ```

3. Adjust the columns for the DataFrame as needed.

   ```python
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
   ```

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

   Ensure that the script is executed in an environment with internet access.

2. The script fetches leads data from the AmoCRM API, processes it, and saves the results in JSON files (`assets/leads_0.json`, `assets/leads_1.json`, etc.) for each page of leads.

3. The script also compiles the data into a single CSV file (`assets/leads.csv`).

## Data Processing

- The script handles paginated responses, fetching all available leads from the API.

- Timestamps are converted to human-readable date formats.

- A link to each lead's details page is generated and added to the DataFrame.

## Optional Database Loading

If you want to load the extracted data into a database, uncomment the following code section at the end of the script:

```python
# df = pd.read_csv('assets/leads.csv')
# table_name = 'sales_leads'
# engine = sqlalchemy.create_engine("mariadb+mariadbconnector://all:yaro1997dobrg*M@localhost:3306/amoCRM")
# inspector = sqlalchemy.inspect(engine)
# if not inspector.has_table(table_name):
#     df.head(0).to_sql(table_name, engine, if_exists='replace', index=False)
# df.to_sql(table_name, engine, if_exists='replace', index=False)
# print(f'{table_name} loaded to the database')
```

Ensure you have set up your database connection and adjusted the code according to your database details.

## Note

- The script catches exceptions during the data extraction process and prints error messages if any issues occur.

- Customize the script based on your AmoCRM API structure and data requirements.

Feel free to modify and extend the script according to your specific use case and data processing needs.
