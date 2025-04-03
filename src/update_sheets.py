import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from config import GOOGLE_SHEET_ID, SHEET_NAME, MLB_STATS_API, CREDENTIALS_FILE
import pandas as pd
from bs4 import BeautifulSoup
import json
import numpy as np
import random

# Authenticate
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\piotr\Downloads\sincere-lexicon-329704-e385292fc1d9.json", scope)
client = gspread.authorize(creds)

# Open the sheet using the Sheet ID
SHEET_ID = "1hL3is__Jyar-Lw6L3mO2P4U7CCzJcAEmRFlMoYtaYiQ"
sheet = client.open_by_key(SHEET_ID).sheet1

# Step 3: Clear all data in the sheet
sheet.clear()  # This removes all existing data from the sheet

# Step 4: Fetch the webpage
url = "https://baseballsavant.mlb.com/leaderboard/custom?year=2025&type=batter&filter=&min=q&selections=pa%2Ck_percent%2Cbb_percent%2Cwoba%2Cxwoba%2Csweet_spot_percent%2Cbarrel_batted_rate%2Chard_hit_percent%2Cavg_best_speed%2Cavg_hyper_speed%2Cwhiff_percent%2Cswing_percent&chart=false&x=pa&y=pa&r=no&chartType=beeswarm&sort=xwoba&sortDir=desc"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 5: Extract the JSON data from the script tag
script_tag = soup.find('script', string=lambda t: t and 'var data =' in t)  # Find the script tag containing the JSON
json_data_str = script_tag.string.split('var data = ')[1].split(';')[0]  # Extract the JSON data part
player_data = json.loads(json_data_str)  # Parse the JSON string into Python data structure

# Step 6: Convert the data into a pandas DataFrame
df = pd.DataFrame(player_data)

# Handle NaN values: Replace NaN with an empty string to avoid JSON errors
df = df.fillna('')

# Step 7: Sort by a random column
random_column = random.choice(df.columns.tolist())  # Select a random column to sort by
df = df.sort_values(by=random_column, ascending=False)  # Sort in descending order

# Step 8: Add a "Rank" column at the start
df.insert(0, "Rank", range(1, len(df) + 1))  # Add rank numbers starting from 1

# Step 9: Insert Column Headers
sheet.append_row(df.columns.tolist())  # Add column headers to the first row

# Step 10: Insert Updated Data
sheet.append_rows(df.values.tolist())  # Add the player data below the headers

print(f"Google Sheet cleared and updated with fresh data successfully! Sorted by: {random_column}")