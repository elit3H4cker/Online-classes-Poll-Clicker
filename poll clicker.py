import pyautogui
print("press ctrl-c to quit")
try:
       while True:
            if(pyautogui.locateOnScreen('search.png')!=None):
             pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('search.png')))

except KeyboardInterrupt:
    print('\nDone.')

