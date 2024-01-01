

headers = {
    'Accept-Language': "en-US,en;q=0.9",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    'Cookie': 'PHPSESSID=c52ce44e89bf737014ccb08720802d80; _ga=GA1.2.1181881201.1697707372; _gid=GA1.2.1122304227.1697707372; _ga_VL41109FEB=GS1.2.1697707372.1.1.1697707419.0.0.0',
    "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    "X-Forwarded-For": "49.36.178.7",
    "Accept-Encoding": "gzip, deflate, br",
    'Host': "myhttpheader.com",
    'upgrade-insecure-requests': "1",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'sec-fetch-site': "cross-site",
    'sec-fetch-mode': "navigate",
    'sec-fetch-user': "?1",
    'sec-fetch-dest': "document",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "Windows",
    'x-forwarded-proto': "https",
    'x-https': "on"
}



from bs4 import BeautifulSoup
import requests

site_content = requests.get(
f"https://www.amazon.com/OnePlus-Moonstone-Smartphone-SuperVOOC-CPH2417/dp/B0B7QQN6P9/?_encoding=UTF8&pd_rd_w=XE0mq&content-id=amzn1.sym.595f69d1-9647-4ce9-9fca-a43eb1c1f3b6&pf_rd_p=595f69d1-9647-4ce9-9fca-a43eb1c1f3b6&pf_rd_r=3XCX5P3DM32GRHVN8NX1&pd_rd_wg=s5DsZ&pd_rd_r=81a189cd-309d-423f-8c85-0dcca5c355a4&ref_=pd_gw_exports-popular-this-season-with-similar-asins/",
headers=headers).text

soup = BeautifulSoup(site_content, "html.parser")

product_cost = soup.find(name="span", class_="a-price-whole")
product_fraction = soup.find(name="span", class_="a-price-fraction")

actual_cost = float(product_cost.getText() + product_fraction.get_text())
print(actual_cost)