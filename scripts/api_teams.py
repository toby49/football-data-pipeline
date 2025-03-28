import requests
import pandas as pd
from pandas_gbq import to_gbq
import keys

API_KEY = keys.api_key
URL = 'https://v3.football.api-sports.io/teams'

# Set up headers for authentication
headers = {
    'x-rapidapi-key': API_KEY,
    # 'x-rapidapi-host': 'v3.football.api-sports.io'
}

# Make a request to the API to fetch match data (Premier League ID = 39)
params = {'league': 39, 'season': 2023}
response = requests.get(URL, headers=headers, params=params)
data = response.json()

# Convert data into a pandas DataFrame
df = pd.json_normalize(data['response'])

# Replace dots in column names with underscores to allign with GBQ allowed characters
df.columns = df.columns.str.replace('.', '_')

# Define BigQuery project and table details
project_id = "civil-zodiac-454713-q3"  
table_id = 'raw_football.raw_teams'  

# Load DataFrame into BigQuery (use the 'replace' write disposition or 'append' if you prefer to add data to an existing table)
to_gbq(df, destination_table=table_id, project_id=project_id, if_exists='replace')

print(f"Data has been successfully loaded into BigQuery table {table_id} in project {project_id}")
