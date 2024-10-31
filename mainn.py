from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

driver_path = 'C:\\Users\\HP\\Desktop\\chromedriver-win64\\chromedriver.exe'

options = Options()
options.add_argument('--headless')  
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.upwork.com/freelance-jobs/')

driver.quit()
