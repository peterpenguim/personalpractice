import pyautogui
import time


pyautogui.alert("Pressione OK para inciar o programa.")
pyautogui.PAUSE = 1
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/u/0/my-drive')
pyautogui.press('enter')

pyautogui.hotkey('winleft', 'd')
pyautogui.moveTo(1300, 30)
pyautogui.mouseDown()
pyautogui.moveTo(650, 450)
pyautogui.hotkey('alt', 'tab')
pyautogui.mouseUp()
time.sleep(3)

pyautogui.alert('O programa finalizou.')