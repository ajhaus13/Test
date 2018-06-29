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

call(['/usr/bin/open', '/Applications/Spotify.app'])
time.sleep(5)
pyautogui.press('space')

# pyautogui.keyDown('command')
# pyautogui.press('t')
# pyautogui.keyUp('command')
# pyautogui.typewrite('spotify.com')
# pyautogui.press('enter')
# time.sleep(5)
# pyautogui.typewrite('\t'*6)
# pyautogui.press('enter')
# time.sleep(6)
# pyautogui.typewrite('\t'*5)
# pyautogui.press('enter')
# time.sleep(3)
# pyautogui.typewrite('\t'*7)
# pyautogui.press('enter')
