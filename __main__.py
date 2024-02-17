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
    
    ##If you're trying to set this up on a computer that isn't mine, you're going
    ##   to have to adjust ALL these variables- Save the Addresses. First, comment
    ##    out EVERYTHING below, and just remove the comment for the code block below:
    
    ##while(True):
    ##    input("Waiting for Enter...")
    ##    print(mouse.position)
        
    ##Use the tips on each variable to fill in the values- Just type in what the 
    ##   print line says, and then you should be all set! 
    
    ##Browser-Based Variables    
    browserStartPos = (72, 1062)            ##<- Where your browser is on the hotbar.
    addrBarPos = (559, 52)                  ##<- Where your address bar is on a full-screen window browser.
    
    frAddr = "https://www1.flightrising.com/"
    pfAddr = "https://pokefarm.com/party"
    
    ##Flight Rising Variables
    dragLairPos =   (544, 323)              ##<- Where the "Dragon Lair" link is.
    dlFeedPos       =   (1351, 303)         ##<- Where the "Feed" button is on the Lair Page.
    dlFeedNokayPos      =   (951, 600)      ##<- The "Okay" button when there is no feeding needed.
    dlFeedOkayPos       =   (951, 633)      ##<- The "Okay" button when dragons have been fed.
    dlFirstDragPos  =   (771, 491)          ##<- Position of the first dragon in your lair.
    dlDragBondPos       =   (1273, 793)     ##<- Where the "Bond" button is on any dragon's page.
    dlDragBondClosePos  =   (983, 690)      ##<- Where the close button for the "Bonding" pop-up is. --- OLD!!!
    dlNextDragPos       =   (1150, 692)     ##<- The right arrow button that appears when hovering over the dragon. Moves to the next dragon.
    gatherPos   =   (544, 355)              ##<- Where the "Gather Items" link is, on the main page.
    gatherHuntPos   =   (812, 675)          ##<- Where the "Hunt" button is on the Gather page.
    gatherFishPos   =   (1052, 675)         ##<- Where the "Fish" button is on the Gather page.
    gatherBugPos    =   (1295, 675)         ##<- Where the "Catch" button is on the Gather page.
    gatherRepeatPos =   (1109, 760)         ##<- When gathering, the "Repeat Gathering" button's position.
    gatherStopPos   =   (962, 760)          ##<- When gathering, the "Go back" button's position, returns to the main gather page.
    
    ##Pokefarm Variables
    fieldsPos   =   (107, 210)              ##<- The button to go to your Fields. Labeled "Fields."
    publicViewPos   =   (947, 1000)         ##<- When on your fields page, the "Go to public view" button.
    centeredPos     =   (947, 775)          ##<- Using QoL, this is the position Pokemon center to on any fields.
    scourPos   =   (335, 210)               ##<- The button to go to your Scour missions, labeled "Scours."
    firstScourPos   =   (757, 475)          ##<- The "Retrieve" button for your first scouring Pokemon.
    firstScourEndPos=   (817, 490)          ##<- The "Go" button that sends your Pokemon back out.
    secondScourPos  =   (1079, 475)         ##<- ^^ Second Scouring Pokemon's Retrieve button.
    secScourEndPos  =   (1138, 490)         ##<- ^^ Second Scouring Pokmeon's Go button.
    thirdScourPos   =   (1401, 475)         ##<- ^^^ Third Scouring Pokemon's Retrieve button.
    thirdScourEndPos=   (1458, 490)         ##<- ^^^ Third Scouring Pokemon's Go button.
    playersPos  =   (845, 95)               ##<- The link at the top of the Pokefarm Q page, saying "X players online."
    openAllPos      =   (824, 400)          ##<- On the list of players, the button labelled "Open all."
    clickPokemonPos =   (1043, 515)         ##<- Using QoL, the position of the button when the page is in the style of "Hide all Click Fast."
    
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
    
    ##Feed Dragons
    mouse.position = dlFeedPos
    mouse.click(Button.left, 1)
    time.sleep(3)
    mouse.position = dlFeedOkayPos
    mouse.click(Button.left, 1)
    mouse.position = dlFeedNokayPos
    mouse.click(Button.left, 1)
    time.sleep(3)
    
    ##Bond with Dragon Familiars
    mouse.position = dlFirstDragPos
    mouse.click(Button.left, 1)
    time.sleep(3)
        ##Default is set to 50, can adjust based on bonding needs
    for x in range(50):
        mouse.position = dlDragBondPos
        mouse.click(Button.left, 1)
        time.sleep(1)
        keyboard.type(" ")
        time.sleep(1)
        mouse.position = dlNextDragPos
        mouse.click(Button.left, 1)
        time.sleep(2)
        
    ##Return to main screen, ensures position reset to continue with gathering
    mouse.position = addrBarPos
    mouse.click(Button.left, 1)
    keyboard.type(frAddr)
    keyboard.press(Key.enter)
    time.sleep(4)
    mouse.position = gatherPos
    mouse.click(Button.left, 1)
    time.sleep(3)
    
    ##First-time Hunt gathering: 3 times, total 3
    mouse.position = gatherHuntPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = gatherRepeatPos
    for x in range(2):
        mouse.click(Button.left, 1)
        time.sleep(1)
    mouse.position = gatherStopPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    
    ##First-time Fish Gathering: 3 times, total 6
    mouse.position = gatherFishPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = gatherRepeatPos
    for x in range(2):
        mouse.click(Button.left, 1)
        time.sleep(1)
        
    #First-time Bug Gathering: 4 times, total 10
    mouse.position = gatherBugPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = gatherRepeatPos
    for x in range(3):
        mouse.click(Button.left, 1)
        time.sleep(1)
    mouse.position = gatherStopPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    
    ##If 3-day streak is active, gathering begins to work again
    ##Second Hunt: 2 times, total 12
    mouse.position = gatherHuntPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = gatherRepeatPos
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = gatherStopPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    
    ##Second Fishing Trip: 1 time, total 13
    mouse.position = gatherFishPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = gatherStopPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    
    ##Gather Bugs another 2 times, total 15
    mouse.position = gatherBugPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = gatherRepeatPos
    mouse.click(Button.left, 1)
    time.sleep(1)
    
    
    
    ##Switch to Pokefarm
    mouse.position = addrBarPos
    mouse.click(Button.left, 1)
    keyboard.type(pfAddr)
    keyboard.press(Key.enter)
    time.sleep(4)
    
    ##Pokefarm Autorun
    ##Goes to your fields, enters public view to click through your own stuff.
    mouse.position = fieldsPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = publicViewPos
    mouse.click(Button.left, 1)
    time.sleep(2)
        ##Make sure you have QoL, so that the fields are centered
    mouse.position = centeredPos
    
    ##Autoruns a default number of each field, assuming Sorted fields- Starts
    ##   with Sour, and clicks through 14 fields of Sour (Because we're assuming
    ##    that the "Any" fields are first with the Sour ones.
    for x in range(14):
        keyboard.type('1')
        for z in range(50):
            mouse.click(Button.left, 1);
            time.sleep(0.1)
        keyboard.type('d')
        time.sleep(0.5)
    ##Then, iterates through each berry after sour, assuming that all field sets
    ##   are of the same length- If not, you might just want to copy the above 
    ##    code for the sour fields 5 times, changing they "keyboard.type" number
    ##    to the number of the field's berry.
    for y in range(4):
        for w in range(7):
            keyboard.type('{0}'.format(y+1))
            for v in range(50):
                mouse.click(Button.left, 1)
                time.sleep(0.1)
            keyboard.type('d')
            time.sleep(0.5)
            
    ## Scour: This segment's still a little finicky, sometimes the third scour 
    ##   doesn't register as restarting their mission. You might want to check 
    ##    later.
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
    
    ##Clicks the "Go again" buttons.
    mouse.position = firstScourEndPos
    mouse.click(Button.left, 1)
    mouse.position = secScourEndPos
    mouse.click(Button.left, 1)
    mouse.position = thirdScourEndPos
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    
    ##Clicks through online players, in order to boost the Egg Timer up to level
    ##  10.
    mouse.position = playersPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = openAllPos
    mouse.click(Button.left, 1)
    time.sleep(2)
    mouse.position = clickPokemonPos
    
    ##Make sure the "Open All" settings are set to 50 players on a page, or this
    ##   bot will be wasting a lot of time and clicks, and it's more likely to
    ##    result in a page error. If you like it with 10 players on a page, you
    ## might want to adjust this such that 'X' goes to 25 and 'Y' goes to 75 instead.
    for x in range(5):
        for y in range(350):
            mouse.click(Button.left, 1)
            time.sleep(0.1)
        time.sleep(4)
        

if __name__ == '__main__':
    main()