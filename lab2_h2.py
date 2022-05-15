from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import common
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

user = [
    'ex.smirandaf@externosvolcan.cl',
    'jferjo@gmail.com',
    'jferjo@gmail.com',
    'gbiscarra@volcan.cl',
    'rcatrileo@volcan.cl',
    'Wsilva@volcan.cl',
    'jcardenas@volcan.cl',
    'dsanchez@volcan.cl',
    'cvidal@volcan.cl',
    'placroix@volcan.cl',
    'placroix@volcan.cl',
    'zrojas@volcan.cl',
    'ecalbuante@volcan.cl',
    'Jlagos@volcan.cl',
    'csomodevilla@volcan.cl',
    'afuentes@volcan.cl'
]

user1 = [
    '10120',
    '10794',
    '11121',
    '5001',
    'acatalan',
    'mledermann',
    'mpinto'
]
password = [
    '*6A75CD1A0DA6C18EB0F44D4DB04637E8CA645443',
    '*A4B6157319038724E3560894F7F932C8886EBFCF',
    '*49E5538C0E9F3FE1EA3A847ADCFB83EFB4B46E83',
    '*724DA1C4C69FE68B0AA52C529307E616E5DC3CE5',
    '*83C95A415A3CBC9D602C88BDC1178587B3F685F0',
    '*2C8E2B8A047950C5226CA2B8A3BAD016A9A0DFF3',
    '*B80CC91D3A1593CE72E0E81199DECC82D031747E',
    '*CF11544044A11397965F0A00B7695C897CECCD00',
    '*B141B461E8F96DB476458D6880BDF76D49019445',
    '*E79972E8C03E783783BC8373049AE1E47CB8B95A',
    '*3EC108783A5A8C311C48C7399073982F5170DBE1',
    '*48CFCEE57C65B4F5EE5A74158CBA81839F3F342C',
    '*AE3B473BE7550628C13F9B899B40C16B2FE3D76E',
    '*295D0D4A3494B1283639910F11F3BEEF71B401F2',
    '*E6FF5671D412D3FE3A1B4E6FE51BE6A6728CF56C',
    '*9B07EC4AEE38B0702251FD93DEBE9D130E48665D'
]

password1 = [
    '202cb962ac59075b964b07152d234b70',
    '202cb962ac59075b964b07152d234b70',
    '202cb962ac59075b964b07152d234b70',
    '202cb962ac59075b964b07152d234b70',
    '01a2747dd11b6a3765122d434fe798c9',
    '202cb962ac59075b964b07152d234b70',
    '48bc5af245d2f00733b37ddb94d57656'
]

url = 'https://tienda.volcan.cl/home-region-metropolitana/#'
url1 = 'http://www.ducassegen.cl/ducasse/index.php'

for i in range(len(user)):
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="bwp-header"]/div[1]/div[2]/div[2]/a/i').click()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(user[i])
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password[i])
    driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/div/div/div/form/div[4]/input[3]').click()
    time.sleep(1)

for i in range (len(user1)):
    try:
        driver.switch_to.alert.dismiss()    
    except common.exceptions.NoAlertPresentException:
        driver.get(url1)
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr[6]/td[2]/table/tbody/tr[2]/td[3]/input').send_keys(user1[i])
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr[6]/td[2]/table/tbody/tr[3]/td[3]/input').send_keys(password1[i])
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr[6]/td[2]/table/tbody/tr[3]/td[4]/input').click()
    time.sleep(5)