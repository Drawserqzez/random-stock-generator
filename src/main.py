import bs4
import random
import requests

url = "https://www.avanza.se/frontend/template.html/marketing/advanced-filter/advanced-filter-template?widgets.stockLists.filter.list[0]=SE.LargeCap.SE&widgets.stockLists.filter.list[1]=SE.Inofficiella&widgets.stockLists.filter.list[2]=SE.MidCap.SE&widgets.stockLists.filter.list[3]=SE.SmallCap.SE&widgets.stockLists.filter.list[4]=SE.Xterna+listan&widgets.stockLists.filter.list[5]=SE.FNSE&widgets.stockLists.filter.list[6]=SE.XNGM&widgets.stockLists.filter.list[7]=SE.NSME&widgets.stockLists.filter.list[8]=SE.XSAT&widgets.stockLists.active=true&parameters.startIndex=0&parameters.maxResults=10000&parameters.selectedFields[0]=LATEST&parameters.selectedFields[1]=PRICE_PER_EARNINGS&parameters.selectedFields[2]=NBR_OF_OWNERS"
test_url = "https://www.avanza.se/frontend/template.html/marketing/advanced-filter/advanced-filter-template?widgets.stockLists.filter.list[0]=SE.LargeCap.SE&widgets.stockLists.filter.list[1]=SE.Inofficiella&widgets.stockLists.filter.list[2]=SE.MidCap.SE&widgets.stockLists.filter.list[3]=SE.SmallCap.SE&widgets.stockLists.filter.list[4]=SE.Xterna+listan&widgets.stockLists.filter.list[5]=SE.FNSE&widgets.stockLists.filter.list[6]=SE.XNGM&widgets.stockLists.filter.list[7]=SE.NSME&widgets.stockLists.filter.list[8]=SE.XSAT&widgets.stockLists.active=true&parameters.startIndex=0&parameters.maxResults=10&parameters.selectedFields[0]=LATEST&parameters.selectedFields[1]=PRICE_PER_EARNINGS&parameters.selectedFields[2]=NBR_OF_OWNERS"
# TODO: Replace this with the real url when not testing
page = requests.get(test_url) # Fetches the html from the specified url

# If the status is 200 that means that everything went as planned
if page.status_code == 200:
    # Create bs4 object with the response from the get request
    big_soup = bs4.BeautifulSoup(page.text, "html.parser")

    data = big_soup.find_all("tr", class_="row") # Finds all the required tr elements
    data_amount = int(len(data) / 3) # There are three distinct tables, so the actual amount of rows is a third of the length

    for row_no in range(data_amount):
        print(f"Row number {row_no}") # TODO: Remove this when not debugging
        small_soup = bs4.BeautifulSoup(big_soup.__str__(), "html.parser") # Creates another bs4 object with lesser content for speedier computation
        data_tags = small_soup.find_all("tr", class_=f"rowId{row_no}") # Finds the tr elements with the specific row-number

        for tags in data_tags:
            print(d)
# Else it shows an error message
else: 
    print(f"The call returned a bad status code. Code: {page.status_code}")