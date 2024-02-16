'''
Created on Sep 23, 2023

@author: EnderWolf
'''
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

def main():
    print("This program (Should!) automatically take care of most dailies for you.")
    print("Just keep an eye out for it, and make sure no formats have changed, and")
    print("That your browser is still in the same place it was before!")
    
    keyboard = KeyboardController()
    mouse = MouseController()
    
    
    ##Browser-Based Variables    
    browserStartPos = (72, 1062)
    addrBarPos = (559, 52)
    
    frAddr = "https://www1.flightrising.com/"
    pfAddr = "https://pokefarm.com/party"
    
    ##Flight Rising Variables
    dragLairPos =   (544, 323)
    dlFeedPos       =   (1351, 303)
    dlFeedNokayPos      =   (951, 600)
    dlFeedOkayPos       =   (951, 633)
    dlFirstDragPos  =   (771, 491)
    dlDragBondPos       =   (1273, 793)
    dlDragBondClosePos  =   (983, 690)
    dlNextDragPos       =   (1150, 692)
    gatherPos   =   (544, 355)
    gatherHuntPos   =   (812, 675)
    gatherFishPos   =   (1052, 675)
    gatherBugPos    =   (1295, 675)
    gatherRepeatPos =   (1109, 760)
    gatherStopPos   =   (962, 760)
    
    ##Pokefarm Variables
    fieldsPos   =   (107, 210)
    publicViewPos   =   (947, 1000)
    centeredPos     =   (947, 775)
    scourPos   =   (335, 210)
    firstScourPos   =   (757, 475)
    firstScourEndPos=   (817, 490)
    secondScourPos  =   (1079, 475)
    secScourEndPos  =   (1138, 490)
    thirdScourPos   =   (1401, 475)
    thirdScourEndPos=   (1458, 490)
    playersPos  =   (845, 95)
    openAllPos      =   (824, 400)
    clickPokemonPos =   (1043, 515)
    
    input("Waiting for Enter...")
    
    ##Browser Startup
    mouse.position = browserStartPos
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = addrBarPos
    mouse.click(Button.left, 1)
    keyboard.type(frAddr)
    keyboard.press(Key.enter)
    time.sleep(4)
    
    ##Flight Rising actions
    mouse.position = dragLairPos
    mouse.click(Button.left, 1)
    time.sleep(4)
    mouse.position = dlFeedPos
    mouse.click(Button.left, 1)
    time.sleep(3)
    mouse.position = dlFeedOkayPos
    mouse.click(Button.left, 1)
    mouse.position = dlFeedNokayPos
    mouse.click(Button.left, 1)
    time.sleep(3)
    mouse.position = dlFirstDragPos
    mouse.click(Button.left, 1)
    time.sleep(3)
    for x in range(50):
        mouse.position = dlDragBondPos
        mouse.click(Button.left, 1)
        time.sleep(1)
        keyboard.type(" ")
        time.sleep(1)
        mouse.position = dlNextDragPos
        mouse.click(Button.left, 1)
        time.sleep(2)
    mouse.position = addrBarPos
    mouse.click(Button.left, 1)
    keyboard.type(frAddr)
    keyboard.press(Key.enter)
    time.sleep(4)
    mouse.position = gatherPos
    mouse.click(Button.left, 1)
    time.sleep(3)
    mouse.position = gatherHuntPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = gatherRepeatPos
    for x in range(3):
        mouse.click(Button.left, 1)
        time.sleep(1)
    mouse.position = gatherStopPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = gatherFishPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = gatherRepeatPos
    for x in range(2):
        mouse.click(Button.left, 1)
        time.sleep(1)
    mouse.position = gatherBugPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = gatherRepeatPos
    for x in range(2):
        mouse.click(Button.left, 1)
        time.sleep(1)
    
    
    
    ##Switch to Pokefarm
    mouse.position = addrBarPos
    mouse.click(Button.left, 1)
    keyboard.type(pfAddr)
    keyboard.press(Key.enter)
    time.sleep(4)
    
    ##Pokefarm Autorun
    mouse.position = fieldsPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = publicViewPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = centeredPos
    for x in range(14):
        keyboard.type('1')
        for z in range(50):
            mouse.click(Button.left, 1);
            time.sleep(0.1)
        keyboard.type('d')
        time.sleep(0.5)
    for y in range(4):
        for w in range(7):
            keyboard.type('{0}'.format(y+1))
            for v in range(50):
                mouse.click(Button.left, 1)
                time.sleep(0.1)
            keyboard.type('d')
            time.sleep(0.5)
    mouse.position = scourPos
    mouse.click(Button.left, 1)
    time.sleep(3)
    mouse.position = firstScourPos
    mouse.click(Button.left, 1)
    mouse.position = secondScourPos
    mouse.click(Button.left, 1)
    mouse.position = thirdScourPos
    mouse.click(Button.left, 1)
    time.sleep(3)
    mouse.position = firstScourEndPos
    mouse.click(Button.left, 1)
    mouse.position = secScourEndPos
    mouse.click(Button.left, 1)
    mouse.position = thirdScourEndPos
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.position = playersPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = openAllPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = clickPokemonPos
    for x in range(5):
        for y in range(350):
            mouse.click(Button.left, 1)
            time.sleep(0.1)
        time.sleep(4)
        

if __name__ == '__main__':
    main()