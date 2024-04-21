import requests
from bs4 import BeautifulSoup

def get_item_price(item):
    original_item = item
    item = item.replace(" ", "_")
    url = f"https://hayday.fandom.com/wiki/{item}"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # for a maximum price of 2,340

        # Try to get exact price
        # Find an element containing "maximum price"
        elem = soup.find(string=lambda text: "maximum price" in text.lower())
        if elem:
            text = elem.lower()
            # Remove anything that isn't a number
            price = "".join([c for c in text if c.isdigit()])
            price = int(price) / 10
        else:
            # find text containing "to" inside portable-infobox
            elem = soup.find("aside", {"class": "portable-infobox"})
            # Find the element containing "to"
            elem = elem.find(string=lambda text: "to" in text.lower())

            if elem:
                text = elem.lower().split("to")[1]
                # Remove anything that isn't a number
                price = "".join([c for c in text if c.isdigit()])
                price = price+".0"
            else:
                price = None

        if price:
            print(f"\"{original_item}\": {price},")
    else:
        print(f"Error fetching price for {item}")

items = []

for item in items:
    get_item_price(item)