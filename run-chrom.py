from selenium import webdriver

#id=identifierId
#name=password
#class=VfPpkd-vQzf8d

un = ""
pw = ""
driver = "/home/pi/Documents/homepage_login/chromedriver"

#sets chrome options
options = webdriver.ChromeOptions()
options.add_argument('start-fullscreen')
options.add_experimental_option("excludeSwitches", ['enable-automation']) #removes "Chrome is being controlled by automation" message
driver = webdriver.Chrome(options=options) #opens Chromium

#navigates to website and waits 10s
url=""
driver.get(url)
driver.implicitly_wait(10)

#username input
driver.find_element_by_id("identifierId").send_keys(un)
driver.find_element_by_class_name("VfPpkd-vQzf8d").click()
#password input
driver.find_element_by_name("password").send_keys(pw)
driver.find_element_by_class_name("VfPpkd-vQzf8d").click()
