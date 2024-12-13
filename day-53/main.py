from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")

google_list = "https://docs.google.com/forms/d/e/1FAIpQLSdNyo6NBnaxGBhdim5TDqKt3DUOPSupARp06VlHO4TkFKjDLg/viewform?usp=header"

zillow = response.text
#print(zillow)

soup = BeautifulSoup(zillow, "html.parser")
#zillow = soup.select(".StyledPropertyCardDataWrapper a")

###### ALL LINKS ######
zillow = soup.find_all(name = "a", class_ = "property-card-link")
zillow_links = [link["href"] for link in zillow]


###### ALL PRICES ######
all_prices = soup.find_all(class_ = "PropertyCardWrapper__StyledPriceLine")
#print(all_prices)
zillow_prices = [price.getText().split("+")[0] for price in all_prices]
#print(zillow_prices)

###### ALL ADDRESSES ######
all_addresses = soup.find_all(name = "address")
#print(all_addresses)
#zillow_addresses = [address.getText().split("\n")[1].replace(" ","") for address in all_addresses]
zillow_addresses = [address.getText().replace("|"," ").strip() for address in all_addresses]

print(zillow_addresses)