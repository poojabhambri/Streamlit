import requests
import pandas as pd

def fetch_data():
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.xlsx'  # Replace with the URL of the XLSX file
    response = requests.get(url)

    # Save the XLSX file locally
    with open('owid-covid-data.xlsx', 'wb') as f:
        f.write(response.content)

    # Read the data using pandas
    data = pd.read_excel('owid-covid-data.xlsx')
    return data
def main():
    st.title('Daily Update App')
    st.write('Welcome to the daily update app!')

    data = fetch_data()

    # Display the fetched data
    st.write('Fetched Data:')
    st.write(data)

if __name__ == '__main__':
    main()