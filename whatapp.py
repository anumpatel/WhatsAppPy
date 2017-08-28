# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:30:59 2017

@author: anurag
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
 
# Path to chrome-driver
driver = webdriver.Chrome('/home/user/chromedriver')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
 
# Name of a friend you want to send the message.
target = "Friend's Name"
 
# The Message body goes in string
string = "hi"
y_arg = '//*[@id="side"]/div[2]/div/label/input'
input_y = wait.until(EC.presence_of_element_located((
    By.XPATH, y_arg)))
input_y.send_keys(target + Keys.ENTER)


 
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))


input_box.send_keys(string)
input_box.send_keys(Keys.ENTER)

    
