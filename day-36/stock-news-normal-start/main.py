import requests
from datetime import date, timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_key = ""
news_api_key = ""

twilio_api_key = ""
twilio_sid = ""
twilio_token = ""

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key
}

stock = requests.get(STOCK_ENDPOINT, params = stock_parameters)
stock_data = stock.json()
#print(data["Time Series (Daily)"]["2024-10-31"]["4. close"])

yesterday = str(date.today() - timedelta(days=1))
day_before = str(date.today() - timedelta(days=2))

#[new_value for (key, value) in dictionary.items()]
#yesterday_closing = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
#day_before_closing = float(stock_data["Time Series (Daily)"][day_before]["4. close"])

#print(yesterday_closing)
#print(day_before_closing)

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#pos_difference = abs(yesterday_closing - day_before_closing)

#print(pos_difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#percent_diff = (pos_difference/yesterday_closing)*100
#print(percent_diff)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#if percent_diff > 5:
#    print("Get News")

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

news_parameters = {
        "q": COMPANY_NAME,
    "from": yesterday,
    "sortBy": "popularity",
    "apiKey": news_api_key
}

news = requests.get(NEWS_ENDPOINT, params = news_parameters)
news_data = news.json()
#print(news_data)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

three_articles = news_data["articles"][0:3]
#print(three_articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# for article in three_articles:
#     headline = article["source"]
#     description = article["description"]
#     formatted_articles = f"Headline: {headline}. \n Brief: {description}"
#     print(formatted_articles)
#TODO 9. - Send each article as a separate message via Twilio. 

client = Client(twilio_sid, twilio_token)


if percent_diff > 5:
#    print("Get News")
    for article in three_articles:
        headline = article["source"]
        description = article["description"]
        formatted_articles = f"Headline: {headline}. \n Brief: {description}"
        message = client.messages.create(
            from_= "whatsapp:+14155238886",
            body = formatted_articles,
            to = "whatsapp:+18328580221"
        )




#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

