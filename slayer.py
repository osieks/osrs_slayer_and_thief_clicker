#pip3 install pyautogui
import pyautogui
import time

def find_red(ilosc_klikniec, czas_walki,debug):
    found = 0
    conf = 1
    conf_step = 0.02

    for i in range(0, ilosc_klikniec):
        while found==0:
            if debug==1:
                print('conf'+str(conf))
            red_location = pyautogui.locateCenterOnScreen('find3.png',confidence=conf)
            if(red_location != None):
                red_location = pyautogui.locateCenterOnScreen('find2.png',confidence=conf)
            #red_location = pyautogui.locateCenterOnScreen('red_pixel2.png')
            if debug==1:
                print(red_location)
            if(red_location != None):
                if debug==1:
                    print('found')
                    pyautogui.moveTo(red_location)
                else:
                    pyautogui.click(red_location)
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
                time.sleep(1)
                print("Sleeping "+str(i))
        else:
            time.sleep(czas_walki)


ilosc_klikniec = 1000
czas_walki = 15
debug=0

find_red(ilosc_klikniec,czas_walki,debug)
