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
    titles = []

    for entry in data:
        orgs.append(entry['organisaatio'])
        titles.append(entry['tyotehtava'])

    org_freq = {}
    title_freq = {}

    for org in orgs:
        org_freq[org] = org_freq.get(org, 0) + 1
    
    for title in titles:
        title_freq[title] = title_freq.get(title, 0) + 1

    max_org = None
    max_org_count = -1
    for org, count in org_freq.items():
        if count > max_org_count:
            max_org = org
            max_org_count = count
    
    max_title = None
    max_title_count = -1
    for title, count in title_freq.items():
        if count > max_title_count:
            max_title = title
            max_title_count = count

    return {
        'most_common_organization': max_org,
        'most_common_job_title': max_title
    }

def job_posting_analysis(data):
    org_counts = {}

    for entry in data:
        org = entry['organisaatio']
        org_counts[org] = org_counts.get(org, 0) + 1

    count_values = list(org_counts.values())

    total = 0
    for val in count_values:
        total += val
    average = total / len(count_values)

    # Manual min/max
    min_val = min(count_values)
    max_val = max(count_values)

    # Standard deviation
    variance = 0
    for val in count_values:
        variance += (val - average) ** 2
    stddev = (variance / len(count_values)) ** 0.5

    return {
        'total_postings': total,
        'average': average,
        'min': min_val,
        'max': max_val,
        'stddev': stddev,
        'organization_counter': org_counts
    }

def generate_reports(data, summary, analysis, txt_file, csv_file):
    try:
        with open(txt_file, 'w') as txt, open(csv_file, 'w') as csv:
            
            # For txt file
            txt.write(f"Total number of entries: {count_entries(data)}\n")
            txt.write(f"Most common organization: {summary['most_common_organization']}\n")
            txt.write(f"Most common job title: {summary['most_common_job_title']}\n\n")
            
            #For CSV file
            csv.write("Key,Value\n")
            csv.write(f"Total Entries,{count_entries(data)}\n")
            csv.write(f"Most Common Organization,{summary['most_common_organization']}\n")
            csv.write(f"Most Common Job Title,{summary['most_common_job_title']}\n")
            
            
            # Job Posting Stats
            txt.write("Job Posting Analysis by organization\n")
            txt.write("======================================\n")
            txt.write(f"{'Metric':<35}{'Value':>10}\n")
            txt.write("-" * 45 + "\n")
            txt.write(f"{'Total postings':<35}{analysis['total_postings']}\n")
            txt.write(f"{'Average postings per organization':<35}{analysis['average']:.2f}\n")
            txt.write(f"{'Minimum postings':<35}{analysis['min']}\n")
            txt.write(f"{'Maximum postings':<35}{analysis['max']}\n")
            txt.write(f"{'Standard deviation':<35}{analysis['stddev']:.2f}\n\n")

            csv.write(f"Total Postings,{analysis['total_postings']}\n")
            csv.write(f"Average,{analysis['average']:.2f}\n")
            csv.write(f"Minimum,{analysis['min']}\n")
            csv.write(f"Maximum,{analysis['max']}\n")
            csv.write(f"Standard Deviation,{analysis['stddev']:.2f}\n")

            
    except Exception as e:
        print(f"Error generating reports: {e}")

# Testing the function
if __name__ == "__main__":
    url = 'http://gis.vantaa.fi/rest/tyopaikat/v1/kaikki'
    data = load_json(url)
    
    if data:
        print(f"Number of entries: {count_entries(data)}")
        summary_statistics = calculate_summary_statistics(data)
        job_analysis = job_posting_analysis(data)
        
        generate_reports(
            data,
            summary_statistics,
            job_analysis, 
            'report.txt', 
            'report.csv')