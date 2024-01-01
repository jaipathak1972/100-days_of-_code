import requests
from datetime import datetime
from tkinter import *

# Pixela API Configuration
USERNAME = "jaipathak12"
TOKEN = "b2hj1gk31l3j2"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

# Create the Pixela user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)

# Create the Pixela graph for habit tracking
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {"X-USER-TOKEN": TOKEN}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Create the Tkinter GUI
window = Tk()
window.title("Daily Habit Tracker")
window.config(padx=100, pady=50, bg="khaki2")

# Label OF HABIT_CHECK
label = Label(text="HABIT_CHECK", fg="Black", font=("arial", 40, "bold"))
label.grid(row=0, column=1)

# ENTRY OF THE INPUT NUMBER

today = datetime.now()
date = str(today).split(" ") [0] .split("-")
x = "".join(date)
print(x)

progress_entry = Entry(width=10, bg="azure")

progress_entry.grid(row=2, column=1, pady=60)

# Function to add data to the Pixela graph
def add_data():
    today = datetime.now()
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity": progress_entry.get(),
    }
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    print(response.text)
    progress_entry.delete("0" ,"end")

# Function to update data (not used here)
# def update_data():
#     today = datetime.now()
#     update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#     new_pixel_data = {
#         "quantity": "4.5"
#     }
#     response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#     print(response.text)

# Function to delete data (not used here)
# def delete_data():
#     today = datetime.now()
#     delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#     response = requests.delete(url=delete_endpoint, headers=headers)
#     print(response.text)

# Buttons for adding data
add_button = Button(text="Add Data", command=add_data)
add_button.grid(row=3, column=1, pady=10)



window.mainloop()
