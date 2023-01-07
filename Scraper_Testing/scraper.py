from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

# some code is utilized from kromme's Scrape-Facebook-birthdays' github repo

username = input("Enter Facebook username: ")
password = input("Enter Facebook password: ")

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(PATH, options=options)

driver.get("https://www.facebook.com/")

# find username box and type user's username
username_entry = driver.find_element(By.ID, 'email')
username_entry.send_keys(username)

# find password box and type user's password
password_entry = driver.find_element(By.ID, 'pass')
password_entry.send_keys(password)

# hit enter to send the username and password to facebook
password_entry.send_keys(Keys.RETURN)

# wait 5 seconds to see if it worked
time.sleep(5)

# send the user to the birthday tab
driver.get("https://www.facebook.com/events/birthdays/")
time.sleep(5)


driver.quit()
