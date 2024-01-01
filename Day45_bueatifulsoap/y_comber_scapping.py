import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/")
data = response.text
soup = BeautifulSoup(data, "html.parser")
anchor_tags = soup.find_all(name="a", rel="noreferrer")
link = soup.find_all()

artical_texts = []
artical_link = []

for tag in anchor_tags:
    text = tag.getText()
    artical_texts.append(text)
    
    link = tag.get("href")
    artical_link.append(link)


artical_votes = [int(score.getText().split()[0]) for score in soup.find_all(name = "span", class_="score")]

# print(artical_texts)
# print(artical_link)
# print(artical_votes)

largest_vote = max(artical_votes)
largest_index = artical_votes.index(largest_vote)
print(largest_index)

print(artical_votes[largest_index])
print(artical_texts[largest_index])
print(artical_link[largest_index])
# decrsing_list = []
# for index, vote in enumerate(artical_votes):
#     if vote[int(index)] < vote [ int(index)+1]:
#         decrsing_list.append(vote):
#     else:
#         vote[int(index)+1]
     
