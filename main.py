import time


i = ['inventory', ]


def death():
    print("---        ------         -        ---------     -       -")
    print("-    -     -             - -           -         -       -")
    print("-    -     ------       -----          -         ---------")
    print("-    -     -           -     -         -         -       -")
    print("---        ------     -       -        -         -       -")
    exit()

def explore():
  print("As you're walking through the Bijenkorf, you see something on the ground")
  print("When you take a closer look, you notice that the small jar is full of pills")
  print("Do you take a pill (type: take), leave them (type: leave) or just keep them (type: keep)")
  while True:
    option = input("> ")
    if option == "take":
      print("You swallow the pill and you don't feel a thing")
      print("suddenly you begin to hallucinate")
      print("the pill was cyanide")
      print("That one pill was enough to murder 10 hamsters")
      print("Your hallucinations are mostly about hamsters")
      print("You know this will be the end of your fear for them, aswell as it is the end of your life")
      death()
    elif option == "keep":
      print("You put the pills in your backpack")
      i.append('pills')
      print("you go back to the metro station where you started")
      start()
    elif option == "leave":
      print("You are too pussy to touch the pills")
      print("you leave them on the ground and go back to the metro station where it all started")
      start()
    elif option == "i":
      print(i)
    else:
      print(option + " is not an option")
      
      
def bijenkorf():
  print("You are standing in the Bijenkorf")
  print("You decide to run")
  print("You trip and fall, now you are walking cripple in the Bijenkorf")
  print("do you want to explore the bijenkorf(type: explore) or do you want to go back to the streets(type: back)")
  while True:
    option = input("> ")
    if option == "explore":
      explore()
    elif option == "back":
      start()
    elif option == "i":
      print(i)
    else:
      print(option + " is not an option")

def UithofTracks():
    print("You are walking over the tracks ")
    print("There is an exit door on your right hand side")
    print("Do you go through the door (type: door) or do you continue walking? (type: walk)")
    while True:
        option = input("> ")
        if option == "door":
              print("You open the door, the light on the other side is very bright.")
              print("Once your eyes are adjusted to the light, you find out that you've just entered the Bijenkorf")
              bijenkorf()
        elif option == "walk":
            print("You ignore the door on the right and decide to keep walking")
            print("There is a sound, vaguely in the background that keeps getting louder")
            print("Now there are lights coming around the corner, it is a train")
            print("You start running towards the door, but the train is (obviously) faster")
            print("When you look back you see one gigantic hamster steering the train")
            print("It is the last thing you'll ever see")
            death()
        elif option == "i":
            print(i)
        else:
            print(option + " is not an option")

def hide1():
    print("You chose to hide in the cupboard")
    print("You wait for the big creature to pass and you put the gun in your backpack, after this you have a choice")
    i.append('gun')
    print("Do you want to go back to the metro station (type: back) or do you want to go on the tracks (type: tracks)")
    while True:
        option = input("> ")
        if option == "back":
            start()
        elif option == "tracks":
            tracks1()
        elif option == "i":
            print(i)
        else:
            print(option + " is not an option")


def shoot1():
    print("You shot and killed the creature that was coming at you")
    print("Because of the sound of your shot tens of creatures are coming towards you from all sides")
    print("You're dropped in your biggest nightmare, tens of gigantic hamsters coming to rip you apart")
    print("You're still conscious while 3 meter long hamsters are starting to gnaw on your bones")
    print("Your blood is in your mouth, it is the last thing you'll ever taste")
    death()

def booth1():
    print("As you're walking towards the ticket booth, you see the shadow slowly moving towards you")
    print("The screeching gets louder while you arrive at the booth")
    print("You're searching the booth in hope of finding something useful on this EPIC adventure")
    print("In one of the drawers you find a gun and a article out of a newspaper")
    print("Do you want to shoot the creatures?(type: shoot) or hide? (type: hide)")
    while True:
        option = input("> ")
        if option == "shoot":
            shoot1()
        elif option == "hide":
            hide1()
        elif option == "i":
            print(i)
        else:
            print(option + " is not an option")

def shadows1():
    print("You follow the shadow")
    print("You see a big dark creature with red eyes, you take a moment to look at it")
    print("BIG MISTAKE, the creature spots you and comes running towards you")
    print("You sprint back but stumble over the tracks, the creature is standing over you")
    print("You turn around and look into its blood red eyes while it turns into your biggest nightmare:a hamster")
    print("You look at those enormous cheeks, while he uses his gigantic teeth to rip a part of your shoulder out ")
    print("He turns around and you watch his booty wiggle with joy while he walks away, you're slowly bleeding to death")
    death()

def followSound():
    print("You decide to walk towards the sound")
    print("*THERE IT IS AGAIN* you hear the screeching again and turn your head")
    print("Shadows, you see shadows on the wall on the other side of the tracks, next to you there is a ticket booth")
    print("What do you want to do, get in the ticket booth(type: booth) or follow the shadows(type: shadows)")
    while True:
        option = input("> ")
        if option == "booth":
            booth1()
        elif option == "shadows":
            shadows1()
        elif option == "i":
            print(i)
        else:
            print(option + " is not an option")



def tracks1():
    print("You Ignore the screeches and jump down onto the tracks")
    time.sleep(0)
    print("No trains, no sound at all")
    time.sleep(0)
    print("Do you want to walk towards the Hague Central(type: central) or towards the Uithof(type: uithof)")
    while True:
        option = input("> ")
        if option == "central":
            CentralTracks()
        elif option == "uithof":
            UithofTracks()
        elif option == "i":
            print(i)
        else:
            print(option + " is not an option")


def metro():
    print("You start descending down the stairs into the dark subway station")
    time.sleep(0)
    i.append('flashlight')
    print("suddenly you hear a faint screech")
    i.append('batteries')
    time.sleep(0)
    print("Do you want to start walking on the tracks towards a station(type: tracks) ,follow the sound(type: follow) or go back (type: back) ")
    while True:
        option = input("> ")
        if option == "tracks":
            tracks1()
        elif option == "follow":
            followSound()
        elif option == "back":
            start()
        elif option == "i":
            print(i)
        else:
            print(option + " is not an option")

def talk1():
    print("You start walking towards the man")
    print("he sees you coming towards him")
    print("he shouts: HEY, are you finally ready for my quest?")
    print("type: yes or no")
    while True:
        option = input("> ")
        if option == "yes":
            quest1()
        elif option == "no":
            print("You walk out of pathé back to the metro station")
            start()
        elif option == "i":
            print(i)
        else:
            print(option + " is not an option")

def room3():
    print("You enter the big room")
    print("Gosh darn it, there is no movie playing at the moment")
    print("You look around")
    print("OVER THERE, you faintly see an old man sitting in one of the cinema seats")
    print("do you want to strangle the man(type: strangle) or do you want to go talk to him(type: talk)")
    while True:
        option = input("> ")
        if option == "strangle":
            print("You walk up to the man, he doesn't seem to be alive")
            print("You get ready to strike at him")
            print("The man turns his head and you flinch")
            print("You decide to still go for the kill")
            print("The man sees you coming at him and stabs you with a knife he had been hiding")
            print("STUPID FOOL, YOU COULD'VE KILLED US BOTH, he shouts")
            death()
        elif option == "talk":
            talk1()
        elif option == "i":
            print(i)
        else:
            print(option + "is not an option")

def room8():
    print("You go all the way up to room 8")
    print("You pull the big doors of the room open and you see light")
    print("You continue walking and see that there is a movie playing")
    print("You look at the screen and you see that the movie playing is G-Force")
    print("Those cute little hamsters make great spies")
    print("Do you want to try and reach the beamer room(type: beamer) or search all the chairs(type: chairs)")
    while True:
        option = input("> ")
        if option == "beamer":
            print("You find a door and open it")
            print("blood, blood everywhere")
            print("You almost start to vomit, suddenly you see something on the ground")
            print("it is a key")
            print("what could this be used for?")
            print("you put the key in your inventory")
            i.append('Key-M')
            print("You slowly walk back to the metro station where you began")
            start()
        elif option == "chairs":
            print("You wasted a lot of time, you did not find a thing")
            print("you walk back to the metro station where you began")
            start()
        elif option == "i":
            print(i)
        else:
            print(option + " is not an option")


def pathe():
    print("You enter the big yellow room of pathé")
    print("You take a quick look around and notice that everything has worn down")
    print("Do you want to go to room 3(type: room 3) or do you want to go to room 8(type: room 8)")
    while True:
        option = input("> ")
        if option == "room 3":
            room3()
        elif option == "room 8":
            room8()
        elif option == "i":
            print(i)
        else:
            print(option + " is not an option")

def intersport():
    print("You walk up to Intersport")
    print("the doors are closed")
    print("do you want to smash the window(type: smash) or go to pathé(type: pathe)")
    while True:
        option = input("> ")
        if option == "smash":
            print("you sprint towards the window")
            print("you brace yourself whilst you are impacting with the glass")
            print("you hear a sound of breaking glass as you fall on the floor")
            print("a warm stream is flowing down your neck")
            print("you realise that some glass has cut you throath and you start to faint")
            death()
        elif option == "pathe":
            pathe()
        elif option == "i":
            print(i)
        else:
            print(option + " is not an option")

def cinema():
    print("You start climbing the stairs")
    print("You feel that you are weak, like you have been in a coma for the past years")
    print("As you stand at the top of the stairs you decide")
    print("Go to the Intersport(type: intersport) or enter Pathé(type: pathe)")
    while True:
        option = input("> ")
        if option == "intersport":
            intersport()
        elif option == "pathe":
            pathe()
        elif option == "i":
            print(i)
        else:
            print(option + " is not an option")

def decathlon():
  print("You go on the escelator and start going down, the decathlon is completely empty")
  print("You can get anything you want from the store")
  print("Do you want to go towards the toy's (type: toy's) or go to the swimattributes (type: swim)")
  while True:
    option = input("> ")
    
    

def start():
    print("what do you want to do, go up the stairs in the direction of the cinema(type: cinema), go back in to the metro station(type: metro)")
    print("start walking in the direction of The Hague Central station(type:central), go inside of the Decathlon(type: decathlon) or walk in the Direction of the Bijenkorf(type: bijenkorf)")
    while True:
        if 'flashlight' and 'batteries' in i:
          print("NOTE: You can combine the flashlight and the batteries to make the flashlight work!")
          print("Do you want to combine the Flashlight and the Batteries?")
          print("type: yes or no")
          option = input("> ")
          if option == "yes":
            i.append('working flashlight')
            i.remove('flashlight')
            i.remove('batteries')
            print("You now have a working flashlight!")
          elif option == "no":
            print("You chose to not merge the things")
        else:
          option = input("> ")
          if option == "cinema":
              cinema()
          elif option == "metro":
              metro()
          elif option == "central":
              central()
          elif option == "decathlon":
              decathlon()
          elif option == "bijenkorf":
              bijenkorf()
          elif option == "i":
              print(i)
          else:
              print(option + " is not an option")


print("Help guide: throughout the entire story you can type i to open your inventory, Also do not use capital letters!!")
print("ENJOY!")
print("*Here you are no soul to be seen...*")
time.sleep(0)
print("*All alone at Spuimarkt in the Hague*")
time.sleep(0)
print("You look around and see you are standing in front of the tram station next to the cinema and the Mac Donalds")
time.sleep(0)
print("*What happened here? It is pitch black outside but there are some lights burning*")
time.sleep(0)
print(".")
start()
