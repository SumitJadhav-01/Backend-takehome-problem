# PubMed Paper Fetcher
## `Here all Documentation and Code`
##### `OVERVIEW`
This program consists of two Python scripts, pubmed_fetcher.py and cli.py, designed to fetch research papers from PubMed based on a search query. It retrieves paper details such as authors, affiliations, and publication dates, and saves the data in a CSV file or displays it in the console.
##### `CODE ORGANIZATION`
- 1. File 1: pubmed_fetcher.py
This module contains functions for interacting with the PubMed API, processing the fetched data, and saving the results in a structured format.
 `Functions`
```
**1. fetch_ids(query: str) -> List[str]**
```
Purpose: Fetches PubMed IDs (PMIDs) for a given search query.

Parameters:query (str): The search query string.

Returns: A list of PubMed IDs (List[str]).

```
**2. get_paper_details(ids: List[str]) -> List[Dict[str, Optional[str]]]**
```
Purpose: Fetches detailed information about papers using their PMIDs.

Parameters:ids (List[str]): A list of PubMed IDs.

Returns: A list of dictionaries containing paper details.

```
**3. parse_xml(xml_data: str) -> List[Dict[str, Optional[str]]]**
```
Purpose: Parses XML data returned by PubMed API to extract paper metadata.

Parameters:xml_data (str): XML string containing paper data.

Returns: A list of dictionaries with metadata such as title, authors, and affiliations.

```
**4. save_csv(filename: str, papers: List[Dict[str, Optional[str]]]) -> None**
```
Purpose: Saves paper details to a CSV file.

Parameters:filename (str): Name of the output CSV file.

papers `(List[Dict[str, Optional[str]]])`: A list of dictionaries containing paper details.


- 2. File 2: cli.py


This script serves as the command-line interface for interacting with the PubMed Fetcher functionality.


`Functions`
```
**1. setup_logging(debug: bool) -> None**
```
Purpose: Configures the logging level.

Parameters:debug (bool): If True, sets the logging level to DEBUG. Otherwise, sets it to INFO.

```
**2. main() -> None**
```
Purpose: Main entry point for the script. Processes command-line arguments and coordinates data fetching and output.

Functionality:

Parses command-line arguments (query, output file, and debug mode).

Fetches PubMed IDs using the fetch_ids function.

Retrieves paper details with the get_paper_details function.

Saves results to a file using save_csv or displays them on the console.


##### `INSTALLATION AND EXECUTION INSTRUCTIONS`


To execute the provided Python scripts (pubmed_fetcher.py and cli.py), follow the step-by-step guide below.
- 1. Prerequisites
Python Installed: Ensure you have Python 3.6 or later installed on your system. You can download it from python.org.

Pip Installed: Pip usually comes with Python. You can verify by running:
```
pip --version

```
Internet Connection: Required for fetching data from PubMed.
- 2. Setting Up the Project
1. Clone the Repository
```
 git clone https://github.com/SumitJadhav-01/Backend-takehome-problem.git
 
 cd  Backend-takehome-problem
 
 cd pubmed_fetcher
```
- 3. Install Dependencies:
The scripts rely on the requests library for making HTTP requests. Install it using pip:
Now, run the following command to install the dependencies listed in your pyproject.toml:
```
poetry install
```
- 4. Executing the Scripts
 After the installation, you can execute the get-papers-list command from the command line. Poetry will automatically use the cli.py script and pass the arguments you provide:
*a. Basic Usage*
To fetch papers related to a specific query and display them in the console:

 ```
poetry run get-papers-list "your search query"
```
Example:
 
poetry run get-papers-list "machine learning" 
*b. Saving Results to a CSV File*
To save the fetched papers to a CSV file, use the -f or --file option followed by the desired filename.

 ```
poetry run get-papers-list "your search query" -f <filename>.csv
```
Example:
 
poetry run get-papers-list "machine learning" -f results.csv

*c. Enabling Debug Mode*
For more detailed logging (useful for troubleshooting), enable debug mode with the -d or --debug flag.

```
poetry run get-papers-list "your search query"-d
```
Example:
 
poetry run get-papers-list "genomics" -d
*d. Combining Options*
You can combine options to save results to a file and enable debug mode simultaneously.

 ```
poetry run get-papers-list "your search query" -f output.csv -d
```
Example:

poetry run get-papers-list  "CRISPR technology" -f crispr_papers.csv -d
*e. Full Command Syntax*
```
poetry run get-papers-list query [-f FILE] [-d]
```
query: (Required) The search term for PubMed.

-f, --file: (Optional) Specify the filename to save the results as a CSV.

-d, --debug: (Optional) Enable debug mode for detailed logs.

- 5. Example Workflow
Let's go through a complete example where we search for papers related to "artificial intelligence in medicine" and save the results to a file named ai_medicine_papers.csv with debug logging enabled.
*a. Run the Command*
```
poetry run get-papers-list "artificial intelligence in medicine" -f ai_medicine_papers.csv -d
```
*b. Expected Output*
Console Output: Detailed logs due to debug mode, including information about fetching IDs and paper details.

CSV File: A file named ai_medicine_papers.csv will be created in the project directory containing the fetched paper details with the following columns:

PMID,
Title,
Date,
Authors,
Companies,
Email,

*c. Viewing the Results*
Open the ai_medicine_papers.csv file using any spreadsheet application (e.g., Microsoft Excel, Google Sheets) or a text editor to view the fetched PubMed articles
##### `Tools and Libraries Used`
1. Requests Library

Purpose: requests is a popular Python library used for making HTTP requests. In this program, it is used to interact with the PubMed API to fetch PubMed IDs and retrieve detailed information about research papers.

2. Argparse Library

Purpose: argparse is a built-in Python library for parsing command-line arguments, enabling the user to run the program with custom parameters. In this project, it allows the user to specify the PubMed search query and control other options like file saving and debug mode.

Documentation: https://docs.python.org/3/library/argparse.html

3.XML Parsing with xml.etree.ElementTree

Purpose: xml.etree.ElementTree is a built-in Python module for parsing and manipulating XML data. This library is used in the project to parse XML responses from PubMed and extract relevant information like authors, affiliations, and publication dates.

Documentation: https://docs.python.org/3/library/xml.etree.elementtree.html

4. Logging

Purpose: The built-in Python logging module is used to log messages, providing insight into the program’s execution. It is helpful for debugging, tracking the flow of the program, and diagnosing issues.

Documentation: https://docs.python.org/3/library/logging.html

5. CSV Module

Purpose: The built-in csv module is used for reading from and writing to CSV files. In this project, it's used to save the fetched PubMed paper details into a CSV file format

Documentation: https://docs.python.org/3/library/csv.html


6. Regular Expressions with re

Purpose: The re module provides support for working with regular expressions. It is used in the project to filter out university or institute affiliations from the list of authors' affiliations.

Documentation: https://docs.python.org/3/library/re.html

7. Type Hinting

Purpose: Type hinting is used throughout the code to indicate expected data types for function parameters and return values, improving readability, maintainability, and enabling type checking tools.

Documentation: https://docs.python.org/3/library/typing.html


8. Virtual Environments

Purpose: Virtual environments allow the program to run with a controlled set of dependencies, isolated from other Python projects. This is particularly important for avoiding version conflicts between libraries.

Documentation: https://docs.python.org/3/library/venv.html
