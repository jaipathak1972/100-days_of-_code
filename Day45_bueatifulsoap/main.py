from bs4 import BeautifulSoup
import lxml
with open ("Day45_bueatifulsoap/website.html" ,"r", encoding="utf8") as fr:
    data =fr.read()


soup = BeautifulSoup(data, "html.parser")
anchor_tag= soup.find_all(name="a")

for tag in anchor_tag:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

# heading = soup.find(name="h1", id = "name2")

# print(heading.getText())
company_url =soup.select_one(selector= "p a")
print(company_url.get("href"))

print(soup.select(".heading").getText())
