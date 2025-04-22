import urllib.request
import json
import ssl
from datetime import datetime

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

# Function to count the number of entries
# This function takes the data as input and returns the number of entries.
def count_entries(data):
    return len(data)

# Function to calculate summary statistics
# This function takes the data as input and returns a dictionary with the most common organization and job title.
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

# Function to analyze job postings by organization
# This function counts the number of job postings for each organization
# and calculates the total, average, minimum, maximum, and standard deviation of postings.
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

# Filter and count job titles for a specific organization
# This function takes the data and an organization name as input and returns a dictionary with job titles as keys and their counts as values.
# It iterates through the data, checking if the organization matches the input, and updates the counts accordingly.
def filter_and_count_job_titles(data, org_name):
    job_counts = {}
    for entry in data:
        if entry['organisaatio'] == org_name:
            title = entry['tyotehtava']
            job_counts[title] = job_counts.get(title, 0) + 1
    return job_counts

# Function to check application deadlines
# This function checks the application deadlines in the data and returns a dictionary with counts of expired and open postings.
# It uses the datetime module to compare the current date with the deadline date.
def check_application_deadlines(data):
    expired = []
    open_now = []

    for entry in data:
        deadline_str = entry.get('haku_paattyy_pvm')
        if deadline_str:
            try:
                deadline_date = datetime.strptime(deadline_str, "%Y-%m-%d")
                if deadline_date < datetime.today():
                    expired.append(entry)
                else:
                    open_now.append(entry)
            except ValueError:
                print(f"Invalid date format in entry: {deadline_str}")
    
    return {
        "expired_count": len(expired),
        "open_count": len(open_now),
        "expired_postings": expired,
        "open_postings": open_now
    }

# Function to generate reports
# This function generates a text and CSV report based on the data, summary statistics, and job posting analysis.
def generate_reports(data, summary, analysis, specific_org, job_titles, txt_file, csv_file):
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
            txt.write("=" * 45 + "\n")
            txt.write(f"{'Statistics':<35} | {'Value'}\n")
            txt.write("-" * 45 + "\n")
            txt.write(f"{'Total postings':<35} | {analysis['total_postings']}\n")
            txt.write(f"{'Average postings per organization':<35} | {analysis['average']:.2f}\n")
            txt.write(f"{'Minimum postings':<35} | {analysis['min']}\n")
            txt.write(f"{'Maximum postings':<35} | {analysis['max']}\n")
            txt.write(f"{'Standard deviation':<35} | {analysis['stddev']:.2f}\n\n")

            csv.write(f"Total Postings,{analysis['total_postings']}\n")
            csv.write(f"Average,{analysis['average']:.2f}\n")
            csv.write(f"Minimum,{analysis['min']}\n")
            csv.write(f"Maximum,{analysis['max']}\n")
            csv.write(f"Standard Deviation,{analysis['stddev']:.2f}\n")
            
           ## Job postings by organization 
            txt.write("Postings by each organization:\n")
            txt.write("=" * 100 + "\n")
            txt.write(f"{'Organization':<50}{'Number of job posted':>10}\n")
            txt.write("-" * 100 + "\n")
            csv.write("Organization,Number of job posted\n")
            
            # Sort the organizations by count in descending order
            # This is done by creating a list of tuples and sorting it
            org_items = list(analysis['organization_counter'].items())
            for i in range(len(org_items)):
                for j in range(i + 1, len(org_items)):
                    if org_items[i][1] < org_items[j][1]:
                        org_items[i], org_items[j] = org_items[j], org_items[i]
            
            # Write the sorted organizations to the text and CSV files
            for org, count in org_items:
                txt.write(f"{org:<50}{count:>10}\n")
                csv.write(f"\"{org}\",{count}\n")

            # Job titles posted by a specific organization
            txt.write(f"\nJob titles posted by '{specific_org}'\n")
            txt.write("=" * 100 + "\n")
            txt.write(f"{'Job Title':<50}{'Number of job posted':>10}\n")
            txt.write("-" * 100 + "\n")
            csv.write(f"\nJob Titles ({specific_org}),Job Title,Number of job posted\n")

            job_items = list(job_titles.items())
            for title, count in job_items:
                txt.write(f"{title:<50}{count:>10}\n")
                csv.write(f"\"{title}\",{count}\n")
                
    except Exception as e:
        print(f"Error generating reports: {e}")

# Function to generate a report of expired job postings
def generate_expired_jobs_report(expired_data, output_file):
    try:
        with open(output_file, 'w') as file:
            
            file.write(f"Total expired job postings: {len(expired_data)}\n")
            file.write("Expired Job Postings\n")
            file.write("=" * 100 + "\n")
            file.write(f"{'Job Title':<35}{'Organization':<35}{'Deadline':>15}\n")
            file.write("-" * 100 + "\n")
            for entry in expired_data:
                title = entry.get('tyotehtava', 'Unknown')
                org = entry.get('organisaatio', 'Unknown')
                deadline = entry.get('haku_paattyy_pvm', 'Unknown')
                file.write(f"{title:<35}| {org:<35}| {deadline:>15}\n")
                
        print(f"Expired job postings written to: {output_file}")
    except Exception as e:
        print(f"Failed to write expired jobs report: {e}")

# Testing the function
if __name__ == "__main__":
    url = 'http://gis.vantaa.fi/rest/tyopaikat/v1/kaikki'
    data = load_json(url)
    
    if data:
        deadlines = check_application_deadlines(data)
        open_data = deadlines['open_postings']
        expired_data = deadlines['expired_postings']
        
        summary_statistics = calculate_summary_statistics(data)
        job_analysis = job_posting_analysis(data)
        specific_org = "Kasvatus ja oppiminen, Toisen asteen koulutus"
        job_titles = filter_and_count_job_titles(data, specific_org)
        
        print(f"Number of entries: {count_entries(data)}")
        
        generate_reports(
            data,
            summary_statistics,
            job_analysis, 
            specific_org,
            job_titles,
            'report.txt', 
            'report.csv')
        
        generate_expired_jobs_report(
            expired_data,
            'expired_jobs.txt')