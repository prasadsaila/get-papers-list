# get-papers-list

A Python command-line tool to fetch PubMed papers that include at least one author affiliated with a pharmaceutical or biotech company.

## Features

- Accepts any PubMed query syntax  
- Extracts paper details using the PubMed API  
- Filters for non-academic, pharma/biotech-affiliated authors  
- Outputs to CSV or console  
- Typed Python code with error handling and modular structure  

## Requirements

- Python 3.9+
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management

## Setup

```bash
git clone https://github.com/prasadsaila/get-papers-list.git
cd get-papers-list
poetry install
```

## Usage

```bash
poetry run get-papers-list "cancer immunotherapy" --file results.csv
```

### Options

- `-f`, `--file`: Output CSV file path  
- `-d`, `--debug`: Enable debug logs  
- `-h`, `--help`: Show help message  

## Output CSV Columns

- PubmedID  
- Title  
- Publication Date  
- Non-academic Author(s)  
- Company Affiliation(s)  
- Corresponding Author Email  

## Heuristics Used

- Academic institutions identified by keywords like `university`, `institute`, etc.  
- Pharma/biotech affiliations identified using terms like `pharma`, `therapeutics`, `genomics`, etc.

## Project Structure

- `get_papers.py`: Core logic and PubMed access  
- `cli.py`: Command-line interface  
- `pyproject.toml`: Poetry configuration  
- `README.md`: Documentation  

## Tools & Libraries Used

- [Biopython](https://biopython.org/) – for PubMed access  
- [Poetry](https://python-poetry.org/) – for dependency and script management

 ## Summary of PubMed API calls used
API Function	Purpose	Code Used
- esearch	Search for PubMed IDs	✅
- efetch	Get metadata for papers	✅

  ## TEST PYPI
  - https://test.pypi.org/project/get-papers-list-prasad-saila/



