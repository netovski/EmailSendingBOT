import pyautogui
from time import sleep

# extrair cada sg
# 	clicar no historico de garantias
pyautogui.click(107,321,duration=2)
# 	clicar em pesquisar
pyautogui.click(959,228,duration=2)
# 	clicar e digitar nr da sg
with open('sgs.txt','r') as arquivo:
    for linha in arquivo:
        sg = linha
        pyautogui.click(435,113,duration=0.5)
        pyautogui.write(sg)
        sleep(1)  
# 	clique duplo
        pyautogui.doubleClick(441,316,duration=2)
# 	clicar em relatorio
        pyautogui.click(962,680,duration=4)
# 	clicar no historico de garantias
        pyautogui.click(107,321,duration=0.5)
# aguardar 
if not sg:
    print("lista percorrida")