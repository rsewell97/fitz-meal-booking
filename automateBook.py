from selenium import webdriver
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

date_to_book = '21/11/2018'
meal_type = 2
nut_free = False
add_info = ''

ddate, dmonth, dyear = date_to_book.split('/')
meal_type = meal_types[str(meal_type)]

months = {
    '01': 'Jan',
    '02': 'Feb',
    '03': 'Mar',
    '04': 'Apr',
    '05': 'May',
    '06': 'Jun',
    '07': 'Jul',
    '08': 'Aug',
    '09': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec'
    }
dmonth = months[dmonth]

driver = webdriver.Chrome()
driver.get('https://collegebills.fitz.cam.ac.uk/collegebill/')

def ravenAuth(crsid,password):
    driver.find_element_by_name('userid').send_keys(crsid)
    tmp = driver.find_element_by_name('pwd')
    tmp.send_keys(password)
    tmp.submit()

if 'https://raven.cam.ac.uk/' in driver.current_url:
    ravenAuth()

driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnContinue"]').click()
#im in

sdate, smonth, syear = 0,'',0
while (sdate != ddate) and (smonth != dmonth) and (syear != dyear):
    _, sdate, smonth, syear = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_lblSitting"]').text.split(' ')

    nxt = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_calMealDates"]/tbody/tr[1]/td/table/tbody/tr/td[3]/a')
    prv = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_calMealDates"]/tbody/tr[1]/td/table/tbody/tr/td[1]/a')

    if int(syear) > int(dyear):
        nxt.click()
    else: #right year
        if smonth != dmonth:
            nxt.click()
        else: #right month
            table_entries = driver.find_elements_by_tag_name('td')
            table_entries = [x for x in table_entries if x.text.isdigit()]
            if int(ddate) < 15:
                #iterate from start
                for i in table_entries:
                    if i.text == ddate:
                        i.click()  
                        break
                break           
            else:
                #iterate from end            
                for i in reversed(table_entries):
                    if i.text == ddate:
                        i.click() 
                        break
                break   

#now just actually book it
while True:
    try:
        driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnBook"]').click()
        break
    except:
        time.sleep(10)

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

driver.quit()   #quit