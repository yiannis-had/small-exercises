import hashlib
import time
import win32.win32api
import re
import requests
import pyperclip


url = "https://chipmonkzslots.com/offers"

sleeptime = 2

ignore = [
    "AQ6W-NMPZK3-72SB9",
    "AQB7-9FCCK3-M6LGA",
    "AQBQ-S2DAAC-M3KBP",
    "AQGF-GSY77H-LXSB6",
    "AQ6W-NMPZK3-72SB9",
]


def getHash():

    r = requests.get(url)
    text = r.text
    global regex
    regex = re.findall("[A-Z0-9]{4,6}\-[A-Z0-9]{4,6}\-[A-Z0-9]{4,6}", text)
    print(regex)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


current_hash = getHash()

while 1:
    if getHash() == current_hash or regex == ignore:
        print("Not Changed")
    else:
        pyperclip.copy(regex[0])
        win32.win32api.MessageBox(0, "CHANGED", "CHANGED", 0x00001000)
        print("Changed")
        break
    time.sleep(sleeptime)
