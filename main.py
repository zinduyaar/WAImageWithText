
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas
import time

excel_data = pandas.read_excel('Contacts.xlsx', sheet_name='Main')

count = 0

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('user-data-dir=C:/Users/jobsa/AppData/Local/Google/Chrome/User Data/Profile 2')
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
# driver.get("https://web.whatsapp.com")
# wait = WebDriverWait(driver, 100)

# if sending only text
# send_button_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'

# if sending text with image
send_button_path = '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div'

text_box_path='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div'
# url = 'https://web.whatsapp.com/send?phone=' + str(excel_data['Contact'][count]) + '&text=' + msg
# driver.get(url)
for index, row in excel_data.iterrows():
    try:
        url = 'https://web.whatsapp.com/send?phone=' + str(row['Mobile(country code prefix)']) + '&text=' + row['URL Encoded msg']
        
        driver.get(url)
        
        
        text_box = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.XPATH, text_box_path)))
        text_box.send_keys(Keys.CONTROL, 'v')

        click_btn = WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.XPATH, send_button_path)))
        click_btn.click()
        time.sleep(3)
        # Wait for the message to be sent
        # Wait for message status to change to "sent", "delivered", or "read"

        # all_messages = driver.find_elements(By.CLASS_NAME, 'message-out')
        # last_message = all_messages[len(all_messages)-1]
        # last_message_stats = last_message.find_element(By.XPATH, './div/div[1]/div[1]/div/div[3]/div/div/span')
        # sts = last_message_stats.get_attribute('aria-label')
        # while 'pending' in sts.strip().lower():
        #   sts = last_message_stats.get_attribute('aria-label')

        # sent_status = "sent"
        # EC.text_to_be_present_in_element
        # WebDriverWait(driver, 35).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="main"]/div[3]/div/div/div[1]/div/div/div/div[2]/div[2]'), sent_status))
        # driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '//*[@id="main"]/div[3]/div/div/div[1]/div/div/div/div[2]/div[2]')))

        count = count + 1
    except Exception as e:
        print('Failed to send message to ' + str(excel_data['Contact'][count]) + str(e))
driver.quit()
print("The script executed successfully.")


