from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import logging
prnt = logging.getLogger(__name__) 

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set Chrome options for headless mode and disable sandboxing
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU (no need in headless mode)
chrome_options.add_argument("--no-sandbox")  # Disable sandboxing (required in CI environments)
chrome_options.add_argument("--remote-debugging-port=9222")  # For debugging in some cases

# Initialize the WebDriver with the configured options
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)


driver.get("https://the-internet.herokuapp.com/broken_images")

broken_Images = driver.find_element(By.XPATH, '//*[@id="content"]/div/h3')

wait = WebDriverWait(driver, timeout=2)
wait.until(lambda d : broken_Images.is_displayed())
time.sleep(3)

images = driver.find_elements(By.TAG_NAME,"img")
print("\n")
prnt("\n")

for img in images:
    src = img.get_attribute("src")
    
    natural_width = img.get_attribute('naturalWidth')
    natural_height = img.get_attribute('naturalHeight')
    
    if natural_width == '0' or natural_height == '0':
        print(f"Broken Image: {src}")
        prnt(f"Broken Image: {src}")
        
    else:
        print(f"Image OK: {src}")
        prnt(f"Broken Image: {src}")


driver.quit()
