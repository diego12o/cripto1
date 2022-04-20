

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.shopify.es/"
driver.get(url)

mail = 'x@gmail.com'
password = '123456pailita'
nombre = 'diego'
apellido = 'jajajaj'

#REGISTRO
time.sleep(2)
driver.find_element_by_xpath('//*[@id="ShopifyMainNav"]/ul[2]/li/a').click()
time.sleep(3)
log = driver.find_element_by_xpath('//*[@id="account_email"]')
log.send_keys(mail)
driver.find_element_by_xpath('//*[@id="body-content"]/div[2]/div/div/div/div/div[2]/div/form/button').click()
time.sleep(4)
log = driver.find_element_by_xpath('//*[@id="account_first_name"]')
log.send_keys(nombre)
time.sleep(2)
log = driver.find_element_by_xpath('//*[@id="account_last_name"]')
log.send_keys(apellido)
time.sleep(2)
log=driver.find_element_by_xpath('//*[@id="account_password"]')
log.send_keys(password)
time.sleep(2)
log = driver.find_element_by_xpath('//*[@id="password-confirmation"]')
log.send_keys(password)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="submit-disable"]/button').click()
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/header/div/div/div/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="Polarispopover2"]/div[2]/div/div/ul/li[3]/button').click()
time.sleep(3)

# ACCEDER
driver.find_element_by_xpath('//*[@id="ShopifyMainNav"]/ul[2]/li/a').click()
time.sleep(3)
log = driver.find_element_by_xpath('//*[@id="account_email"]')
log.send_keys(mail)
time.sleep(3)
log = driver.find_element_by_xpath('//*[@id="account_password"]')
log.send_keys(password)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/ul/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="submit-disable"]/button').click()
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/header/div/div/div/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="Polarispopover2"]/div[2]/div/div/ul/li[3]/button').click()
time.sleep(3)

time.sleep(20)