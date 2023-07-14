#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def send_whatsapp_message():
    phone_number = input("Enter the phone number (including country code): ")
    message = input("Enter the message: ")

    # Wait for the browser window to be detected
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    try:
        # Switch to the existing browser window
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            break

        # Find the chat input field and send a message
        chat_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.copyable-text')))
        chat_input.send_keys(phone_number + Keys.ENTER)
        time.sleep(2)
        chat_input.send_keys(message + Keys.ENTER)

        print("Message sent!")
    except Exception as e:
        print(str(e))
    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    send_whatsapp_message()

