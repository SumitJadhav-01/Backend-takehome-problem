Documentation for PubMed Fetcher


Overview
This program consists of two Python scripts, pubmed_fetcher.py and cli.py, designed to fetch research papers from PubMed based on a search query. It retrieves paper details such as authors, affiliations, and publication dates, and saves the data in a CSV file or displays it in the console.

Code Organization

File 1: pubmed_fetcher.py
This module contains functions for interacting with the PubMed API, processing the fetched data, and saving the results in a structured format.

Functions

fetch_ids(query: str) -> List[str]

Purpose: Fetches PubMed IDs (PMIDs) for a given search query.
Parameters:
query (str): The search query string.
Returns: A list of PubMed IDs (List[str]).


get_paper_details(ids: List[str]) -> List[Dict[str, Optional[str]]]

Purpose: Fetches detailed information about papers using their PMIDs.
Parameters:
ids (List[str]): A list of PubMed IDs.
Returns: A list of dictionaries containing paper details.


parse_xml(xml_data: str) -> List[Dict[str, Optional[str]]]

Purpose: Parses XML data returned by PubMed API to extract paper metadata.
Parameters:
xml_data (str): XML string containing paper data.
Returns: A list of dictionaries with metadata such as title, authors, and affiliations.


save_csv(filename: str, papers: List[Dict[str, Optional[str]]]) -> None

Purpose: Saves paper details to a CSV file.
Parameters:
filename (str): Name of the output CSV file.
papers (List[Dict[str, Optional[str]]]): A list of dictionaries containing paper details.

File 2: cli.py

This script serves as the command-line interface for interacting with the PubMed Fetcher functionality.

Functions

setup_logging(debug: bool) -> None

Purpose: Configures the logging level.
Parameters:
debug (bool): If True, sets the logging level to DEBUG. Otherwise, sets it to INFO.


main() -> None

Purpose: Main entry point for the script. Processes command-line arguments and coordinates data fetching and output.

Functionality:
Parses command-line arguments (query, output file, and debug mode).
Fetches PubMed IDs using the fetch_ids function.
Retrieves paper details with the get_paper_details function.
Saves results to a file using save_csv or displays them on the console.

Installation and Execution Instructions

To execute the provided Python scripts (pubmed_fetcher.py and cli.py), follow the step-by-step guide below. This guide assumes you have basic knowledge of using the command line and Python environments.

1. Prerequisites
Python Installed: Ensure you have Python 3.6 or later installed on your system. You can download it from python.org.

Pip Installed: Pip usually comes with Python. You can verify by running:

 
pip --version
Internet Connection: Required for fetching data from PubMed.

2. Setting Up the Project
a. Create a Project Directory
Choose a location on your computer and create a new directory for the project.
 
mkdir pubmed_project
cd pubmed_project
b. Create the Python Files
Create two Python files: pubmed_fetcher.py and cli.py.

pubmed_fetcher.py
Create and open pubmed_fetcher.py in your favorite text editor and paste the following code:

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
Create and open cli.py in your text editor and paste the following code:

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


c. Install Required Python Packages

The scripts rely on the requests library for making HTTP requests. Install it using pip:
 
pip install requests

If you plan to manage dependencies more robustly, consider using a virtual environment:
 
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies within the virtual environment
pip install requests

3. Executing the Scripts

The cli.py script is the main entry point that utilizes functions from pubmed_fetcher.py to fetch and display or save PubMed articles based on a search query.


a. Basic Usage

To fetch papers related to a specific query and display them in the console:
 
python cli.py "your search query"

Example:

python cli.py "cancer research"


b. Saving Results to a CSV File

To save the fetched papers to a CSV file, use the -f or --file option followed by the desired filename.
 
python cli.py "your search query" -f results.csv

Example:

python cli.py "machine learning in healthcare" -f ml_healthcare_papers.csv


c. Enabling Debug Mode

For more detailed logging (useful for troubleshooting), enable debug mode with the -d or --debug flag.
 
python cli.py "your search query" -d

Example:
 
python cli.py "genomics" -d


d. Combining Options

You can combine options to save results to a file and enable debug mode simultaneously.

python cli.py "your search query" -f output.csv -d

Example:

python cli.py "CRISPR technology" -f crispr_papers.csv -d

e. Full Command Syntax
 
python cli.py <query> [-f FILE] [-d]
<query>: (Required) The search term for PubMed.
-f, --file: (Optional) Specify the filename to save the results as a CSV.
-d, --debug: (Optional) Enable debug mode for detailed logs.

4. Example Workflow

Let's go through a complete example where we search for papers related to "artificial intelligence in medicine" and save the results to a file named ai_medicine_papers.csv with debug logging enabled.

a. Run the Command
 
python cli.py "artificial intelligence in medicine" -f ai_medicine_papers.csv -d

b. Expected Output

Console Output: Detailed logs due to debug mode, including information about fetching IDs and paper details.
CSV File: A file named ai_medicine_papers.csv will be created in the project directory containing the fetched paper details with the following columns:

PMID
Title
Date
Authors
Companies
Email

c. Viewing the Results
Open the ai_medicine_papers.csv file using any spreadsheet application (e.g., Microsoft Excel, Google Sheets) or a text editor to view the fetched PubMed articles.

5. Troubleshooting
Module Not Found Error: Ensure both pubmed_fetcher.py and cli.py are in the same directory. Also, verify that you're running the command from within that directory.

Missing Dependencies: If you encounter issues related to missing Python packages, ensure you've installed all required packages using pip.

Network Issues: Since the scripts fetch data from the internet, ensure you have a stable internet connection. Also, check if your firewall or network settings are blocking HTTP requests to PubMed's API.

Invalid Query Results: If no papers are found, try refining your search query for better results.
 



Tools and Libraries Used
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













