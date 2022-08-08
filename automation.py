
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import math
import os
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



try:
    browser = webdriver.Chrome()
    browser.get("https://www.google.com/webhp?hl=ru&sa=X&ved=0ahUKEwi-uL70mqr5AhWTzYsKHQNFAVYQPAgI")

    browser.maximize_window()

    search = browser.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search.send_keys('фото бараша')
    search.send_keys(Keys.ENTER)
    browser.find_element ('xpath', '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()   
    
    #tabs = browser.window_handles
    #browser.switch_to.window(tabs[1])
    img1 = browser.find_elements('class name','rg_i.Q4LuWd')
    img_link = img1[1].get_attribute('src')
    browser.get(img_link)
    
    action = ActionChains(browser)
    action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])

    browser.get("https://vreale.net/")
    
    browser.find_element ('id', 'log_email').send_keys('dokkod432@gmail.com')
    browser.find_element ('id', 'log_password').send_keys('Windranner')
    browser.find_element ('xpath', '//*[@id="log_in"]').click()

    wait = WebDriverWait(browser, 5)

    #elem = wait.until(EC.visibility_of_all_elements_located(('xpath','//*[@id="page"]/div[3]/div[1]/div[8]/input')))
    #elem.clear()
    browser.find_element ('xpath', '//*[@id="page"]/div[3]/div[1]/div[8]/input').click()
    browser.find_element ('xpath', '//*[@id="post_text"]').send_keys('Найкращій в світі Бараш, люблю його\n\
    P.S. Пост був створений за допомогою Селениум')
    action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    time.sleep(5)
    browser.find_element('xpath', '//*[@id="post_send_but"]').click()
    time.sleep(3)


    
    #browser.find_element ('xpath', '//*[@id="login_but"]').click()
    #time.sleep(10)
    #elem.clear(all)
    #elem.send_keys(img_link)
    

    
   
finally:

    time.sleep(30)
  
    browser.quit()
