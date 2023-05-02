from requests_html import HTMLSession

s = HTMLSession()

def thoigian(look_up = None):
    if look_up == None:
        look_up = "thời gian tại Việt nam"
        
    try:
        url = f"https://www.google.com/search?q={look_up}"
        r = s.get(url, headers={"User_Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'})
        time_local = r.html.find("div.gsrt.vk_bk.FzvWSb.YwPhnf", first = True)
    except:
        return "NULL"
    result = time_local #.split("\n")
    return time_local

if __name__ == "__main__":
    print(thoigian())