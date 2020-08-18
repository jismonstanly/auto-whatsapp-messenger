from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\JISMON\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
print(driver.title)
time.sleep(20)
driver.find_element_by_xpath("//*[@title='Kaptronics']").click()
time.sleep(20)
for i in range(100):
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys("test messege")
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()