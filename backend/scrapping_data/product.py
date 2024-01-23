import os
import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime

commodity_url_list = [
    "https://kr.investing.com/commodities/copper",
    "https://kr.investing.com/commodities/aluminum"
]

product_name_list = [
    "Copper",
    "Aluminum"
]

# Get the current date and time
current_date = datetime.now().strftime('%Y-%m-%d')

# Create the 'save_data' directory if it doesn't exist
save_data_dir = r'C:\Users\staff\Documents\YRC\Finance_data\securities_analysis\backend\save_data'
os.makedirs(save_data_dir, exist_ok=True)
print("Current Working Directory:", os.getcwd())

for i in range(len(commodity_url_list)):
    url = commodity_url_list[i]
    product_name = product_name_list[i]

    html = requests.get(url).text  # 웹 요청

    content = BeautifulSoup(html, 'html.parser')
    body = content.html.body

    # Extract information based on HTML structure
    prev_close = body.find('dd', {'data-test': 'prevClose'}).text.strip()
    open_price = body.find('dd', {'data-test': 'open'}).text.strip()
    daily_range = body.find('dd', {'data-test': 'dailyRange'}).text.strip()
    week_range = body.find('dd', {'data-test': 'weekRange'}).text.strip()
    one_year_return = body.find('dd', {'data-test': 'oneYearReturn'}).text.strip()
    contract_size = body.find('dd', {'data-test': 'contract_size'}).text.strip()

    with open(f'{save_data_dir}/{product_name}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)
        print("Current Working Directory:", os.getcwd())

        # Write header row
        csv_writer.writerow(['Product', 'Previous Close', 'Open Price', 'Daily Range', '52-Week Range', 'One-Year Return', 'Contract Size', "Date"])
        csv_writer.writerow([product_name, prev_close, open_price, daily_range, week_range, one_year_return, contract_size, current_date])

    # Print or use the extracted data
    print(f"Product: {product_name}")
    print(f"Previous Close: {prev_close}")
    print(f"Open Price: {open_price}")
    print(f"Daily Range: {daily_range}")
    print(f"52-Week Range: {week_range}")
    print(f"One-Year Return: {one_year_return}")
    print(f"Contract Size: {contract_size}")
