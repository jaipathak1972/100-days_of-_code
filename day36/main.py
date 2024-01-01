import requests
import smtpd


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_key ="25756ac8be2b4881a3de6e9d70847b29"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

  
reponse = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=MFGMG7SROIU9E471")
reponse.raise_for_status()
data = reponse.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]

yesterday_data_0 = data_list[0]
yesterday_data_1 = data_list[1]

yesterday_closing_price = float(yesterday_data_0["4. close"])
yesterday_yesterday_closing_price =float( yesterday_data_1["4. close"])

clossing_diff =abs( yesterday_closing_price - yesterday_yesterday_closing_price )

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (clossing_diff / float(yesterday_yesterday_closing_price)) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > -1:
    new_para = {
        "q": COMPANY_NAME,
        "apiKey":"25756ac8be2b4881a3de6e9d70847b29",
    }



    news_response = requests.get("https://newsapi.org/v2/everything?", params=new_para)        ## STEP 2: https://newsapi.org/ 
    artical =news_response.json()["articles"]
    three_Articals = artical[0:2]
    print(three_Articals)
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.



#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
final_list = [f"Headline: {artical['title']}. \nBrief: {artical['description']}  "for artical in three_Articals]
print(final_list)
#TODO 9. - Send each article as a separate message via Twilio. 



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

