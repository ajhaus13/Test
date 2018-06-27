from subprocess import Popen, call
import pyautogui
import time

call(['/usr/bin/open', '/Applications/Google Chrome.app'])


pyautogui.keyDown('command')
pyautogui.press('t')
pyautogui.keyUp('command')
pyautogui.typewrite('facebook.com')
pyautogui.press('enter')
pyautogui.keyDown('command')
pyautogui.press('t')
pyautogui.keyUp('command')
pyautogui.typewrite('weather austin texas')
pyautogui.press('enter')
pyautogui.keyDown('command')
pyautogui.press('t')
pyautogui.keyUp('command')
pyautogui.typewrite('spotify.com')
pyautogui.press('enter')
time.sleep(4)
pyautogui.click(x = 229, y = 615)
time.sleep(3)
pyautogui.moveTo(x = 330, y = 335)
pyautogui.click()

