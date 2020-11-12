# Importing required stuff.
from selenium import webdriver
import time
import schedule

# Settings some things up.
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("user-data-dir=c:\\profile\\user-data")

driver = webdriver.Chrome(executable_path="c:\\chromedriver\\chromedriver.exe", options=chrome_options) # change the path to your chromedriver.exe

# Google docs link
driver.get('') # add your google docs link here for dinamic meeting links.


# Opening google meeting function
def opening():
    print('Opening Google Meeting...')
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_xpath('//*[@id="kix-appview"]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div/div[1]').click()
    driver.find_element_by_xpath('//*[@id="kix-appview"]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div[2]/span[2]/span').click()
    driver.find_element_by_xpath('//*[@id="docs-linkbubble-link-text"]').click()


# Joining google meeting function
def joining():
    print('Joining Google Meeting...')
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span').click()


# Sending Attendence Function
def attendence():
    name = 'Kanwarnoor Singh 10a 22'
    time.sleep(5)
    print('Sending Attendence...')
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[7]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[7]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea').send_keys(name)
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[7]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[2]/span').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[7]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/button/i').click()


# Leaving google meet function
def leaving():
    driver.switch_to.window(driver.window_handles[1])
    print('Leaving Google Meeting...')
    driver.close()


# Closing app
def close():
    print('Closing app...')
    driver.quit()


# Timings for each and every class
schedule.every().day.at("09:09").do(opening)
schedule.every().day.at("09:10").do(joining)
schedule.every().day.at("09:20").do(attendence)
schedule.every().day.at("09:45").do(leaving)

schedule.every().day.at("10:09").do(opening)
schedule.every().day.at("10:10").do(joining)
schedule.every().day.at("10:20").do(attendence)
schedule.every().day.at("10:45").do(leaving)

schedule.every().day.at("11:09").do(opening)
schedule.every().day.at("11:10").do(joining)
schedule.every().day.at("11:20").do(attendence)
schedule.every().day.at("11:45").do(leaving)

schedule.every().day.at("12:00").do(close)

# do not change this code.
while True:
    schedule.run_pending()
    time.sleep(1)
