import csv
import re
from typing import List, Tuple, Optional
from Bio import Entrez

Entrez.email = "your-email@example.com"

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["university", "institute", "college", "school", "hospital", "center", "centre", "department"]
    return not any(word in affiliation.lower() for word in academic_keywords)

def is_pharma_company(affiliation: str) -> bool:
    pharma_keywords = ["pharma", "biotech", "therapeutics", "biosciences", "genomics", "laboratories", "inc", "ltd", "corp"]
    return any(word in affiliation.lower() for word in pharma_keywords)

def fetch_pubmed_ids(query: str) -> List[str]:
    handle = Entrez.esearch(db="pubmed", term=query, retmax=100)
    record = Entrez.read(handle)
    return record["IdList"]

def fetch_paper_details(pubmed_id: str) -> Optional[Tuple[str, str, str, List[str], List[str], Optional[str]]]:
    handle = Entrez.efetch(db="pubmed", id=pubmed_id, rettype="medline", retmode="text")
    from Bio import Medline
    records = Medline.parse(handle)
    record = next(records, None)
    if not record:
        return None

    title = record.get("TI", "")
    pub_date = record.get("DP", "")
    authors = record.get("AU", [])
    affiliations = record.get("AD", [])
    emails = re.findall(r"[\w\.-]+@[\w\.-]+", str(affiliations))

    non_academic_authors = []
    company_affiliations = []

    if isinstance(affiliations, str):
        affiliations = [affiliations]

    for affil in affiliations:
        if is_non_academic(affil) and is_pharma_company(affil):
            company_affiliations.append(affil)
            non_academic_authors.extend(authors)

    return pubmed_id, title, pub_date, list(set(non_academic_authors)), list(set(company_affiliations)), emails[0] if emails else None

def write_csv(data: List[Tuple[str, str, str, List[str], List[str], Optional[str]]], file_name: Optional[str] = None):
    fieldnames = ["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"]
    output = open(file_name, "w", newline="") if file_name else None
    writer = csv.DictWriter(output or None, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow({
            "PubmedID": row[0],
            "Title": row[1],
            "Publication Date": row[2],
            "Non-academic Author(s)": "; ".join(row[3]),
            "Company Affiliation(s)": "; ".join(row[4]),
            "Corresponding Author Email": row[5] or "N/A"
        })
    if output:
        output.close()
