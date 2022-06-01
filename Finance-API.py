import requests
import json

#free API key for Alpha Vantage 
api_key = 'I93R4JQEH18ETZOW'

def printJson (data :dict):
    print(json.dumps(data, indent = 4))
    
def fetchData(function: str, symbol: str, api_key: str) -> dict:
    # Use API's web format to fetch data
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    
    #output data in unicode from HTML page
    data = response.text 
    
    #clean retrieve data from JSON
    parsed = json.loads(data)
    return parsed

#function call that returns a dictionary of the API
printJson(fetchData('INCOME_STATEMENT', 'AMZN', api_key))

# how to calculate FCF, (cash - expenses - debt - payouts)
# FCF = EBIT*(1-tax rate) + Depreciation - CAPX - increase in net working capital (non-cash current assets (inventory, non cash equivalents))