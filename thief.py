#pip3 install pyautogui
import pyautogui
import time
import keyboard  # using module keyboard

tab_zdjec = ['ard.png','ard2.png']

pyautogui.FAILSAFE = False

def find_red(czas_walki,debug):
    found = 0
    conf = 1
    conf_step = 0.2
    
    print('no. images= '+str(len(tab_zdjec)))
    while(True):
        if keyboard.is_pressed('q'):
            raise
        while found==0:
            if keyboard.is_pressed('q'):
                raise
            prev_mouse_location = pyautogui.position()
            print('conf'+str(conf))

            red_location = None
            for z in range(len(tab_zdjec)):
                print(tab_zdjec[z])
                red_location = pyautogui.locateCenterOnScreen(tab_zdjec[z],confidence=conf, grayscale=False)
            #red_location = pyautogui.locateCenterOnScreen('red_pixel2.png')
            if debug==1:
                print(red_location)
            if(red_location != None):
                if debug==1:
                    print('found')
                    pyautogui.moveTo(red_location)
                else:
                    pyautogui.click(red_location)
                    pyautogui.moveTo(prev_mouse_location)
                found = 1
                print("found")
            else:
                conf=conf-conf_step
                if conf<conf_step:
                    conf=1
        
        conf = 1
        found = 0

        if debug==1:
            for i in range(0,czas_walki):
                time.sleep(0)
                print("Sleeping "+str(i))
        else:
            time.sleep(czas_walki)

czas_walki = 1
debug=1

find_red(czas_walki,debug)
