#!/usr/bin/python3
import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()


def send_whatsapp_message():
    phone_number = input("Enter the phone number (including country code): ")
    message = input("Enter the message: ")

    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone_number,
            message=message,
            tab_close=True
        )
        time.sleep(10)
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    send_whatsapp_message()

