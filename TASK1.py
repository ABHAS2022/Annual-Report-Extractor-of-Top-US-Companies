


import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
from lxml import etree

def fetching_report(val):
    # Construct URL and fetch HTML content

    '''Stocklight is the website that I have used to extract the pdfs of company's annual report pdf'''

    url = f"https://stocklight.com/stocks/search?q={val}"
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')  # Decode for proper parsing

    # Parse HTML using lxml
    parser = etree.HTMLParser()
    tree = etree.fromstring(html_content, parser)

    ''' Now after I have searched the company in stocklight I have gone into the HTML structure of the 
    webpage to extract the "Name of the Company" and also extracted the further directing link to the report pdf '''


    # Extract report URL and company name using XPath
    
    #Here the tree.xpath is the command in the lxml.tree will help us to locate the path where the desired 
    #information is stored

    #In elements I have stored the path location for the new redirecting website
    #In company_name I have stored the path location for the company name
    elements = tree.xpath("/html/body/div[3]/div[2]/div[2]/a[1]")
    company_name = tree.xpath("/html/body/div[3]/div[2]/div[2]/a[1]/div/div[2]")

    # stri is giving us the another redirecting website for this case which when parsed will take us to the final webpage
    # where the annual report is there

    stri = "https://stocklight.com"
    #Link extration step from the stored address
    if elements:
        for element in elements:
            if element.get('href'):
                stri = stri + element.get('href')


    #Company_name extraction step I have given the output text (company name) to company_name variable itself in order to minimize the variables
    # Handle company name
    if company_name:
        for name in company_name:
            if name.text:
                company_name = name.text.strip()

    # Fetch additional info from the obtained report URL
    url = stri
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')

    # Parse HTML using lxml
    parser = etree.HTMLParser()
    tree = etree.fromstring(html_content, parser)

    #Again the same methodology for the website extration and pdf extraction

    # Extract website URL
    xpath_expression = "/html/body/div[6]/div/div[1]/div[2]/div/div[1]/a"
    elements = tree.xpath(xpath_expression)
    website = tree.xpath("/html/body/div[4]/div/div[1]/div/div/div/a")

    # Handle website URL
    stri = ""
    if elements:
        for element in elements:
            if element.get('href'):
                stri = element.get('href')
    else:
        stri = "No report found"

    if website:
        for element in website:
            if element.get('href'):
                website = element.get('href')
    else:
        print(f"No elements found using the provided XPath expression COMPANY WEBSITE. {val}")

    # Return report URL, company name, and website URL
    return stri, company_name, website 



def main():
    #I have used companiesmarketcap.com for finding the top 100 comapanies of US
    # Define URL for finding top 100 US companies
    companies_url = "https://companiesmarketcap.com/usa/largest-companies-in-the-usa-by-market-cap/"

    # Get list of companies
    response = requests.get(companies_url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract company names
    company_elements = soup.find_all("div", class_="company-code")
    companies = [element.text.strip() for element in company_elements]

    # Lists to store data
    
    l = [] #It is storing the the annual report pdf link
    
    l1 = [] #It is storing the company_name where pdf is extracted
    
    l2 = [] #It is storing the website of the company

    count = 1 #count is used to keep the track of the process

    # Iterate over companies and fetch info
    for company in companies[:100]:
        report, company_name, website = fetching_report(company)
        print(count)
        count = count + 1
        l.append(report)
        l1.append(company_name)
        l2.append(website)

    # Create DataFrame
    df = pd.DataFrame({"Company":l1,"Website":l2,"Annual Report":l})

    
    # Save to CSV
    df.to_csv("Result.csv",index=False)


main()













