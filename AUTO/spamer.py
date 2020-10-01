import pyautogui
time.sleep(5)

f = open("spam message text", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")








