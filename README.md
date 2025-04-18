# RocketReach Sample Scraper

This project demonstrates a simple, safe method for extracting contact information from RocketReach using Selenium automation.

> **Important:** This is only a simulation project created for portfolio and proposal purposes. No actual data was scraped from RocketReach.

---

## Project Structure

```
rocketreach-scraper/
├── selenium_scraper.py       # Python script that automates browser scraping
├── output/
│   └── rocketreach_contacts_sample.csv  # Sample dummy data file
└── screenshots/               # Folder for storing screenshots of code and results
```

## Features

- Automated browser navigation using Selenium.
- Manual login required to comply with RocketReach terms.
- Scrapes sample contact information fields:
  - Full Name
  - Job Title
  - Company Name
  - Email Address
  - LinkedIn Profile
- Saves extracted data into a structured CSV file.

## Setup Instructions

1. Install required libraries:

```bash
pip install selenium pandas
```

2. Make sure you have Chrome browser installed and the corresponding `chromedriver` executable available.

3. Run the script:

```bash
python selenium_scraper.py
```

4. Log in manually when prompted.

5. After login, the script will navigate to the search page and scrape a few sample contacts.

6. Check the output folder for the resulting CSV file.

## Disclaimer

- This project is a **mock simulation** intended only for demonstrating automation capabilities.
- Always respect the Terms of Service of any platform.
- For production scraping of RocketReach data, official API access is recommended.

---

Created with ❤️ for portfolio showcase.
