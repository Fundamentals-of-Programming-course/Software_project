# Analyzing Open Data in JSON Format

## Learning Goals
Through this assignment, you will learn to collaboratively write and test a Python program that processes and analyzes a dataset in JSON format, chosen by your group from an open data source.

---

## Background
Develop a Python-based data analysis program that reads a JSON file, processes it to extract key insights, and writes a summary report. You will use a real-world dataset chosen from [Helsinki Region Infoshare](https://hri.fi/), which provides open datasets in JSON format. The goal is to practice working with files, loops, conditionals, and lists while analyzing data collaboratively.

You will analyze the dataset by calculating summary statistics, such as total entries, average values, or the most frequent occurrences, and present the results in a readable report. If time allows, you can add additional features such as filtering the data by date or further data exploration.

---

## Preparatory Actions
1. **Choose a Dataset**: Visit [Helsinki Region Infoshare](https://hri.fi/) and search for a suitable dataset in JSON format that interests your group. Ensure that the dataset contains structured data suitable for analysis.
   
2. **Create a Repository**: Create a new GitHub repository for your group. You can follow the instructions at [GitHub Docs: Creating a new repository](https://docs.github.com/en/get-started/quickstart/create-a-repo).
   
3. **Protect the Main Branch**: As a group, protect the main branch of your repository by setting up branch protection. Follow the steps in [GitHub Docs: Managing a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule) to require pull requests before merging.

4. **Collaborate via GitHub Issues**: Optionally, use GitHub Issues to divide the workload among your group members. For guidance, see [GitHub Docs: Quickstart for GitHub Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/quickstart).

---

## Workflow Actions
1. **Implement JSON Data Parser**: Write a Python function to load and parse the JSON file chosen by your group. Ensure that you handle any potential errors that may occur when loading the file.
   
2. **Data Analysis Functions**: Implement the following key functions:
   - Count the total number of entries in the dataset.
   - Calculate summary statistics (e.g., average values, most frequent entries).
   - Optionally, add filters for analyzing data by specific conditions (e.g., date range).
   
3. **Report Generation**: Implement a function to write the results of your analysis to a report file (e.g., `report.txt`). The report should summarize key findings, such as total entries, most popular occurrences, and any statistics you calculate.

---

## Testing and Documentation
- Test your program manually or by writing additional test scripts if necessary. Ensure that all code is properly documented and each function is well-commented to explain its purpose and logic.

- Before submitting the assignment, make sure that all code changes are merged into the main branch of your GitHub repository. Follow instructions on Canvas for submitting your assignment.
