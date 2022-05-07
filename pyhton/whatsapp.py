import pyautogui
import pyperclip
import time

telefone = input('Telefone >> ')
mensagem = input('Mensagem >> ')
quantidade = int(input('Quantidade >> '))
pyperclip.copy('https://web.whatsapp.com/send?phone={}&text={}'.format(telefone, mensagem))

pyautogui.PAUSE = 1

for i in range(quantidade):
    pyautogui.press('winleft')
    pyautogui.write('gx')
    pyautogui.press('enter')
    time.sleep(5)
    with pyautogui.hold('ctrl'):
        pyautogui.press('v')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(650, 380)
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'f4')

pyautogui.alert('Fim do programa.')