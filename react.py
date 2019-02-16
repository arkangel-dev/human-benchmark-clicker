import numpy as np
import pyautogui
import imutils
import cv2

LoopAllow = True

while LoopAllow:
	image = pyautogui.screenshot(region=(49,297, 1, 1))
	image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
	pixel = image[0,0]
	if pixel[1] == 219:
		pyautogui.click(200,300)