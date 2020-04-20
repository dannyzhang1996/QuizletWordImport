from selenium import webdriver
import numpy as np
import pandas as pd
import time
data = pd.read_csv('wordlist.csv')
# data.iloc[62:,:]
raw = data.to_numpy()
raw = raw[1:, :]
print(raw)

browser = webdriver.Chrome()
browser.get('https://quizlet.com/zh-cn')
time.sleep(2)
login = browser.find_element_by_xpath('//*[@id="SiteHeaderReactTarget"]/header/div[1]/div/div[2]/span[2]/div/div[3]/div/button[1]')
    # findElement(By.cssSelector("button.dialog-confirm"))
login.click()
# print(login)
time.sleep(2)
username = browser.find_element_by_xpath('//*[@id="username"]')
username.send_keys('yourUserName')
passwd = browser.find_element_by_xpath('//*[@id="password"]')
passwd.send_keys('yourPassword')
loginbt = browser.find_element_by_xpath('/html/body/div[7]/div/div[2]/form/button')
loginbt.click()
time.sleep(3)

studyset = browser.find_element_by_xpath('//*[@id="DashboardPageTarget"]/div/section[2]/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div/div/div[2]/a')
studyset.click()
time.sleep(3)

edit = browser.find_element_by_xpath('//*[@id="SetPageTarget"]/div/div[1]/div[3]/div[1]/div/div/section/div/div[1]/div/div[1]/span/span/a')
edit.click()

for items in raw:
    tmpCN = items[1]
    tmpEN = items[0]
    add = browser.find_element_by_xpath('//*[@id="addRow"]/span/button')
    add.click()
    input_CN = browser.find_elements_by_xpath("//*[@contenteditable='true']")
    lasttwo = input_CN[-2]
    lastone = input_CN[-1]
    lasttwo.send_keys(tmpCN)
    lastone.send_keys(tmpEN)
    time.sleep(1)


