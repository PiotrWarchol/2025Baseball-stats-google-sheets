# Baseball Stats Google Sheets Updater

## Overview
This project fetches baseball player statistics from Baseball Savant and updates a Google Sheet with the latest data. The script ensures the sheet is cleared before each update, sorts the data by a random column, and adds a ranking column for dynamic analysis.

## Features
- **Automated Data Retrieval**: Scrapes the latest baseball stats from Baseball Savant.
- **Google Sheets Integration**: Updates a specified Google Sheet with fresh data.
- **Sheet Reset**: Clears previous data before inserting new statistics.
- **Random Sorting**: Data is sorted by a randomly selected column each time the script runs.
- **Ranking System**: Adds a "Rank" column to order players dynamically.

## Requirements
- Python 3.12+
- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `json`
  - `gspread`
  - `oauth2client`
  - `pandas`

## Setup
1. **Google Sheets API Authentication**
   - Obtain a Google Service Account JSON key.
   - Enable the Google Sheets API and add the service account email to your Google Sheet with edit permissions.
   - Update the script with your key file path.

2. **Install Dependencies**
   ```bash
   pip install requests beautifulsoup4 gspread oauth2client pandas
   ```

3. **Update Configuration**
   - Replace `Baseball Stats` in the script with the actual name of your Google Sheet.
   - Ensure the correct file path to your Google Service Account key JSON.

## Running the Script
Run the script with:
```bash
python update_sheets.py
```

## Expected Output
- The script fetches baseball stats and converts them into a structured table.
- Data is sorted by a randomly chosen column.
- A "Rank" column is added.
- The Google Sheet is cleared and updated with new headers and data.

## Future Enhancements
- Allow user selection of the sorting column.
- Implement scheduled updates using a cron job or a cloud function.

## License
This project is licensed under the MIT License.

## Author
Piotr Warchol

