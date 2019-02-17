from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import base64
import time

meal_types = {
    '1':'Standard',
    '2':'*Vegetarian',
    '3':'*Gluten Free',
    '4':'Vegan',
    '5':'No Red Meat',
    '6':'Nut Free'
}

crsID, paswd = 'rms207', 'xyz'
date_to_book = '01/02/2022'
meal_type = 2
nut_free = False
add_info = ''

meal_type = meal_types[str(meal_type)]

driver = webdriver.Chrome()
driver.get('https://collegebills.fitz.cam.ac.uk/collegebill/Main.aspx?currentDate={}'.format(date_to_book))

def ravenAuth(crsid,password):
    print("Logging into Raven")
    driver.find_element_by_name('userid').send_keys(crsid)
    tmp = driver.find_element_by_name('pwd')
    tmp.send_keys(password)
    tmp.submit()
    if 'https://raven.cam.ac.uk/' not in driver.current_url:
        print("Auth success")
    else:
        driver.quit()
        raise RuntimeError("Authentication Failed: Check crsID and/or password")


if 'https://raven.cam.ac.uk' in driver.current_url:
    ravenAuth(crsID,paswd)

driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnContinue"]').click()
#authenticated

#now just actually book it
print("Found date... waiting for booking to be released")
wait = WebDriverWait(driver, 10)
while True:
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ContentPlaceHolder1_Menu1"]/ul/li[1]/a')))
    try:
        driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnBook"]').click()
        print("Found booking")
        break
    except:
        pass
    time.sleep(10)
    driver.refresh()

    if 'https://raven.cam.ac.uk' in driver.current_url:
        ravenAuth(crsID,paswd)
    

print("Specify info and book")
#now on booking page
meal = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_lstMeals"]')
for option in meal.find_elements_by_tag_name('option'):
    if option.text == meal_type:
        option.click()
        break
if nut_free:
    driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_lstDietary_0"]').click()
driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtXtraInfo"]').send_keys(add_info)
driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnBook"]').click()  #submit booking

print("BOOKED EVENT FOR {}, see booking here: {}".format(date_to_book,driver.current_url))
driver.quit()   #quit
