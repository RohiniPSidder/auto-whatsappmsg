# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time
import pandas as pd

df = pd.read_excel('numbers.xlsx')
time.sleep(20)

# Config
login_time = 30    # Time for login (in seconds)
new_msg_time = 7   # TTime for a new message (in seconds)
send_msg_time = 7  # Time for sending a message (in seconds)
country_code = 91   # Set your country code

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)

for index, row in df.iterrows():
        num = str(row['phone number'])
        msg = str(row['message'])
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}&text={msg}'
        driver.get(link)
        time.sleep(new_msg_time)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(send_msg_time)

# Quit the driver
driver.quit()
