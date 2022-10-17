import pyautogui, time

f = open("beemovie.txt",'r')
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")

	
