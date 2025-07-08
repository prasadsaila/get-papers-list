import argparse
import logging
from get_papers_list.get_papers import fetch_pubmed_ids, fetch_paper_details, write_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", help="PubMed query string")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    parser.add_argument("-f", "--file", help="Output CSV file name")

    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    logging.debug("Fetching PubMed IDs...")
    ids = fetch_pubmed_ids(args.query)
    logging.debug(f"Found {len(ids)} IDs")

    results = []
    for pubmed_id in ids:
        logging.debug(f"Processing ID: {pubmed_id}")
        paper = fetch_paper_details(pubmed_id)
        if paper and paper[3]:
            results.append(paper)

    write_csv(results, args.file)
    if not args.file:
        print("\n\nResults:")
        for row in results:
            print(row)
