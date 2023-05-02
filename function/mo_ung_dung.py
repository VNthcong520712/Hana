import pyautogui as pya

def mo(app):	
	pya.press("win")
	pya.write(app, interval=0.2)
	pya.press("enter")