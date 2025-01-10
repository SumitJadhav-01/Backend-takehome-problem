# PubMed Paper Fetcher
## `Here all Documentation and Code`
##### `OVERVIEW`
This program consists of two Python scripts, pubmed_fetcher.py and cli.py, designed to fetch research papers from PubMed based on a search query. It retrieves paper details such as authors, affiliations, and publication dates, and saves the data in a CSV file or displays it in the console.
##### `CODE ORGANIZATION`
- 1. File 1: pubmed_fetcher.py
This module contains functions for interacting with the PubMed API, processing the fetched data, and saving the results in a structured format.
 `Functions`

**1. fetch_ids(query: str) -> List[str]**

Purpose: Fetches PubMed IDs (PMIDs) for a given search query.

Parameters:query (str): The search query string.

Returns: A list of PubMed IDs (List[str]).


**2. get_paper_details(ids: List[str]) -> List[Dict[str, Optional[str]]]**

Purpose: Fetches detailed information about papers using their PMIDs.

Parameters:ids (List[str]): A list of PubMed IDs.

Returns: A list of dictionaries containing paper details.


**3. parse_xml(xml_data: str) -> List[Dict[str, Optional[str]]]**

Purpose: Parses XML data returned by PubMed API to extract paper metadata.

Parameters:xml_data (str): XML string containing paper data.

Returns: A list of dictionaries with metadata such as title, authors, and affiliations.


**4. save_csv(filename: str, papers: List[Dict[str, Optional[str]]]) -> None**

Purpose: Saves paper details to a CSV file.

Parameters:filename (str): Name of the output CSV file.

papers (List[Dict[str, Optional[str]]]): A list of dictionaries containing paper details.





- 2. File 2: cli.py


This script serves as the command-line interface for interacting with the PubMed Fetcher functionality.


`Functions`

**1. setup_logging(debug: bool) -> None**

Purpose: Configures the logging level.

Parameters:debug (bool): If True, sets the logging level to DEBUG. Otherwise, sets it to INFO.


**2. main() -> None**

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
pip --version
Internet Connection: Required for fetching data from PubMed.
- 2. Setting Up the Project
1. Clone the Repository

 git clone https://github.com/your-username/pubmed-fetcher.git
 
cd pubmed-fetcher

- 3. Install Required Python Packages
The scripts rely on the requests library for making HTTP requests. Install it using pip:
pip install requests
If you plan to manage dependencies more robustly, consider using a virtual environment:
#Create a virtual environment
python -m venv venv

#Activate the virtual environment

#On Windows:
venv\Scripts\activate

#On macOS/Linux:
source venv/bin/activate

#Install dependencies within the virtual environment
pip install requests
- 4. Executing the Scripts
The cli.py script is the main entry point that utilizes functions from pubmed_fetcher.py to fetch and display or save PubMed articles based on a search query.
*a. Basic Usage*
To fetch papers related to a specific query and display them in the console:

 
python cli.py "your search query"

Example:
 
python cli.py "cancer research"
*b. Saving Results to a CSV File*
To save the fetched papers to a CSV file, use the -f or --file option followed by the desired filename.

 
python cli.py "your search query" -f results.csv

Example:
 
python cli.py "machine learning in healthcare" -f ml_healthcare_papers.csv
*c. Enabling Debug Mode*
For more detailed logging (useful for troubleshooting), enable debug mode with the -d or --debug flag.

 
python cli.py "your search query" -d

Example:
 
python cli.py "genomics" -d
*d. Combining Options*
You can combine options to save results to a file and enable debug mode simultaneously.

 
python cli.py "your search query" -f output.csv -d

Example:

 
python cli.py "CRISPR technology" -f crispr_papers.csv -d
*e. Full Command Syntax*
python cli.py query [-f FILE] [-d]

query: (Required) The search term for PubMed.

-f, --file: (Optional) Specify the filename to save the results as a CSV.

-d, --debug: (Optional) Enable debug mode for detailed logs.
- 5. Example Workflow
Let's go through a complete example where we search for papers related to "artificial intelligence in medicine" and save the results to a file named ai_medicine_papers.csv with debug logging enabled.
*a. Run the Command*
python cli.py "artificial intelligence in medicine" -f ai_medicine_papers.csv -d

*b. Expected Output*
Console Output: Detailed logs due to debug mode, including information about fetching IDs and paper details.

CSV File: A file named ai_medicine_papers.csv will be created in the project directory containing the fetched paper details with the following columns:

PMID
Title
Date
Authors
Companies
Email
*c. Viewing the Results*
Open the ai_medicine_papers.csv file using any spreadsheet application (e.g., Microsoft Excel, Google Sheets) or a text editor to view the fetched PubMed articles.
- 6. Troubleshooting
Module Not Found Error: Ensure both pubmed_fetcher.py and cli.py are in the same directory. Also, verify that you're running the command from within that directory.

Missing Dependencies: If you encounter issues related to missing Python packages, ensure you've installed all required packages using pip.

Network Issues: Since the scripts fetch data from the internet, ensure you have a stable internet connection. Also, check if your firewall or network settings are blocking HTTP requests to PubMed's API.

Invalid Query Results: If no papers are found, try refining your search query for better results.
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


### `code explanation of 2 files`

This notebook demonstrates how to fetch research papers from PubMed using their API.
It is divided into two main parts:

1. `pubmed_fetcher.py`: This module fetches PubMed IDs, retrieves paper details, and saves them into a CSV file.
2. `cli.py`: This is the command-line interface for interacting with the `pubmed_fetcher.py` module, allowing users to fetch papers via a query and save them into a CSV file.

 The workflow includes fetching PubMed IDs based on a search query, retrieving detailed information about the papers, and parsing their metadata such as title, authors, date, and affiliations. Additionally, the data can be saved in CSV format


### `pubmed_fetcher.py`

This module contains functions that interact with the PubMed API to:

1. **Fetch PubMed IDs**: The `fetch_ids()` function takes a search query and retrieves a list of PubMed IDs.
2. **Get Paper Details**: The `get_paper_details()` function fetches detailed paper information for the list of PubMed IDs, such as title, authors, publication date, and email.
3. **Parse XML Response**: The `parse_xml()` function processes XML data from PubMed to extract the relevant information.
4. **Save to CSV**: The `save_csv()` function saves the fetched paper details into a CSV file for further analysis or export.

The module uses **requests** for API calls and **xml.etree.ElementTree** for XML parsing.

This file interacts with PubMed’s API, fetches data about research papers, parses the data, and saves the results into a CSV.
Import Statements


import requests 
import csv
import re
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional         
import requests: Imports the requests library, which allows you to send HTTP requests (like GET or POST requests) to access external APIs like PubMed’s API.

import csv: Imports the csv module, which is used to read and write CSV (Comma Separated Values) files. It allows saving paper data into a .csv file.

import re: Imports the re module, which is used to work with regular expressions for pattern matching and text searching. In this code, it helps filter out university or institute affiliations.

import xml.etree.ElementTree as ET: Imports ElementTree, which is used to parse XML data. PubMed’s API returns paper details in XML format, so we need this library to handle the XML and extract relevant information.

from typing import List, Dict, Optional: These are type hints from the typing module. List, Dict, and Optional are used to specify what type of data the functions will use. This makes the code more readable and helps avoid mistakes.
fetch_ids Function


"""Fetch PubMed IDs for a given query."""
def fetch_ids(query: str) -> List[str]:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
    }
def fetch_ids(query: str) -> List[str]:: This defines a function called fetch_ids, which takes one argument, query (a string). The function returns a list of strings (PubMed IDs).

base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi": This sets the base URL for the PubMed search API.

params = {...}: This dictionary holds the parameters for the API request.

"db": "pubmed": Tells the API to search the PubMed database.

"term": query: This is the search term (query) that the user provides.

"retmode": "json": Requests the results in JSON format.
try:
    response = requests.get(base_url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data["esearchresult"]["idlist"]
except requests.RequestException as e:
    print(f"Error fetching PubMed IDs: {e}")
    return []

try:: This begins a try block that will attempt to make a request to the PubMed API.

response = requests.get(base_url, params=params, timeout=10): This sends a GET request to PubMed’s API with the specified parameters. timeout=10 ensures the request doesn’t hang for more than 10 seconds.

response.raise_for_status(): This checks if the response was successful (status code 200). If not, it raises an exception.

data = response.json(): This converts the JSON response to a Python dictionary.

return data["esearchresult"]["idlist"]: Extracts the list of PubMed IDs (idlist) from the JSON data and returns it.

except requests.RequestException as e:: If any error occurs (like a network failure), it’s caught here.

print(f"Error fetching PubMed IDs: {e}"): Prints an error message.

return []: If there’s an error, the function returns an empty list.
get_paper_details Function
"""Fetch detailed information about papers from PubMed."""

def get_paper_details(ids: List[str]) -> List[Dict[str, Optional[str]]]:
    details_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    if not ids:
        return []

def get_paper_details(ids: List[str]) -> List[Dict[str, Optional[str]]]:: Defines the function get_paper_details, which takes a list of PubMed IDs and returns a list of dictionaries. Each dictionary will hold details about a paper.

details_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi": This is the base URL for fetching detailed information about papers.

if not ids:: Checks if the ids list is empty. If it is, the function returns an empty list because there’s no data to fetch.
ids_str = ",".join(ids)
params = {
        "db": "pubmed",
        "id": ids_str,
        "retmode": "xml",
    }

def get_paper_details(ids: List[str]) -> List[Dict[str, Optional[str]]]:: Defines the function get_paper_details, which takes a list of PubMed IDs and returns a list of dictionaries. Each dictionary will hold details about a paper.

details_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi": This is the base URL for fetching detailed information about papers.

if not ids:: Checks if the ids list is empty. If it is, the function returns an empty list because there’s no data to fetch.
try:
    response = requests.get(details_url, params=params, timeout=10)
    response.raise_for_status()
    return parse_xml(response.text)
except requests.RequestException as e:
    print(f"Error fetching paper details: {e}")
    return []

 response = requests.get(details_url, params=params, timeout=10): Sends the GET request to fetch the paper details.
 
response.raise_for_status(): Raises an error if the response is not successful.

return parse_xml(response.text): Passes the raw XML response to the parse_xml function for processing.

except requests.RequestException as e:: Catches any exceptions and prints an error message.

return []: Returns an empty list if there was an error.
parse_xml Function
"""Parse XML data from PubMed and extract paper details."""

def parse_xml(xml_data: str) -> List[Dict[str, Optional[str]]]:
    root = ET.fromstring(xml_data)
    papers = []

def parse_xml(xml_data: str) -> List[Dict[str, Optional[str]]]:: Defines the function parse_xml, which takes XML data as input and returns a list of dictionaries (one dictionary per paper).

root = ET.fromstring(xml_data): Parses the XML data and returns the root of the XML tree.

papers = []: Initializes an empty list to store the paper details.
for article in root.findall(".//PubmedArticle"):
        paper: Dict[str, Optional[str]] = {}
        paper["PMID"] = article.findtext(".//PMID")
        paper["Title"] = article.findtext(".//ArticleTitle")
        paper["Date"] = None
        paper["Authors"] = []
        paper["Companies"] = []
        paper["Email"] = None

for article in root.findall(".//PubmedArticle"):: Loops through all the <PubmedArticle> elements in the XML data.

paper: Dict[str, Optional[str]] = {}: Initializes a dictionary for storing the details of a paper.

paper["PMID"] = article.findtext(".//PMID"): Extracts the PubMed ID (PMID) from the XML element and stores it in the dictionary.

paper["Title"] = article.findtext(".//ArticleTitle"): Extracts the title of the paper.

paper["Date"] = None, paper["Authors"] = [], paper["Companies"] = [], paper["Email"] = None: Initializes placeholders for other paper details.
        # Extract publication date

date = article.find(".//PubDate")
if date is not None:
    year = date.findtext("Year")
    month = date.findtext("Month")
    day = date.findtext("Day")
    if year and month and day:
        paper["Date"] = f"{year}-{month}-{day}"

date = article.find(".//PubDate"): Finds the <PubDate> element in the article.

if date is not None:: Checks if the <PubDate> element is found.

year, month, day: Extracts the publication year, month, and day.

paper["Date"] = f"{year}-{month}-{day}": If all parts of the date are available, it formats them as YYYY-MM-DD.
        # Extract authors and affiliations

authors = article.findall(".//Author")
for author in authors:
    affiliation = author.findtext("AffiliationInfo/Affiliation")
    if affiliation and not re.search(r"university|institute", affiliation, re.IGNORECASE):
        paper["Authors"].append(author.findtext("LastName"))
        paper["Companies"].append(affiliation)

authors = article.findall(".//Author"): Finds all <Author> elements in the article.

for author in authors:: Loops through each author.

affiliation = author.findtext("AffiliationInfo/Affiliation"): Extracts the author's affiliation (e.g., university or company).

if affiliation and not re.search(r"university|institute", affiliation, re.IGNORECASE):: Checks if the affiliation is not a university or institute (using a regular expression).
paper["Authors"].append(author.findtext("LastName")): Adds the author's last name to the Authors list.

paper["Companies"].append(affiliation): Adds the affiliation to the Companies list.
        # Extract corresponding author email

corresponding = article.find(".//Author[CorrespondingAuthor='Y']")
if corresponding is not None:
    email = corresponding.findtext("AffiliationInfo/AuthorEmail")
    if email:
        paper["Email"] = email

corresponding = article.find(".//Author[CorrespondingAuthor='Y']"): Finds the corresponding author (the one marked with CorrespondingAuthor="Y").

if corresponding is not None:: Checks if a corresponding author is found.

email = corresponding.findtext("AffiliationInfo/AuthorEmail"): Extracts the email of the corresponding author.

if email:: If an email is found, it adds the email to the dictionary.
papers.append(paper)

return papers

papers.append(paper): Adds the paper’s details to the papers list.

return papers: Returns the list of all papers' details.

### `cli.py`

This script serves as the command-line interface for interacting with the `pubmed_fetcher.py` module. It handles the following tasks:

1. **Argument Parsing**: Using `argparse`, the script accepts a search query (`query`), an optional output file name (`--file`), and a debug flag (`--debug`).
2. **Logging**: The `setup_logging()` function configures logging to display debug or informational messages.
3. **Fetch and Display Results**: The `main()` function fetches PubMed IDs using the `fetch_ids()` function, retrieves detailed information about the papers using `get_paper_details()`, and prints or saves the results.

The script is designed to be executed from the command line with various options for flexibility.
This script handles user input from the command line, invokes functions from pubmed_fetcher.py, and displays or saves the results.

Import Statements
import argparse 
import logging
from pubmed_fetcher import fetch_ids, get_paper_details, save_csv
from typing import Optional

import argparse: Imports the argparse module, which allows us to handle command-line arguments.

import logging: Imports the logging module, which helps with debugging and printing log messages.

from pubmed_fetcher import ...: Imports the functions from pubmed_fetcher.py.

from typing import Optional: Imports the Optional type hint from typing to indicate that a value might be None.
setup_logging Function
def setup_logging(debug: bool) -> None:
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

def setup_logging(debug: bool) -> None:: Defines the function setup_logging, which sets up logging based on whether debugging is enabled.

logging.basicConfig(level=logging.DEBUG): Sets the logging level to DEBUG if debugging is enabled. This provides detailed information about what the code is doing.

logging.basicConfig(level=logging.INFO): If debugging is not enabled, it logs at the INFO level, which provides less verbose information.
main Function

def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch papers from PubMed based on a query.")
    parser.add_argument("query", type=str, help="PubMed search query")
    parser.add_argument("-f", "--file", type=str, help="File to save results", default=None)
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

def main() -> None:: Defines the main function, which will run the core logic of the script.

parser = argparse.ArgumentParser(description="..."): Initializes an argument parser that will handle command-line arguments.

parser.add_argument("query", ...): Defines the required positional argument query (the search term for PubMed).

parser.add_argument("-f", "--file", ...): Defines the optional argument -f (file to save results)
.
parser.add_argument("-d", "--debug", ...): Defines the optional argument -d (enables debug mode).

args = parser.parse_args(): Parses the arguments provided by the user when running the script.
if not args.query:
    print("Error: Query is missing!")
    return

if not args.query:: Checks if the query argument was provided. If not, it prints an error message and stops the program.
setup_logging(args.debug)
logging.debug(f"Fetching papers for query: {args.query}")

setup_logging(args.debug): Calls the setup_logging function to configure logging based on the debug flag.

logging.debug(...): Logs a debug message showing the search query.
pubmed_ids = fetch_ids(args.query)
if len(pubmed_ids) == 0:
    print("No papers found.")
    return

pubmed_ids = fetch_ids(args.query): Calls fetch_ids to get the PubMed IDs for the query.

if len(pubmed_ids) == 0:: Checks if no IDs were returned. If there are no results, it prints a message and stops.
papers = get_paper_details(pubmed_ids)

papers = get_paper_details(pubmed_ids): Calls get_paper_details to fetch the details for the papers based on the PubMed IDs.
if args.file:
        save_csv(args.file, papers)
        print(f"Results saved in {args.file}")
else:
        for paper in papers:
            print(paper)

if args.file:: Checks if the -f argument was provided (i.e., whether to save the results to a file).

save_csv(args.file, papers): Saves the papers to a CSV file if a filename is given.

else:: If no filename is provided, it prints each paper's details to the console.
if __name__ == "__main__":
    main()

if __name__ == "__main__":: Ensures the main function is called when the script is executed directly (not when imported as a module).
##### `All Code`
pubmed_fetcher.py

import requests
import csv
import re
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional

"""Fetch PubMed IDs for a given query."""
def fetch_ids(query: str) -> List[str]:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["esearchresult"]["idlist"]
    except requests.RequestException as e:
        print(f"Error fetching PubMed IDs: {e}")
        return []

"""Fetch detailed information about papers from PubMed."""
def get_paper_details(ids: List[str]) -> List[Dict[str, Optional[str]]]:
    details_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    if not ids:
        return []

    ids_str = ",".join(ids)
    params = {
        "db": "pubmed",
        "id": ids_str,
        "retmode": "xml",
    }
    try:
        response = requests.get(details_url, params=params, timeout=10)
        response.raise_for_status()
        return parse_xml(response.text)
    except requests.RequestException as e:
        print(f"Error fetching paper details: {e}")
        return []
    
"""Parse XML data from PubMed and extract paper details."""
def parse_xml(xml_data: str) -> List[Dict[str, Optional[str]]]:
    root = ET.fromstring(xml_data)
    papers = []
    
    for article in root.findall(".//PubmedArticle"):
        paper: Dict[str, Optional[str]] = {}
        paper["PMID"] = article.findtext(".//PMID")
        paper["Title"] = article.findtext(".//ArticleTitle")
        paper["Date"] = None
        paper["Authors"] = []
        paper["Companies"] = []
        paper["Email"] = None

        # Extract publication date
        date = article.find(".//PubDate")
        if date is not None:
            year = date.findtext("Year")
            month = date.findtext("Month")
            day = date.findtext("Day")
            if year and month and day:
                paper["Date"] = f"{year}-{month}-{day}"

        # Extract authors and affiliations
        authors = article.findall(".//Author")
        for author in authors:
            affiliation = author.findtext("AffiliationInfo/Affiliation")
            if affiliation and not re.search(r"university|institute", affiliation, re.IGNORECASE):
                paper["Authors"].append(author.findtext("LastName"))
                paper["Companies"].append(affiliation)

        # Extract corresponding author email
        corresponding = article.find(".//Author[CorrespondingAuthor='Y']")
        if corresponding is not None:
            email = corresponding.findtext("AffiliationInfo/AuthorEmail")
            if email:
                paper["Email"] = email
        
        papers.append(paper)
    
    return papers

"""Save the paper details to a CSV file."""
def save_csv(filename: str, papers: List[Dict[str, Optional[str]]]) -> None:
    with open(filename, mode='w', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["PMID", "Title", "Date", "Authors", "Companies", "Email"])
        writer.writeheader()
        for paper in papers:
            writer.writerow({
                "PMID": paper["PMID"],
                "Title": paper["Title"],
                "Date": paper["Date"],
                "Authors": "; ".join(paper["Authors"]),
                "Companies": "; ".join(paper["Companies"]),
                "Email": paper["Email"]
            })

cli.py

import argparse
import logging
from pubmed_fetcher import fetch_ids, get_paper_details, save_csv
from typing import Optional

"""Set up logging configuration."""
def setup_logging(debug: bool) -> None:
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    """Main entry point for the script. Handles command-line arguments."""
def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch papers from PubMed based on a query.")
    parser.add_argument("query", type=str, help="PubMed search query")
    parser.add_argument("-f", "--file", type=str, help="File to save results", default=None)
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    if not args.query:
        print("Error: Query is missing!")
        return

    setup_logging(args.debug)
    
    logging.debug(f"Fetching papers for query: {args.query}")
    
    pubmed_ids = fetch_ids(args.query)
    if len(pubmed_ids) == 0:
        print("No papers found.")
        return
    
    papers = get_paper_details(pubmed_ids)

    if args.file:
        save_csv(args.file, papers)
        print(f"Results saved in {args.file}")
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
