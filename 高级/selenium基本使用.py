from selenium import webdriver

path = 'chromedriver.exe'
driver = webdriver.Chrome(chrome_options=path, )
url = 'https://www.baidu.com'
driver.get(url)
