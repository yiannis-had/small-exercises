import time
import win32.win32api
import re
import requests
import pyperclip
from selenium import webdriver


url = " "

ignore = [
    "AQGM-G4W9DR-5SHBS",
    "AQB7-9FCCK3-M6LGA",
    "AQBQ-S2DAAC-M3KBP",
    "AQGF-GSY77H-LXSB6",
    "AQ6W-NMPZK3-72SB9",
    "AQ2Z-AYB46G-KFNBZ",
    "AQWE-CM87M9-3ZABL",
    "AQGM-G4W9DR-5SHBS",
]


def getregex():

    r = requests.get(url)
    text = r.text
    global regex
    regex = re.findall("[A-Z0-9]{4,6}\-[A-Z0-9]{4,6}\-[A-Z0-9]{4,6}", text)
    return regex


browser = webdriver.Edge()
browser.get("https://www.amazon.co.uk/gc/redeem")
giftcard = browser.find_element_by_id("gc-redemption-input")

while 1:
    if getregex() == ignore:
        print(regex)
    else:
        giftcard.send_keys(regex[0])
        giftcard.submit()
        pyperclip.copy(regex[0])
        win32.win32api.MessageBox(0, "CHANGED", "CHANGED", 0x00001000)
        print("Changed")
        break
