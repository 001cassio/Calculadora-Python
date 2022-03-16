from time import sleep
import pyautogui, pyperclip

#este codigo manda mensagem para o contato que estver aberto, comeco de uso do pyautogui
sleep(5)
for i in range(100):
    pyperclip.copy("te amo bb")
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")


#o codigo para descobrir a posicao de um item e pyautogui.position(), o ideial e usar um time sleep e usar a funcao