import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Send an HTTP GET request to the URL
response = requests.get(url=URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")

# Find all the h3 elements with the class "title"
heading = soup.find_all(name="h3", class_="title")

# Extract the text from these elements and sort the list
all_movies = [tag.getText() for tag in heading]
sorted_list = all_movies[::-1]

# Write the sorted movie list to a file
with open("all_movie_file.txt", "w", encoding='utf-8') as fw:
    for movie in sorted_list:
        fw.write(movie + "\n")
