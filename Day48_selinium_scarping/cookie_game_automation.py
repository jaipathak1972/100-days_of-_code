import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def main():
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option("detach" , True)
    driver = webdriver.Chrome(chrome_option)
    driver.maximize_window()
    driver.get("https://orteil.dashnet.org/experiments/cookie/")

    # Get cookie to click on.
    cookie = driver.find_element(by=By.ID, value="cookie")

    # Get upgrade item ids.
    items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
    item_ids = [item.get_attribute("id") for item in items]

    timeout = time.time() + 8
    timeouts = time.time() + 50
    five_min = time.time() + 600*5  # 5 minutes

    while True:
        cookie.click()

        # Every 5 seconds:
        if time.time() > timeout:

            # Get all upgrade <b> tags
            all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
            item_prices = []

            # Convert <b> text into an integer price.
            for price in all_prices:
                element_text = price.text
                if element_text != "":
                    cost = int(element_text.split("-")[1].strip().replace(",", ""))
                    item_prices.append(cost)

            # Create dictionary of store items and prices
            cookie_upgrades = {}
            for n in range(len(item_prices)):
                cookie_upgrades[item_prices[n]] = item_ids[n]

            # Get current cookie count
            money_element = driver.find_element(by=By.ID, value="money").text
            if "," in money_element:
                money_element = money_element.replace(",", "")
            cookie_count = int(money_element)

            # Find upgrades that we can currently afford
            affordable_upgrades = {}
            for cost, id in cookie_upgrades.items():
                if cookie_count > cost:
                    affordable_upgrades[cost] = id

            # Purchase the most expensive affordable upgrade
            lowest_price_affordable_upgrade = min(affordable_upgrades)
            print(lowest_price_affordable_upgrade )
            to_purchase_id = affordable_upgrades[lowest_price_affordable_upgrade]

            driver.find_element(by=By.ID, value=to_purchase_id).click()

            # Add another 5 seconds until the next check
            timeout = time.time() + 8

            if time.time() > timeouts:
                highest_price_affordable_upgrade = max(affordable_upgrades)
                print(highest_price_affordable_upgrade )
                to_purchase_ids = affordable_upgrades[highest_price_affordable_upgrade]

                driver.find_element(by=By.ID, value=to_purchase_ids).click()


                timeout = time.time() + 50



        

        # After 5 minutes stop the bot and check the cookies per second count.
        if time.time() > five_min:
            cookie_per_s = driver.find_element(by=By.ID, value="cps").text
            # print(cookie_per_s)
            break


    

# Check if the script is run as the main program
if __name__ == "__main__":
    main()


