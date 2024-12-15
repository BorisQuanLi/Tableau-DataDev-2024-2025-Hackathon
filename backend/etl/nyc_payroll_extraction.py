import requests
import logging

NYC_PAYROLL_API_URL = "https://data.cityofnewyork.us/resource/k397-673e.json"

def extract_nyc_payroll_data(nyc_open_data_api_url=NYC_PAYROLL_API_URL):
    # Extract data from the NYC Open Data API
    response = requests.get(nyc_open_data_api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        logging.error(f"Failed to retrieve data: {response.status_code}")
        return []

if __name__ == "__main__":
    data = extract_nyc_payroll_data()
    print(data)
