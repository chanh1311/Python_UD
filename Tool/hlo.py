from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


path = ChromeDriverManager().install()
driver = webdriver.Chrome(path)

#thiết lập trình duyệt
driver.get("http://www.python.org")
#xacs nhan python co trong tieu de
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.quit()