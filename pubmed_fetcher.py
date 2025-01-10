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
