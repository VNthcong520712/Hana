from function import intro, mo_ung_dung, ngay_thang, nghe, noi, thoi_gian, thoi_tiet, tim_kiem, kiem_tra_mang
from time import sleep
import winsound as win
import sys
import random as ran

# kiểm tra kết nối mạng --------------------------------------------------
noi.offline("Attention! please connect wifi")
sleep(2)
noi.offline("System is running")
wait = 0
while not kiem_tra_mang.connect():
	if wait == 6:
		noi.offline("We can not connect wifi, shutting down")
		sys.exit()
	noi.offline("failed to connect, check your network and try again")
	sleep(10)
	wait += 1
sleep(10)
noi.doc("Đã kết nối")

# bắt đầu chương tình ----------------------------------------------------
for i in range(3):
	win.Beep(3800, 50)
sleep(2)
intro.start()
noi.doc("Đã khởi động xong, trợ lý Hana xin chào")
sleep(1)

# xử lý ------------------------------------------------------------------
noi.doc("Hana có thể giúp gì ạ!")
while True:
	listen = input('::')#nghe.nghe_()
	listen = listen.strip()
	print(listen)

	# kêu gọi ------------------------------------------------------------
	if "hana" in listen or "em" in listen:
		dic = {0:"Dạ em nghe", 1:"Em đây ạ", 2:"Em đang nghe đây ạ", 3:"Em nghe nè", 4:" Em có thể giúp gì ạ", 5:"Dạ dạ Hana đây"}
		noi.doc(dic[ran.randint(0, 5)])
		continue

	# xem giờ ------------------------------------------------------------
	elif "giờ" in listen or "thời gian" in listen or "bây giờ là" in listen: 
		ket_qua_gio = thoi_gian.thoigian(listen)
		if ket_qua_gio == 'NULL':
			noi.doc("không tìm thấy kết quả, thử lại giúp Hana nhé")
		else:
			noi.doc("bây giờ là " + ket_qua_gio)
	# ngày của thứ, tuần -------------------------------------------------
	elif "thứ" in listen and "là ngày" in listen:
		if "tuần" not in listen:
			if "hai" in listen:
				thu_ = "hai"
			elif "ba" in listen:
				thu_ = "ba"
			elif "tư" in listen:
				thu_ = "tư"
			elif "năm" in listen:
				thu_ = "năm"
			elif "sáu" in listen:
				thu_ = "sáu"
			elif "bảy" in listen:
				thu_ = "bảy"
			elif "chủ nhật" in listen:
				thu_ = "chủ nhật"

		elif 'tuần' in listen:
			if "tuần trước" in listen:
				tuan_ = -1
			elif "tuần sau" in listen or "tuần tới" in listen:
				tuan_ = 1
			
			split = listen.split()

			if split.index("tuần")-1 in chu_so:
				thu_ = chu_so(split.index("tuần")-1)

	# xem ngày -----------------------------------------------------------
	elif "thứ" not in listen:
		if "hiện tại" in listen or "hôm nay" in listen :
			dinh_dang = "hôm nay "
			ngay = 0
		elif "ngày mai" in listen:
			dinh_dang = "ngày mai "	
			ngay = 1
		elif "ngày mốt" in listen:
			dinh_dang = "ngày mốt "
			ngay = 2
		elif "ngày kia" in listen:
			dinh_dang = "ngày kia "
			ngay = 3
		elif "hôm qua" in listen:
			dinh_dang = "hôm qua "
			ngay = -1
		elif "hôm kia" in listen:
			dinh_dang = "hôm kia "
			ngay = -2

		if "ngày" in listen:
			try:
				ket_qua_ngay = ngay_thang.ngay_thang(ngay)
				if ket_qua_ngay != "NULL":
					noi.doc(dinh_dang+"là ngày " + ket_qua_ngay+" ạ")
			except:
				noi.doc("xin lỗi, Hana không thể tìm thấy kết quả, thử lại giúp Hana nhé!")

	# kiểm tra thứ -------------------------------------------------------
	elif "thứ" in listen:
		if "hiện tại" in listen or "hôm nay" in listen :
			dinh_dang = "hôm nay "
			ngay_ = 0
		elif "ngày mai" in listen:
			dinh_dang = "ngày mai "	
			ngay_ = 1
		elif "ngày mốt" in listen:
			dinh_dang = "ngày mốt "
			ngay_ = 2
		elif "ngày kia" in listen:
			dinh_dang = "ngày kia "
			ngay_ = 3
		elif "hôm qua" in listen:
			dinh_dang = "hôm qua "
			ngay_ = -1
		elif "hôm kia" in listen:
			dinh_dang = "hôm kia "
			ngay_ = -2

		try:
			ket_qua_thu = ngay_thang.thu_(ngay_)
			if ket_qua_thu != "NULL":
				noi.doc(dinh_dang+"là thứ " + ket_qua_thu+" ạ")
		except:
			noi.doc("xin lỗi, Hana không thể tìm thấy kết quả, thử lại giúp Hana nhé!")
