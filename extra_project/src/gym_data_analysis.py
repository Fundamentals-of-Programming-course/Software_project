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

# Generate a report of the analysis results
def generate_report(filename, total_entries, frequent_entries, stats):
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
    

# Testing function 
if __name__ == "__main__":
    json_file = "../json/ulkoliikunta-daily-2021.json"
    data = load_json_file(json_file)
    if data:
        total_entries = count_entries(data)
        
        # Example key for frequent entries and statistics
        frequent = most_frequent_entries(data, "area")
        statistics_data = calculate_statistics(data, "usageMinutes") # should be numeric 
    
    generate_report(
            "gym_data_analysis.txt",
            total_entries,
            frequent,
            statistics_data
        )
    print("Report generated successfully.")