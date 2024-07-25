import csv
import time
from playwright.sync_api import Playwright, sync_playwright, expect

START_URL = ""  # Fill in your website URL
CSV_PATH =  r'data.csv'  # Fill in your CSV path
ROWS = 10 # Fill rows in csv data

def read_reviews_from_csv(filename):
    reviews = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            reviews.append(row)
    return reviews

def write_reviews_to_csv(filename, reviews):
    fieldnames = ['Title', 'Body', 'Name', 'Email']  # Adjust these fieldnames based on your CSV headers
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reviews)

def run(playwright: Playwright, max_iterations: int, reviews_filename: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    reviews = read_reviews_from_csv(reviews_filename)

    processed_indices = []
    for iteration in range(max_iterations):
        if not reviews:
            print("No more reviews to process.")
            break

        page = context.new_page()
        page.goto(START_URL)
        
        page.get_by_role("button", name="Write a review").click()
        page.get_by_placeholder("Enter your title").fill(review['Title'])
        page.get_by_placeholder("Enter your message").fill(review['Body'])
        page.get_by_role("button", name="Next").click()
        page.get_by_role("button", name="Next").click()
        page.get_by_placeholder("Enter your name").fill(review['Name'])
        page.get_by_placeholder("example@yourdomain.com").fill(review['Email'])
        page.locator(".r--submit-form").click()
        page.locator("#modals-container i").click()

        page.close()

    context.close()
    browser.close()

    # Rewrite the CSV file with any remaining reviews
    write_reviews_to_csv(reviews_filename, reviews)

with sync_playwright() as playwright:
    run(playwright, max_iterations=ROWS, reviews_filename=CSV_PATH)
