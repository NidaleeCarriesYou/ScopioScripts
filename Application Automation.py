import pyautogui
import time
import keyboard
import random
import win32api, win32con

Test_number = int(input("how many tests do you want to run? please enter only a number! "))
Clicked = 0
Test_number2 = Test_number

Set_Machine_details_yes_or_no = input("Is 'Set Machine Details' among the tests? Please enter 'yes' or 'no' ")
if Set_Machine_details_yes_or_no == "yes":
    Machine_Type = input("Please enter 'X100' or 'HT' based on machine type! ")
    HT_SN = input("Please enter the X100/X100HT S/N ")
    Camera_SN = input("Please enter the camera S/N ")
else:
    Clicked = 10

print("I'm gonna take it from here... go drink some coffee :) ")




while Test_number > 0:
    if Clicked == 0 and pyautogui.locateOnScreen('Set_Machine_Details.png') != None:
        if pyautogui.locateOnScreen('Set_Machine_Details.png') != None and Set_Machine_details_yes_or_no == "yes" and Clicked == 0:
            pyautogui.click(960, 540)
            pyautogui.press('tab')
            pyautogui.write(HT_SN)
            time.sleep(1)
            pyautogui.press('tab')
            pyautogui.write(Camera_SN)
            time.sleep(1)
            for i in range(4):
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.write("0")
                time.sleep(1)
            if Machine_Type == "HT":
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('enter')
            elif Machine_Type == "X100":
                pyautogui.press('tab')
                pyautogui.press('spacer')
                pyautogui.press('up')
                pyautogui.press('enter')
                pyautogui.press('tab')
                pyautogui.press('enter')
            pyautogui.locateOnScreen('Save.png')
            pyautogui.click(960, 540)
            time.sleep(1)
            pyautogui.click('Save.png')
            while Clicked == 0:
                if pyautogui.locateOnScreen('Dismiss.png') != None:
                    Clicked = 10
                    pyautogui.click('Dismiss.png')
                    time.sleep(2)
                else:
                    time.sleep(5)
            time.sleep(2)
            if pyautogui.locateOnScreen('Next2.png') != None:
                n, m = pyautogui.locateCenterOnScreen('Next2.png')
                pyautogui.click(n, m)
                time.sleep(0.5)
                Test_number -= 1
    elif pyautogui.locateOnScreen('Run_Tests.png') != None:
        x, y = pyautogui.locateCenterOnScreen('Run_Tests.png')
        pyautogui.click('Run_Tests.png')
        time.sleep(0.5)
    elif pyautogui.locateOnScreen('Approve.png') != None:
        x, y = pyautogui.locateCenterOnScreen('Approve.png')
        pyautogui.click('Approve.png')
        time.sleep(0.5)
    elif pyautogui.locateOnScreen('Next.png') != None:
        x, y = pyautogui.locateCenterOnScreen('Next.png')
        pyautogui.click(x,y)
        time.sleep(0.5)
        Test_number -= 1
    elif pyautogui.locateOnScreen('I_have_followed_the_instructions.png') != None:
        x, y = pyautogui.locateCenterOnScreen('I_have_followed_the_instructions.png')
        pyautogui.click('I_have_followed_the_instructions.png')
        time.sleep(0.5)
    else:
        # print("Image not found. Retrying...")
        time.sleep(1)  # Add a delay before the next attempt
        pyautogui.click(960,540)

print("I'm all done! all " + str(Test_number2) + " tests have finished successfully! ")
input("Press any key to exit! ")








# time.sleep(5)
# approve_ = (pyautogui.position())
# print(approve)
# print(pyautogui.pixel(x=-1323, y=880))


### color of approve and next rgb(77, 88, 164)
