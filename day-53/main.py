from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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

#print(zillow_addresses)


####### FILL IN FORM #######

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options = chrome_options)
driver.get(google_list)


for n in range(len(zillow_prices)):
    address_fill = "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"
    address_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, address_fill))
    )

    address_element.send_keys(zillow_addresses[n])

    price_fill = driver.find_element(By.XPATH,
                                     "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_fill.send_keys(zillow_prices[n])

    link_fill = driver.find_element(By.XPATH,
                                    "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_fill.send_keys(zillow_links[n])

    submit = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    submit.click()

    next = "/html/body/div[1]/div[2]/div[1]/div/div[4]/a"
    next_response = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, next))
    )
    next_response.click()