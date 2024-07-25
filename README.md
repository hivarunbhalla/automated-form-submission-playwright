# Automated Review Submission Using Playwright

This Python script automates the process of submitting reviews to a website using Playwright. It reads reviews from a CSV file and submits them one by one.

## Prerequisites

- Python 3.6 or above
- Playwright (automatically installed via `requirements.txt`)
- Chromium browser (installed automatically by Playwright)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hivarunbhalla/automated-review-submission-playwright.git
   cd your-repo

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

## Usage
1. Fill in the required details in the script:

- START_URL: URL of the website where reviews will be submitted.
- CSV_PATH: Path to the CSV file containing reviews.
- ROWS: Number of rows in the CSV data.

2. CSV Format: The CSV file should have the following columns:

- Title: Title of the review.
- Body: Body or content of the review.
- Name: Name of the reviewer.
- Email: Email address of the reviewer.
- Modify the fieldnames list in write_reviews_to_csv function based on your CSV headers.

3. Run the script:

   ```bash
   python main.py

4. The script will launch a Chromium browser, navigate to the website, log in (if required), and submit each review from the CSV file.

## Script Details

- read_reviews_from_csv: Reads reviews from the specified CSV file into a list of dictionaries.
- write_reviews_to_csv: Writes processed reviews back to the CSV file after submission.
- run: Main function that orchestrates the review submission process using Playwright.

## Notes
- Ensure that the Playwright browser is installed and accessible.
- Modify the browser launch options (headless=False) in run function for debugging purposes.
- Handle website-specific elements (role, placeholder, name, locator) as per your website's HTML structure.

