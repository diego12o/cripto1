from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.shopify.es/"
url1 = "https://correotemporal.org/"
url2 = "https://cl.estadio.com/landing"
# driver.get(url)

password = '123456pailita@'
nombre = 'pipe'
apellido = 'wo'
year = 1990
driver.get(url)

driver.execute_script("window.open('https://correotemporal.org/');")

mail = input("Ingrese correo temporal: ")

driver.switch_to.window(driver.window_handles[0])

#---------------------------------SHOPIFY-----------------------------------------------

#REGISTRO
time.sleep(3)
driver.find_element_by_xpath('//*[@id="ShopifyMainNav"]/ul[2]/li/a').click()
time.sleep(3)
log = driver.find_element_by_xpath('//*[@id="account_email"]')
log.send_keys(mail)
time.sleep(40)
driver.find_element_by_xpath('//*[@id="body-content"]/div[2]/div/div/div/div/div[2]/div/form/button').click()
time.sleep(4)
log = driver.find_element_by_xpath('//*[@id="account_first_name"]')
log.send_keys(nombre)
time.sleep(3)
log = driver.find_element_by_xpath('//*[@id="account_last_name"]')
log.send_keys(apellido)
time.sleep(3)
log=driver.find_element_by_xpath('//*[@id="account_password"]')
log.send_keys(password)
time.sleep(3)
log = driver.find_element_by_xpath('//*[@id="password-confirmation"]')
log.send_keys(password)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="submit-disable"]/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/header/div/div/div/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="Polarispopover2"]/div[2]/div/div/ul/li[3]/button').click()
time.sleep(3)

# #ACCEDER
driver.find_element_by_xpath('//*[@id="ShopifyMainNav"]/ul[2]/li/a').click()
time.sleep(3)
log = driver.find_element_by_xpath('//*[@id="account_email"]')
log.send_keys(mail)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="body-content"]/div[2]/div/div/div/div/div[2]/div/form/button').click()
time.sleep(4)
log = driver.find_element_by_xpath('//*[@id="account_password"]')
log.send_keys(password)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/ul/button').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/header/div/div/div/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="Polarispopover2"]/div[2]/div/div/ul/li[3]/button').click()
time.sleep(3)

#RECUPERAR CONTRASEÑA
driver.find_element_by_xpath('//*[@id="ShopifyMainNav"]/ul[2]/li/a').click()
time.sleep(3)
log = driver.find_element_by_xpath('//*[@id="account_email"]')
log.send_keys(mail)
driver.find_element_by_xpath('//*[@id="body-content"]/div[2]/div/div/div/div/div[2]/div/form/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="body-content"]/div[2]/div/div/div/div/div[2]/div/div/a').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="body-content"]/div[2]/div/div/div/div/div[2]/div/form/button').click()

time.sleep(5)

#BUSCA CORREO
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
link_correo = input("Ingrese link para restablecer contraseña: ")
driver.switch_to.window(driver.window_handles[0])
driver.get(link_correo)
time.sleep(2)
log = driver.find_element_by_id('passwords')
log.send_keys(password)
time.sleep(2)
log = driver.find_element_by_xpath('//*[@id="password-confirmation"]')
log.send_keys(password)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="submit-disable"]/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="account_password"]').send_keys(password)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/ul/button').click()
time.sleep(4)

#CAMBIA CONTRASEÑA
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/header/div/div/div/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="Polarispopover2"]/div[2]/div/div/ul/li[1]/a').click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[2])
link = driver.current_url.replace("personal","")+'security'
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.get(link)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="password"]/div[2]/section/footer/button').click()
time.sleep(3)
log = driver.find_element_by_xpath('//*[@id="account_old_password"]')
log.send_keys(password)
time.sleep(3)
log = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[7]/form/div[2]/div/div[2]/div[1]/div/input')
log.send_keys(password)
time.sleep(3)
log = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[7]/form/div[2]/div/div[3]/div/input')
log.send_keys(password)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="change_password"]/form/div[3]/div/div/div/button').click()
time.sleep(3)

#---------------------------------TNTSPORT-----------------------------------------------


#REGISTRO
driver.get(url2)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/section[1]/div[1]/div/div[2]/div/div/div/div/form/div[1]/input').send_keys(nombre)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/section[1]/div[1]/div/div[2]/div/div/div/div/form/div[2]/input').send_keys(apellido)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="email"]').send_keys(mail)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/section[1]/div[1]/div/div[2]/div/div/div/div/form/div[4]/input').send_keys(password)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/section[1]/div[1]/div/div[2]/div/div/div/div/form/div[5]/input').send_keys(password)
input("Ingrese OK si paso Captcha: ")
driver.find_element_by_xpath('//*[@id="confirmation"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="js-submit-signup"]').click()
time.sleep(3)

#CONFIRMACIÓN DE CUENTA
driver.switch_to.window(driver.window_handles[1])
input("Ingrese OK si confirmó cuenta: ")

#INGRESO A LA CUENTA
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/header/div/div[2]/div/button').click()

time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/header/div/div[2]/div/div/div/div/div[2]/section/form/div[1]/input').send_keys(mail)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/header/div/div[2]/div/div/div/div/div[2]/section/form/div[2]/input').send_keys(password)
input("Ingrese OK si paso Captcha: ")
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/header/div/div[2]/div/div/div/div/div[3]/section/div/div[1]/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[3]/section/div/button[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/nav/ul/li[8]/a').click()
time.sleep(3)

#RECUPERACIÓN DE CUENTA
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/header/div/div[2]/div/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/header/div/div[2]/div/div/div/div/div[3]/section/div/div[2]/a').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div/form/div[1]/input').send_keys(mail)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div/form/div[2]/input').click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
link = input("Ingrese link: ")
driver.get(link)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/form/div[1]/input').send_keys(password)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/form/div[2]/input').send_keys(password)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/form/div[3]/input').click()
time.sleep(3)

#MODIFICACIÓN DE CONTRASEÑA
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/section/div[2]/div/form/div[1]/input').send_keys(mail)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/section/div[2]/div/form/div[2]/input').send_keys(password)
input("Ingrese OK si paso Captcha: ")
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/section/div[2]/div/form/div[5]/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[3]/section/div/button[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/nav/ul/li[7]/a').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/section[3]/div/ul/li[1]/a').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/section[3]/div/ul/li[1]/form/div/div[1]/input').send_keys(password)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/section[3]/div/ul/li[1]/form/div/div[2]/input').send_keys(password)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/section[3]/div/ul/li[1]/form/div/div[3]/button').click()
time.sleep(5)

driver.close()
