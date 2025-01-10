import argparse
import logging
from pubmed_fetcher import fetch_ids, get_paper_details, save_csv
from typing import Optional

# Set up logging configuration
def setup_logging(debug: bool) -> None:
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

# Main entry point for the script. Handles command-line arguments
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
