from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title.string)
#print(soup.prettify())

#print(soup.a)

all_anchor_tags = soup.find_all(name = "a")

# for tag in all_anchor_tags:
#     print(tag.getText())
#
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#

heading = soup.find(name = "h1", id = "name")
print(heading)

section_heading = soup.find(name = "h3", class_ = "heading")
print(section_heading.get("class"))

