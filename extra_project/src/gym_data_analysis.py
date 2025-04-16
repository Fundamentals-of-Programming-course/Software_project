import json

def load_json_file(filename):
    # Load and parse a JSON file, handling errors.
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except (json.JSONDecodeError, FileNotFoundError, IOError) as error:
        print(f" Error loading JSON file: {error}")
        return None

# Count the total number of entries in the dataset
def count_entries(data):
    return len(data)

def generate_report(filename, total_entries):
    with open(filename, 'w', encoding='utf-8') as report:
        report.write(f"Total Entries: {total_entries}\n")

# Testing function 
if __name__ == "__main__":
    json_file = "../json/ulkoliikunta-daily-2021.json"
    data = load_json_file(json_file)
    if data:
        total_entries = count_entries(data)
    
    generate_report(
            "gym_data_analysis.txt",
            total_entries 
        )
    print("Report generated successfully.")