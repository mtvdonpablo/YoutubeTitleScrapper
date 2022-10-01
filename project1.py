from pip import main
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



PATH = "/Applications/chromedriver"
driver = webdriver.Chrome(PATH)


driver.get("https://www.youtube.com/")
driver.maximize_window()
time.sleep(4)
search = driver.find_element("xpath", '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
search.send_keys("KSI")
search.send_keys(Keys.RETURN)
time.sleep(4)

titles = driver.find_elements(By.TAG_NAME, "h3")
temp_list = []
new_list=[]
for title in titles:

    if (str(title.text) != "EXPLORE") and (str(title.text) != "MORE FROM YOUTUBE"):
        temp_list.append(str(title.text))

new_list = list(filter(None, temp_list))
for item in new_list:
    print(item)
    print("------------------------------")
driver.quit() 
