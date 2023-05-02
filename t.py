# listen = input()

# chu_so = {
# 	"một":1,
# 	"hai":2,
# 	"ba":3,
# 	"bốn":4,
# 	"năm":5,
# 	"sáu":6,
# 	"bảy":7,
# 	"tám":8,
# 	"chín":9,
# 	"mười":10,
# 	"mười một":11,
# 	"mười hai ":12,
# 	"mười ba":13,
# 	"mười bốn":14,
# 	"mười lăm":15,
# 	"mười sáu":16,
# 	"mười bảy":17,
# 	"mười tám":18,
# 	"mười chín":19,
# 	"hai mươi":20,
# 	"hai mươi mốt":21,
# 	"hai mươi hai":22,
# 	"hai mươi ba":23,
# 	"hai mươi bốn":24,
# 	"hai mươi lăm":25,
# 	"hai mươi sáu":26,
# 	"hai mươi bảy":27,
# 	"hai mươi tám":28,
# 	"hai mươi chín":29,
# 	"hai mốt":21,
# 	"hai hai":22,
# 	"hai ba":23,
# 	"hai bốn":24,
# 	"hai lăm":25,
# 	"hai sáu":26,
# 	"hai bảy":27,
# 	"hai tám":28,
# 	"hai chín":29,
# 	"ba mươi":30,
# 	"ba mươi một":31,
# 	"ba mươi hai":32,
# 	"ba mươi ba":33,
# 	"ba mươi bốn":34,
# 	"ba mươi lăm":45,
# 	"ba mươi sáu":36,
# 	"ba mươi bảy":37,
# 	"ba mươi tám":38,
# 	"ba mươi chín":39,
# 	"ba một":31,
# 	"ba hai":32,
# 	"ba ba":33,
# 	"ba bốn":34,
# 	"ba lăm":45,
# 	"ba sáu":36,
# 	"ba bảy":37,
# 	"ba tám":38,
# 	"ba chín":39,
# 	"bốn mươi":40,
# 	"bốn mươi một":41,
# 	"bốn mươi hai":42,
# 	"bốn mươi ba":43,
# 	"bốn mươi bốn":44,
# 	"bốn mươi lăm":45,
# 	"bốn mươi sáu":46,
# 	"bốn mươi bảy":47,
# 	"bốn mươi tám":48,
# 	"bốn mươi chín":49,
# 	"bốn một":41,
# 	"bốn hai":42,
# 	"bốn ba":43,
# 	"bốn bốn":44,
# 	"bốn lăm":45,
# 	"bốn sáu":46,
# 	"bốn bảy":47,
# 	"bốn tám":48,
# 	"bốn chín":49,
# 	"năm mươi":50,
# 	"năm mươi một":51,
# 	"năm mươi hai":52,
# 	"năm một":51,
# 	"năm hai":52,
# }



# if "thứ" in listen and "là ngày" in listen:
# 		if "tuần" not in listen:
# 			tuan_ = 0
# 			if "hai" in listen:
# 				thu_ = "hai"
# 			elif "ba" in listen:
# 				thu_ = "ba"
# 			elif "tư" in listen:
# 				thu_ = "tư"
# 			elif "năm" in listen:
# 				thu_ = "năm"
# 			elif "sáu" in listen:
# 				thu_ = "sáu"
# 			elif "bảy" in listen:
# 				thu_ = "bảy"
# 			elif "chủ nhật" in listen:
# 				thu_ = "chủ nhật"

# 		elif 'tuần' in listen:
# 			if "tuần trước" in listen:
# 				tuan_ = -1
# 			elif "tuần sau" in listen or "tuần tới" in listen:
# 				tuan_ = 1
			
# 			split = listen.split()

# 			if split.index("tuần")-1 in chu_so:
# 				tuan_ = tuan_ * chu_so(split.index("tuần")-1)

# print(thu_, tuan_)

import numpy as np
import cv2

# Capture video from file
cap = cv2.VideoCapture('D:\\Documents\\Hana assistant\\intro.mp4')

while True:

    ret, frame = cap.read()

    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)


        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()