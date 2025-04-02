# Live MLB Stats in Google Sheets

## Overview
This project automates the process of fetching live MLB baseball statistics and updating them in a Google Sheet. It uses Python along with the Google Sheets API and the MLB Stats API to keep the sheet updated with the latest stats from the ongoing season.

## Features
- Automatically retrieves real-time MLB team statistics.
- Updates a specified Google Sheet with the latest data.
- Uses the Google Sheets API for seamless integration.
- Can be scheduled to run periodically using a cron job or cloud function.

## Technologies Used
- Python
- Google Sheets API
- MLB Stats API
- gspread (Google Sheets integration)
- requests (Fetching live data)
- oauth2client (Google authentication)

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/PiotrWarchol/baseball-stats-google-sheets.git
cd baseball-stats-google-sheets
```

### 2. Set Up a Google Cloud Project
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the **Google Sheets API** and **Google Drive API**.
4. Create a Service Account and generate a JSON key file.
5. Share your Google Sheet with the service account email.

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure Authentication
- Place your `credentials.json` file in the project root.
- Update `config.py` with the name of your Google Sheet.

### 5. Run the Script
```sh
python src/update_sheets.py
```

## Example Output
The Google Sheet will be updated with the following format:
```
| Team          | Wins | Losses | Runs Scored |
|--------------|------|--------|-------------|
| Yankees      | 45   | 30     | 380         |
| Dodgers      | 50   | 25     | 420         |
| Red Sox      | 40   | 35     | 360         |
```

## Automating Updates
To automate the script, you can use:
- **Cron Jobs** (Linux/macOS)
- **Windows Task Scheduler**
- **AWS Lambda** (for cloud execution)

## Future Enhancements
- Support for player-specific stats.
- Adding game schedules and scores.
- Visualization of data using Matplotlib or Google Sheets charts.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Author
Piotr Warchol

