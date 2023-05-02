from datetime import date, timedelta
import calendar

dsthu = {"hai":0, "ba":1, "tư":2, "năm":3, "sáu":4, "bảy":5, "chủ nhật":6}
dsthud = {0:"hai", 1:"ba", 2:"tư", 3:"năm", 4:"sáu", 5:"bảy", 6:"chủ nhật"}

tod = date.today()

def ngay_thang(n = 0):
    return str(tod + timedelta(days=n))

def thu_(t = 0):
    a = ngay_thang(t).split("-")
    a = [int(x) for x in a]
    thu_ = calendar.weekday(*a)
    return dsthud[thu_]

def ngay_cua_thu(thu, tuan = 0):
    thu = dsthu[thu]
    chenh_lech = thu - dsthu[thu_()] + tuan*7
    return ngay_thang(chenh_lech)