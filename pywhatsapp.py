import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome(sys.path[0] + '/chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

print("after wait")

def getMessage():
    url = "https://ajith-messages.p.rapidapi.com/getMsgs"

    querystring = {"category":"love"}

    headers = {
        'x-rapidapi-host': "ajith-messages.p.rapidapi.com",
        'x-rapidapi-key': "790cf6b959mshf12d4fdcf9c8eefp104cbejsnb8bb62524cb4"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()['Message']

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = sys.argv[1]

message = getMessage()

inp_xpath_search = "//input[@title='Search or start new chat']"
input_box_search = wait.until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(target)
time.sleep(2)
print('after search')

selected_contact = driver.find_elements_by_xpath("//span[@class='matched-text']")[0];
selected_contact.click()

print("after contact select")

inp_xpath = '//div[@class="_3u328 copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
input_box.send_keys(message + Keys.ENTER)
time.sleep(2)

print("after send")

driver.quit()

