import urllib.request
import json
import ssl

def load_json(file_url):
    try:
        context = ssl._create_unverified_context()

        with urllib.request.urlopen(file_url, context=context) as response:
            return json.loads(response.read())
    except Exception as error:
        print(f"\nFailed to load JSON data from URL: {file_url}")
        print(f"Reason: {error}\n")
        print("Please check your internet connection or the URL and try again.\n")
        return None

def count_entries(data):
    return len(data)

def generate_reports(data, txt_file, csv_file):
    try:
        with open(txt_file, 'w') as txt, open(csv_file, 'w') as csv:
            
            # For txt file
            txt.write(f"Total number of entries: {count_entries(data)}\n")
            
            #For CSV file
            csv.write("Key,Value\n")
            csv.write(f"Total Entries,{count_entries(data)}\n")
            
    except Exception as e:
        print(f"Error generating reports: {e}")

# Testing the function
if __name__ == "__main__":
    url = 'http://gis.vantaa.fi/rest/tyopaikat/v1/kaikki'
    data = load_json(url)
    
    if data:
        print(f"Number of entries: {count_entries(data)}")
        generate_reports(data, 'report.txt', 'report.csv')