import os
import pyautogui
import keyboard
#pyautogui.locateCenterOnScreen('image.png')
pyautogui.PAUSE = 0.05
x = 0
while True:
    pyautogui.click(1651,519)
    if((x % 1000) == 0):
        #upgrade location sorted by least expensive upgrade
        pyautogui.click(3008,346)
       
        #clicks the lowest cookie producing mechanism first as they will
        #be most expensive/produce the most
        pyautogui.click(3112,900)
        pyautogui.click(3112,950)
        pyautogui.click(3112,830)
        pyautogui.click(3112,760)
        #pyautogui.click(3112,680)
        #pyautogui.click(3112,620)
        #pyautogui.click(3112,570)
        #pyautogui.click(3112,500)
        #pyautogui.click(3112,440)
    if(keyboard.is_pressed('q')):
        break
    if x == 1001:
        x = 0
    x+=1
    print(x)
#result = subprocess.check_output(['echo | xclip -selection c -o'])
#print(result)
#os.system('source ytd.sh')
