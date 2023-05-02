from requests_html import HTMLSession
import pyautogui as py
import pyperclip as cl
from time import sleep

s = HTMLSession()

def tim(content):
    url = f"https://www.google.com/search?q={content}"
    r = s.get(url, headers={"User_Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'})
    try:
        result = r.html.find("div.PZPZlf.hb8SAc", first = True).text
    except:
        try:
            result = r.html.find("span.hgKElc", first = True).text
        except:
            try:
                result = r.html.find("div.Z0LcW", first = True).text
            except:
                try:
                    result = ("đây là các kết quả tôi tìm được")
                except:
                    result = "NULL"
    if result != "NULL":
        py.hotkey("win", "8")
        sleep(2)
        py.hotkey("ctrl", "t")
        cl.copy(url)
        py.hotkey("ctrl", "v")
        py.press("enter")
    return result

def dong():
    py.hotkey("ctrl", "w")

