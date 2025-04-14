
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
Unit tests are provided in test_project.py to ensure the correctness of each function in data_analysis.

### ▶ Requirements
pytest must be installed:
```bash
pip install pytest
```

### ▶ Run the tests
Use the following command in your terminal from the project root:
```bash
pytest -v test_project.py
```
+ This will:
   + Test counting entries
   + Verify the most common organization and job title
   + Check statistical analysis
   + Confirm filtering by organization
   + Validate deadline handling (open vs. expired)

## License

This script is intended for academic and educational purposes. Data usage should comply with the [City of Vantaa](http://gis.vantaa.fi) API terms.
