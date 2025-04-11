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

def calculate_summary_statistics(data):
    orgs = []

    for entry in data:
        orgs.append(entry['organisaatio'])

    org_freq = {}

    for org in orgs:
        org_freq[org] = org_freq.get(org, 0) + 1

    max_org = None
    max_org_count = -1
    for org, count in org_freq.items():
        if count > max_org_count:
            max_org = org
            max_org_count = count

    return {
        'most_common_organization': max_org,
    }

def generate_reports(data, summary, txt_file, csv_file):
    try:
        with open(txt_file, 'w') as txt, open(csv_file, 'w') as csv:
            
            # For txt file
            txt.write(f"Total number of entries: {count_entries(data)}\n")
            txt.write(f"Most common organization: {summary['most_common_organization']}\n")
            
            #For CSV file
            csv.write("Key,Value\n")
            csv.write(f"Total Entries,{count_entries(data)}\n")
            csv.write(f"Most Common Organization,{summary['most_common_organization']}\n")
            
    except Exception as e:
        print(f"Error generating reports: {e}")

# Testing the function
if __name__ == "__main__":
    url = 'http://gis.vantaa.fi/rest/tyopaikat/v1/kaikki'
    data = load_json(url)
    
    if data:
        print(f"Number of entries: {count_entries(data)}")
        summary_statistics = calculate_summary_statistics(data)
        
        generate_reports(
            data,
            summary_statistics, 
            'report.txt', 
            'report.csv')