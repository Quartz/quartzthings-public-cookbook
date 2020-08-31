from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time


#==== setup ====#

driver = webdriver.Chrome() # I'm using Chrome, you might need to switch to your installed driver
user_name = "itc@yerit.com" # username and pw are media credentials from y@qz.com
pw = "film"
products = ["12019010","87032362","27111200","87032342"] # this is an example list of HS codes in eight digits


#==== launch & login ====#

driver.get('https://www.trademap.org/')

driver.find_element_by_id('ctl00_MenuControl_marmenu_login').click();

time.sleep(1) # wait for the broswer to respond..

login_url = driver.find_element_by_id('iframe_login').get_attribute("src")
driver.get(login_url);

login_email = driver.find_element_by_id('PageContent_Login1_UserName');
login_email.clear()
login_email.send_keys(user_name) 

login_email = driver.find_element_by_id('PageContent_Login1_Password');
login_email.clear()
login_email.send_keys(pw)

driver.find_element_by_id('PageContent_Login1_Button').click(); # click on login

time.sleep(1)


#==== navigate to the page & download ====#

for product in products:

	print product

	# navigate to the URL (this is an example of US imported products from China)

	driver.get("https://www.trademap.org/Country_SelCountry_MQ_TS.aspx?nvpm=1%7c156%7c%7c%7c%7c" 
		+ product + "%7c%7c%7c8%7c1%7c1%7c1%7c2%7c3%7c2%7c1%7c1")

	# change the number of display rows to 20 (max)

	numOfColumnOpt = Select(driver.find_element_by_id('ctl00_PageContent_GridViewPanelControl_DropDownList_NumTimePeriod'))
	numOfColumnOpt.select_by_value("20")

	# click the button to download an excel file

	elem = driver.find_element_by_id("ctl00_PageContent_GridViewPanelControl_ImageButton_ExportExcel")
	elem.click()

	time.sleep(2)



driver.close()
