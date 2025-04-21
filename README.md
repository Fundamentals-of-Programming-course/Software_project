# Software project with Python

## Table of content

- [Job Postings Analyzer](#job-postings-analyzer)
  + [Usage](#usage)
  + [API Source](#usage)
  + [Functions Overview](#functions-overview)
  + [Output Example](#output-example)
- [Gym Data Analysis (Extra_project)](#gym-data-analysis-extra_project)
  + [Dataset](#dataset)
  + [Features](#features)
  + [Usage](#usage-1)
  + [Example Report Output](#example-report-output)

- [File Structure](#file-structure)



# Job Postings Analyzer

This Python script analyzes public job postings from the City of Vantaa's open API. It fetches job data, computes summary statistics, filters job titles, and checks for expired application deadlines. Results are saved in `.txt` and `.csv` reports.

## Features

- 📥 Fetch job data from a live JSON API
- 📊 Count total job entries
- 🏢 Identify most common organizations and job titles
- 📈 Analyze statistics: total, average, min, max, and standard deviation of job postings
- 🔍 Filter job titles by organization
- ⏳ Check open and expired job application deadlines
- 📝 Generate detailed reports

## Requirements

- Python 3.x
- Libraries:
  - `json` (built-in)
  - `ssl` (built-in)
- Internet access (to retrieve live job data)

## Usage

1. Run the script:
   ```bash
   python project/src/data_analysis.py
   ```

2. Output files will be generated:
   - `report.txt` – Human-readable summary report
   - `report.csv` – CSV-formatted summary
   - `expired_jobs.txt` – Expired job postings

## API Source

Data is retrieved from:
```
http://gis.vantaa.fi/rest/tyopaikat/v1/kaikki

Example data entry:
  {
      "id": 1,
      "organisaatio": "Kasvatus ja oppiminen, Varhaiskasvatus",
      "ammattiala": "Varhaiskasvatuksen opettaja ja sosionomi",
      "tyotehtava": "Varhaiskasvatuksen kehittäjäopettaja",
      "tyoavain": "https://vantaa.rekrytointi.com/paikat/?o=A_RJ&jgid=1&jid=16818",
      "osoite": "",
      "haku_paattyy_pvm": "2025-04-25",
      "x": 25.002805874123947,
      "y": 60.33124036740038,
      "linkki": "https://vantaa.rekrytointi.com/paikat/?o=A_RJ&jgid=1&jid=16818"
    },
    {
      "id": 2,
      "organisaatio": "Kasvatus ja oppiminen, Perusopetus",
      "ammattiala": "Opetusala",
      "tyotehtava": "Erityisluokanopettaja, Martinlaakson koulu",
      "tyoavain": "https://vantaa.rekrytointi.com/paikat/?o=A_RJ&jgid=1&jid=16576",
      "osoite": "Martinlaaksonpolku 9, 01620 Vantaa",
      "haku_paattyy_pvm": "2025-04-24",
      "x": 24.845235172807822,
      "y": 60.27659037213999,
      "linkki": "https://vantaa.rekrytointi.com/paikat/?o=A_RJ&jgid=1&jid=16576"
    },
```

## Functions Overview

| Function | Purpose |
|---------|---------|
| `load_json(url)` | Load JSON data from a URL |
| `count_entries(data)` | Count total entries in data |
| `calculate_summary_statistics(data)` | Get most common organization and job title |
| `job_posting_analysis(data)` | Analyze statistical data by organization |
| `filter_and_count_job_titles(data, org_name)` | Count job titles within a specific organization |
| `check_application_deadlines(data)` | Identify open and expired job postings |
| `generate_reports(...)` | Create text and CSV reports |
| `generate_expired_jobs_report(expired_data, output_file)` | List all expired job entries |

## Output Example

- **report.txt**
  ```
  Total number of entries: 200
  Most common organization: Education Services
  Most common job title: Teacher

  Job Posting Analysis by organization
  =============================================
  Total postings..........................     835
  Average postings per organization.......    27.83
  Minimum postings.........................      1
  Maximum postings.........................    153
  Standard deviation.......................    34.52
  ```
- **Postings by each organization:**

  ============================================================
  | Organization                                              | Postings |
  |-----------------------------------------------------------|----------|
  | Kasvatus ja oppiminen, Perusopetus                        | 108      |
  | Kasvatus ja oppiminen, Varhaiskasvatus                    | 45       |
  | Vanda stad, Fostran och lärande, Svenskspråkiga servicen  | 8        |
  | Kasvatus ja oppiminen, Toisen asteen koulutus             | 4        |
  | Vanda stad, Fostran och lärande, Grundläggande utbildningen | 3      |
  | Kaupunkikulttuuri ja hyvinvointi, Kulttuuri- ja kirjastopalvelut | 3   |
  | Kaupunkiympäristö, Kiinteistöt ja tilat                   | 2        |
  | Kaupunkikulttuuri ja hyvinvointi, Elinikäinen oppiminen   | 2        |
  | Kaupunkiympäristö, Kaupunkirakenne ja ympäristö           | 2        |
  | Konserninjohto ja elinvoima, Henkilöstöpalvelut           | 2        |
  | Vantaan kaupunki                                          | 1        |
 

- **Job titles posted by 'Kasvatus ja oppiminen, Perusopetu**

========================================================================
| Job Title                                                |  Number of job posted |
|-----------------------------------------------------------|----------|
| Matematiikan lehtorin sijaisuus lukuvuodeksi, Martinlaakson koulu                        | 1    |
| Päätoiminen tuntiopettaja, resurssiopettaja, Askiston koulu                    | 1       |
| Erityisluokanopettaja (vammaisopetus) Kartanonkosken koulu  | 1        |
| Luokanopettaja, Jokiniemen koulu             | 2        |
| Erityisluokanopettaja, Jokiniemen koulu  | 1      |
| Päätoiminen tuntiopettaja, suomi toisena kielenä, Jokiniemen koulu| 1   |
| Lehtori (matematiikka, fysiikka, yhteiskuntaoppi), Peltolan koulu                   | 1        |

- **expired_jobs.txt**
  ```
  Expired Job Postings
  ==============================================================================
  Job Title                       Organization                     Deadline
  ------------------------------------------------------------------------------
  Kindergarten Teacher            Early Childhood Services         2024-11-30
  ```

## Notes

- Deadlines are compared using the system’s current date (`datetime.today()`).
- Any invalid dates in the dataset are caught and reported.
- The script does not require external libraries beyond Python's standard library.


## 🧪 Running Tests
Unit tests are provided in test_data_analysis.py to ensure the correctness of each function in data_analysis.

### ▶ Requirements
pytest must be installed:
```bash
pip install pytest
```

### ▶ Run the tests
Use the following command in your terminal from the project root:
```bash
# Run the tests with this on root terminal 
pytest -v extra_project/test/test_data_analysis.py 
```
+ This will:
   + Test counting entries
   + Verify the most common organization and job title
   + Check statistical analysis
   + Confirm filtering by organization
   + Validate deadline handling (open vs. expired)


---
# Gym Data Analysis (Extra_project) 

This Python project analyzes JSON data from outdoor gym equipment usage in various locations. It generates statistical summaries, identifies the most frequent usage areas, filters entries by conditions, and outputs the results into a formatted report file.

## Dataset
## 📁 Dataset

The data is sourced from:
- File: `ulkoliikunta-daily-2021.json`
- Content: Daily usage logs of outdoor gym equipment including:
  - `utcdate`
  - `area`
  - `groupId`
  - `trackableId`
  - `usageMinutes`
  - `sets`
  - `repetitions`

```
  {
    "utcdate": "2021-05-24T00:00:00.000Z",
    "area": "Hietaniemi",
    "groupId": "OG10",
    "trackableId": "OG10_10268",
    "usageMinutes": 265,
    "sets": 230,
    "repetitions": 1729
  },
  {
    "utcdate": "2021-05-24T00:00:00.000Z",
    "area": "Hietaniemi",
    "groupId": "OG23",
    "trackableId": "OG23_10270",
    "usageMinutes": 236,
    "sets": 188,
    "repetitions": 4185
  },
```

## Features
## 🔧 Features

- Load and parse JSON data with error handling
- Count total entries
- Identify the 5 most frequent entries by a given key (e.g. area or groupId)
- Calculate summary statistics (`average`, `max`, `min`, `median`, `standard deviation`) for numeric fields
- Filter data based on:
  - Date range
  - Two specific field values (e.g. `groupId = OG10` and `area = Hietaniemi`)
- Get all unique `groupId` values
- Generate a well-structured analysis report (`gym_data_analysis.txt`)

## Usage

1. Run the script:
   ```bash
   python exatra_project/src/gym_data_analysis.py
   ```

2. Output files will be generated:
- A text report: `gym_data_analysis.txt`
- Printed message: `Report generated successfully.`


## 📝 Report Contents

- Total entry count
- Most frequent areas
- Summary statistics of `usageMinutes`
- Filtered entries for selected groupId and area
- Unique groupId values in dataset

---

## 📌 Requirements

- Python 3+
- No external dependencies required (uses built-in `json`)

---

## Example Report Output
## 📄 Example Report Output
Here’s a sample output from `gym_data_analysis.txt`:
```text
Example of `gym_data_analysis.txt` Output:

---------------------------------------------------
Total Entries: 3

The Most Frequent Entries:
======================================
Area                      Frequency
--------------------------------------
Hietaniemi                      2
Pirkkola                        1

Summary Statistics on usageMinutes:
======================================
Statistics               Value
--------------------------------------
Average                   120.0
Maximum                   150
Minimum                   90
Median                    120.0
Standard deviation        24.49

                             FILTERED DATA
====================================================================================================
utcdate                        area               groupId          usageMinutes
----------------------------------------------------------------------------------------------------
2021-08-15T00:00:00.000Z    Hietaniemi                OG10                120
2021-08-20T00:00:00.000Z    Hietaniemi                OG10                150

The number of appearance:
===================================
Number of filtered entries: 2

All Unique Group IDs:
===================================
OG10
OG23
```

## 🧪 Tests

Pytest unit tests are provided for:
- JSON loading
- Entry counting
- Frequency analysis
- Summary statistics
- Filtering by key/date
- Unique `groupId` extraction

To run tests:

```bash
# Run the tests with this on root terminal 
pytest -v extra_project/test/test_gym_data_analysis.py 
```
---
# File Structure
## 📂 File Structure

```
extra_project/
│
├── json/
│   └── ulkoliikunta-daily-2021.json  # Input dataset
│
├── src/
│   └── gym_data_analysis.py      # Main script in extra_project
│   └── gym_data_analysis.txt     # Output report
│
├── test/
│   ├── __init__.py
│   └── test_gym_data_analysis.py   # Unit tests using pytest
│
project/
│
├── json/
│   └── data.json
│
├── src/
│   ├── __init__.py
│   ├── data_analysis.py   # Main script in project
│   ├── expired_jobs.txt   # Output report
│   ├── report.csv         # Output report
│   └── report.txt         # Output report
│
├── tests/
│   ├── __init__.py
│   └── test_data_analysis.py  # Unit tests using pytest
│
├── README.md    # Project description
└──  Task.md     # Tasks description
```


## ✨ Credits

Created for an educational project at Laurea University of Applied Sciences.
## License

This script is intended for academic and educational purposes. Data usage should comply with the [City of Vantaa](http://gis.vantaa.fi) API terms.
