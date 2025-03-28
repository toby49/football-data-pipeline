import requests
import pandas as pd
from pandas_gbq import to_gbq
import keys

API_KEY = keys.api_key
URL = 'https://v3.football.api-sports.io/players'

# Set up headers for authentication
headers = {
    'x-rapidapi-key': API_KEY,
    # 'x-rapidapi-host': 'v3.football.api-sports.io'
}

# Make a request to the API to fetch match data 
params = {'league': 39, 'season': 2023, 'team': 42} #Filtering to Arsenal players Premier League 2023/24 season

# Define an empty list to store data from all pages
all_data = []

# Loop through the first 3 pages
for page_num in range(1, 3):  # Pages 1 to 3 - api only allows a maximum of 3 iterations for free account
    params['page'] = page_num
    print(f"Fetching data for page {page_num}...")

    # Make the request for the current page
    response = requests.get(URL, headers=headers, params=params)
    
    # Ensure the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Check if the 'response' key contains data
        if 'response' in data and data['response']:
            all_data.extend(data['response'])  # Append the 'response' data from each page
            print(f"Page {page_num} has {len(data['response'])} players.")
        else:
            print(f"Page {page_num} is empty or contains no player data.")
    else:
        print(f"Failed to fetch data for page {page_num}, status code: {response.status_code}")

# Check if we have any data
if not all_data:
    print("No data was retrieved across all pages.")
else:
    # Normalize the collected data into a DataFrame
    df = pd.json_normalize(all_data)


# Flatten the statistics column
df_statistics = pd.json_normalize(
    df['statistics'].explode(),  # Flatten the list of dictionaries in 'statistics'
    sep='_',  # Use underscore for separating nested keys
    errors='ignore'  # Ignore any missing keys
)

# Now, merge the flattened statistics DataFrame with the original player-level data
df_flattened = pd.concat([df.drop(columns=['statistics']), df_statistics], axis=1)

# Replace dots in column names with underscores to allign with GBQ allowed characters
df_flattened.columns = df_flattened.columns.str.replace('.', '_')

print(df_flattened)

# Define BigQuery project and table details
project_id = "civil-zodiac-454713-q3"  
table_id = 'raw_football.raw_player_stats'  

# Load DataFrame into BigQuery (use the 'replace' write disposition or 'append' if you prefer to add data to an existing table)
to_gbq(df_flattened, destination_table=table_id, project_id=project_id, if_exists='replace')

print(f"Data has been successfully loaded into BigQuery table {table_id} in project {project_id}")

