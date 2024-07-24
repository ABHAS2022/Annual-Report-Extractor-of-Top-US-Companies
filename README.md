# Top Cap US Companies Annual Report Scraper

This project was developed as part of my intern recruitment process at Sprih. The objective was to extract the annual reports of the top 100 market cap US companies.

## Overview

The project consists of two main tasks:

1. **Task1.py**: This script scrapes the names and codes of the top 100 US companies by market cap from [companiesmarketcap.com](https://companiesmarketcap.com/usa/largest-companies-in-the-usa-by-market-cap/). It then uses these company codes to search for annual reports on [stocklight.com](https://stocklight.com/stocks). The script extracts the company name, official website, and annual report link and stores this information in an Excel file.

2. **Task2.py**: This script verifies whether the extracted annual report links are PDF files. It checks if the links redirect to a MIME type of `application/pdf`.

## Features

- **Web Scraping**: Uses BeautifulSoup and Requests to scrape data from websites.
- **Data Extraction**: Extracts and processes relevant information to generate a structured dataset.
- **Data Verification**: Ensures the validity of the extracted links by checking their MIME type.
- **Excel Integration**: Stores the extracted data in an organized Excel file.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/top-cap-us-companies-annual-reports.git
    cd top-cap-us-companies-annual-reports
    ```

2. Install the required dependencies:

    ```bash
    pip install -r dependency.txt
    ```

## Usage

1. Run `Task1.py` to scrape and extract data:

    ```bash
    python Task1.py
    ```

    This script will generate an Excel file with the company names, official websites, and annual report links.

2. Run `Task2.py` to verify the links:

    ```bash
    python Task2.py
    ```

    This script will check if the extracted links point to PDF files.

## Files

- `Task1.py`: Script to scrape company data and extract annual report links.
- `Task2.py`: Script to verify the extracted links.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Project documentation.

## Dependencies

- BeautifulSoup4
- Requests
- Pandas
- Openpyxl

## Contributing

Feel free to fork this repository, create a feature branch, and submit a pull request. Any improvements or suggestions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [companiesmarketcap.com](https://companiesmarketcap.com/usa/largest-companies-in-the-usa-by-market-cap/) for the list of top US companies.
- [stocklight.com](https://stocklight.com/stocks) for providing access to annual report links.

