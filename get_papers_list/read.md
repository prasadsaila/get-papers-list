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
git clone https://github.com/yourusername/get-papers-list.git
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

## Bonus Features

- You may publish the module to [Test PyPI](https://test.pypi.org/) for bonus credit

## License

MIT License

---

### 📦 Publishing to Test PyPI

#### 1. Build the Package

```bash
poetry build
```

#### 2. Register on Test PyPI

Create an account at [Test PyPI](https://test.pypi.org/account/register/) and generate an API token.

#### 3. Upload Using Twine

```bash
poetry add --dev twine
poetry run twine upload --repository testpypi dist/*
```

Use `__token__` as your username and the API token as the password.

#### 4. Test Installation

```bash
pip install --index-url https://test.pypi.org/simple/ get-papers-list
```
