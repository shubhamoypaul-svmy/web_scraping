import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def remove_similar(string_text):
    split_text = string_text.split("\n\n\n")
    return split_text[0]

# Specify the URL of the Mint website
url = "https://www.livemint.com/market/stock-market-news"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the section or element containing the daily news report
news_section = soup.find("div", class_="headlineSec")
#print(soup.find_all("h2",class_ = "headline"))


#Check if the news section exists
if news_section is not None:
    # Extract the required information from the news section
    for news_article in soup.find_all("h2",class_ = "headline"):
        # Extract the title and content of the news article
        title = news_article.find("a").text.strip()
        link = urljoin('https://www.livemint.com', news_article.find("a")["href"])
        #Send a GET request to the URL
        response = requests.get(link)

        # Create a BeautifulSoup object to parse the HTML content
        soup2 = BeautifulSoup(response.content, "html.parser")
        # Print or store the extracted information as per your requirement
        print("Title:", title)
        # Extract the required information from the news section
        div_element = soup2.find("div", class_="mainArea")
        content_p = ""
        for article in div_element.find_all("p"):
            # Extract the title and content of the news article
            content_p += article.get_text()
        print("content: ",remove_similar(content_p))
        #print("Content:", content)
else:
    print("News section not found on the website.")







