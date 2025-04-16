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

# Find the most frequent occurrences of a specific key in the dataset
# This function counts the occurrences of each unique value for the specified key and returns the top 5 most common entries.
def most_frequent_entries(data, key):
    freq_dict = {}
    for entry in data:
        if key in entry:
            val = entry[key]
            if val in freq_dict:
                freq_dict[val] += 1
            else:
                freq_dict[val] = 1
    sorted_freq = []
    for k in freq_dict:
        inserted = False
        for i in range(len(sorted_freq)):
            if freq_dict[k] > sorted_freq[i][1]:
                sorted_freq.insert(i, (k, freq_dict[k]))
                inserted = True
                break
        if not inserted:
            sorted_freq.append((k, freq_dict[k]))
    return sorted_freq[:5]  # Top 5 most common entries

# Calculate summary statistics for a given numeric key in the dataset
# This function computes the average, maximum, minimum, median, and standard deviation for the specified key.
def calculate_statistics(data, key):
    values = []
    for entry in data:
        if key in entry:
            try:
                values.append(float(entry[key]))
            except ValueError:
                continue
            
    # Calculate average, maximum, minimum, median, and standard deviation
    if values:
        avg = sum(values) / len(values)
        max_value = max(values)
        min_value = min(values)
        median_value = sorted(values)[len(values) // 2] if len(values) % 2 != 0 else (sorted(values)[len(values) // 2 - 1] + sorted(values)[len(values) // 2]) / 2
        std_dev = (sum([(x - avg) ** 2 for x in values]) / len(values)) ** 0.5
        return {
            "Average": round(avg,2),
            "Maximum": max_value,
            "Minimum": min_value,
            "Median": median_value,
            "Standard deviation": round(std_dev,2)
        }
    return {}

# Filter the dataset based on a date range and two specific key-value pairs
# This function returns entries that fall within the specified date range and match the given key-value pairs.
def filter_by_date_and_key(data, 
    date_key, start_date, end_date, 
    filter_key, filter_value, 
    filter_key2, filter_value2
    ):
    filtered_data = []
    for entry in data:
        
        if (date_key in entry and filter_key in entry) and (date_key in entry and filter_key2 in entry):
            date_value = entry[date_key]
            if (start_date <= date_value <= end_date and entry[filter_key] == filter_value) and (start_date <= date_value <= end_date and entry[filter_key2] == filter_value2):
                filtered_data.append(entry)
    return filtered_data

# Get all unique key from the dataset, for example groupId
# This function returns a sorted list of unique group IDs found in the dataset.
# Note: This function is not used in the main analysis but can be useful for further analysis.
def get_all_group_ids(data):
    return sorted(set(entry.get("groupId") for entry in data if "groupId" in entry))


# Generate a report of the analysis results
def generate_report(filename, total_entries, frequent_entries, stats, filtered_data,count_appearance, group_ids ):
    with open(filename, 'w') as report:
        report.write(f"Total Entries: {total_entries}\n")
        
        # Writing table header for frequent entries if available
        if frequent_entries:
            report.write("\nThe Most Frequent Entries:\n")
            report.write("=" * 38 + "\n")
            report.write(f"{'Area':<25} {'Frequency':>10}\n")
            report.write("-" * 38 + "\n")
            for entry in frequent_entries:
                if len(entry) == 2:
                    location, count = entry
                    report.write(f"{location:<25} {count:>10}\n")
        
        # Writing table header for statistics 
        if stats:
            report.write("\nSummary Statistics on usageMinutes:\n")
            report.write("=" * 38 + "\n")
            report.write(f"{'Statistics':<25} {'Value':>10}\n")
            report.write("-" * 38 + "\n")
            
            # Writing table rows for statistics
            for stat, value in stats.items():
                report.write(f"{(stat):<25} {(value):>10}\n")
        
         # Writing table header for filtered data if available         
        if filtered_data:
            first_entry = filtered_data[0]
            headers = list(first_entry.keys())
            filer_name = "FILTERED DATA"
            report.write(f"\n{filer_name:>50}\n")
            report.write("=" * 100 + "\n")
            report.write(f"{headers[0]:<25} {headers[1]:>20} {headers[2]:>20} {headers[4]:>20}\n")
            report.write("-" * 100 + "\n")
            
            # Writing table rows
            for entry in filtered_data:
                if len(headers) >= 2:
                    report.write(f"{str(entry.get(headers[0], '')):<25} {str(entry.get(headers[1], '')):>20} {str(entry.get(headers[2], '')):>20}{str(entry.get(headers[4], '')):>20}\n")

        # Writing the number of appearance
        report.write("\nThe number of appearance:\n")
        report.write("=" * 35 + "\n")
        for key, values in count_appearance.items():
            report.write(f"{key}: {values}\n")
        
        # Writing all unique key for example: groupIds
        report.write("\nAll Unique Group IDs:\n")
        report.write("=" * 35 + "\n")
        for gid in group_ids:
            report.write(f"{gid}\n")
            

# Testing function 
if __name__ == "__main__":
    json_file = "../json/ulkoliikunta-daily-2021.json"
    data = load_json_file(json_file)
    if data:
        total_entries = count_entries(data)
        
        # Example key for frequent entries and statistics
        frequent = most_frequent_entries(data, "area")
        statistics_data = calculate_statistics(data, "usageMinutes") # should be numeric 
        
        # Filter data for a specific date range and two specific key-value pairs
        # Note: Ensure that the date format in the dataset matches the format used in the filter
        filtered_data = filter_by_date_and_key(data, 
                        "utcdate", "2021-08-01T00:00:00.000Z", "2021-08-31T23:59:59.999Z", 
                        "groupId", "OG10", 
                        "area", "Hietaniemi"
                   )
        filtered_entries_count = count_entries(filtered_data)
        count_appearance = {"Number of filtered entries": filtered_entries_count}
        
        # Get unique value in a specific key
        group_ids = get_all_group_ids(data)
    
    generate_report(
            "gym_data_analysis.txt",
            total_entries,
            frequent,
            statistics_data,
            filtered_data,
            count_appearance,
            group_ids
        )
    print("Report generated successfully.")