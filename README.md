# Job Scraper

## Description
This project is a web scraper built using Python and Selenium to extract job listings from [VLance.vn](https://www.vlance.vn/viec-lam-freelance). The script searches for a specific job role, scrapes job details, and saves them into a CSV file.

## Features
- Automates job search on VLance.vn
- Extracts job title, role, salary, address, and time left
- Saves job data into `job.csv`
- Uses Selenium for web automation

## Requirements
Make sure you have Python installed (Python 3.x recommended). You also need to install the required dependencies from `requirements.txt`.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/DoThiThuyUyen/crawl-data.git
   cd crawl-data
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```bash
   python scraper.py
   ```
2. The scraped job listings will be saved in `job.csv`.

## Dependencies
This project requires the following Python libraries:
- `selenium`
- `webdriver-manager`

All dependencies are listed in `requirements.txt`.

## Notes
- Ensure that you have Google Chrome installed.
- The script automatically downloads and manages the ChromeDriver.
- The website structure may change over time, so the CSS selectors might need to be updated accordingly.

## License
This project is licensed under the MIT License.

