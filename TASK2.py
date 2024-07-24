# """TASK 2"""

# import pandas as pd
# import requests


# # Function to check if a link leads to a PDF
# def check_pdf_link(link, company):
#     try:
#         # Send a HEAD request to the link to get the response headers
#         response = requests.head(link)
        
#         # Extract the content-type header from the response
#         content_type = response.headers['content-type']
        
#         # Check if the content-type indicates a PDF file
#         if 'application/pdf' in content_type:
#             # If it's a PDF, print a message indicating that the link works and leads to a PDF
#             print(f"Link '{link}' is working and leads to a PDF of website of {company}.")
#         else:
#             # If it's not a PDF, print a message indicating that the link is not a PDF
#             print(f"Link '{link}' is not a PDF for company {company}.")
#     except Exception as e:
#         # If an error occurs during the request, print an error message
#         print(f"Error checking link '{link}': {e}  ==> Company {company}")

# def main():
#     # Read the CSV file containing the links
#     df = pd.read_csv("Result.csv")
#     # Iterate over each link in the DataFrame and check if it's working
#     for count, link in enumerate(df['Annual Report']):
#         # Pass each link and the corresponding company name to the check_pdf_link function
#         check_pdf_link(link, df['Company'][count])


# main()







import pandas as pd
df1 = pd.read_csv("C:\\Users\\ABHAS\\Downloads\\1 - Sheet1 (1).csv")
df2 = pd.read_csv("C:\\Users\\ABHAS\\Downloads\\1 - Sheet1.csv")
val1 = df1['Company'].tolist()
for i in val1:
    if((df1[df1['Company'] == i]["Revenue"]).tolist()[0] == (df2[df2['Company'] == i]['Revenue']).tolist()[0]):
        print("Yes", i)