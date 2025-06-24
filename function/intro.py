import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
import os 

file_name = os.path.dirname(os.path.abspath(__file__))+"\AI(v2).mp4"
window_name = "window"
interframe_wait_ms = 30

def start():
	cap = cv2.VideoCapture(file_name)
	if not cap.isOpened():
		print("Error: Could not open video.")
		exit()

	cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
	cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

	player = MediaPlayer(file_name)

	while (True):
		ret, frame = cap.read()
		audio_frame , val = player.get_frame()
		if not ret:
			print("Reached end of video, exiting.")
			break
		
		cv2.imshow(window_name, frame)
		if cv2.waitKey(interframe_wait_ms) & 0x7F == ord('q'):
			print("Exit requested.")
			break
		if val != 'eof' and audio_frame is not None:
				#audio
				img, t = audio_frame

	cap.release()
	cv2.destroyAllWindows()