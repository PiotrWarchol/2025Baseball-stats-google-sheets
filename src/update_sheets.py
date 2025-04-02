import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials-json@sincere-lexicon-329704.iam.gserviceaccount.com", scope)
client = gspread.authorize(creds)

# Open the sheet using the Sheet ID
SHEET_ID = "1hL3is__Jyar-Lw6L3mO2P4U7CCzJcAEmRFlMoYtaYiQ"
sheet = client.open_by_key(SHEET_ID).sheet1

# Example: Update a row
sheet.append_row(["Yankees", 45, 30, 380])
print("Google Sheet updated successfully!")
