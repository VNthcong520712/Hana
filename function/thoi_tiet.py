from requests_html import HTMLSession
import function.ngay_thang as nt

s = HTMLSession()

def thoi_tiet_tai(city):
    if "ngày mai" in city:
        n = nt.ngay_thang(1)[9] + "-" + nt.ngay_thang(1)[6]
        city = city[:city.index("ngày mai")]+n 
    elif "ngày mốt" in city:
        n = nt.ngay_thang(2)[9] + "-" + nt.ngay_thang(2)[6]
        city = city[:city.index("ngày mốt")]+n 
    
    try:
        url = f'https://www.google.com/search?q=thời tiết {city}'
        
        r = s.get(url, headers={"User_Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'})
        
        temp = r.html.find("span#wob_tm", first = True).text
        symbol = r.html.find("div.vk_bk.wob-unit span.wob_t", first = True).text
        sta = r.html.find("div.VQF4g", first = True).find("span#wob_dc", first = True).text
        detail = r.html.find("div.wtsRwe", first = True).text
        
        detail = detail[:detail.find("km/h")+4].split("\n")
        det = ""
        for x in range(len(detail)):
            if x == len(detail)-1:
                det += detail[x]
            else:
                det += detail[x] + ", "

        out = f'thời tiết tại {city}: {temp}{symbol}, {sta}, {det}'
    except:
        out = "NULL"
    return out

