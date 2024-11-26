from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title.string)
#print(soup.prettify())

#print(soup.a)

#all_anchor_tags = soup.find_all(name = "a")

# for tag in all_anchor_tags:
#     print(tag.getText())
#
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#

# heading = soup.find(name = "h1", id = "name")
# print(heading)
#
# section_heading = soup.find(name = "h3", class_ = "heading")
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector = "#name")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name = "a", class_ = "storylink")
#print(article_tag)

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)



# article_text = article_tag.getText()
# print(article_text)
# article_link =article_tag.get("href")
# print(article_link)
#article_upvotes = soup.find_all(name="span", class_= "score").getText()
#print(article_upvote)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_ = "score")]

print(article_texts)
print(article_links)
print(article_upvotes)