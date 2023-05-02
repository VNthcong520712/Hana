from function import nghe, noi

def hey():
	while True:
		listen = nghe.nghe_()
		if "hey" in listen or "hana" in listen or "em" in listen or "ơi" in listen:
			noi.doc("Dạ em nghe!")