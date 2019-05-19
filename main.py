import time
import random

i = ['inventory', ]
milk = [0]
words = ["peach", "wario", "bowser"]
secret_word = random.choice(words)


def death():
    print("---        ------         -        ---------     -       -")
    print("-    -     -             - -           -         -       -")
    print("-    -     ------       -----          -         ---------")
    print("-    -     -           -     -         -         -       -")
    print("---        ------     -       -        -         -       -")
    exit()


def explore():
    print("As you're walking through the Bijenkorf, you see something on the ground")
    time.sleep(3)
    print("When you take a closer look, you notice that the small jar is full of pills")
    time.sleep(3)
    print("Do you take a pill (type: take), leave them (type: leave) or just keep them (type: keep)")
    while True:
        option = input("> ").lower().strip()
        if option == "take":
            print("You swallow the pill and you don't feel a thing")
            time.sleep(3)
            print("suddenly you begin to hallucinate")
            time.sleep(3)
            print("the pill was cyanide")
            time.sleep(3)
            print("That one pill was enough to murder 10 hamsters")
            time.sleep(3)
            print("Your hallucinations are mostly about hamsters")
            time.sleep(3)
            print("You know this will be the end of your fear for them, aswell as it is the end of your life")
            death()
        elif option == "keep":
            print("You put the pills in your backpack")
            time.sleep(3)
            i.append('pills')
            print("you go back to the metro station where you started")
            start()
        elif option == "leave":
            print("You are too pussy to touch the pills")
            time.sleep(3)
            print("you leave them on the ground and go back to the metro station where it all started")
            start()
        elif option == "i":
            print(i)

        else:
            print(option + " is not an option")


def bijenkorf():
    print("You are standing in the Bijenkorf")
    time.sleep(3)
    print("You decide to run")
    time.sleep(3)
    print("You trip and fall, now you are walking cripple in the Bijenkorf")
    time.sleep(3)
    print("do you want to explore the bijenkorf(type: explore) or do you want to go back to the streets(type: back)")
    while True:
        option = input("> ").lower().strip()
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
    time.sleep(3)
    print("There is an exit door on your right hand side")
    time.sleep(3)
    print("Do you go through the door (type: door) or do you continue walking? (type: walk)")
    while True:
        option = input("> ").lower().strip()
        if option == "door":
            print("You open the door, the light on the other side is very bright.")
            time.sleep(3)
            print("Once your eyes are adjusted to the light, you find out that you've just entered the Bijenkorf")
            bijenkorf()
        elif option == "walk":
            print("You ignore the door on the right and decide to keep walking")
            time.sleep(3)
            print("There is a sound, vaguely in the background that keeps getting louder")
            time.sleep(3)
            print("Now there are lights coming around the corner, it is a train")
            time.sleep(3)
            print("You start running towards the door, but the train is (obviously) faster")
            time.sleep(3)
            print("When you look back you see one gigantic hamster steering the train")
            time.sleep(3)
            print("It is the last thing you'll ever see")
            death()
        elif option == "i":
            print(i)

        else:
            print(option + " is not an option")


def hide1():
    print("You chose to hide in the cupboard")
    time.sleep(3)
    print("You wait for the big creature to pass and you put the gun in your backpack, after this you have a choice")
    i.append('gun')
    time.sleep(3)
    print("Do you want to go back to the metro station (type: back) or do you want to go on the tracks (type: tracks)")
    while True:
        option = input("> ").lower().strip()
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
    time.sleep(3)
    print("The screeching gets louder while you arrive at the booth")
    time.sleep(3)
    print("You're searching the booth in hope of finding something useful on this EPIC adventure")
    time.sleep(3)
    print("In one of the drawers you find a gun and a article out of a newspaper")
    i.append('newspaper')
    time.sleep(3)
    print("there is also a key, you put the key and newspaper in your backpack")
    i.append('Key-N')
    time.sleep(3)
    print("Do you want to shoot the creatures?(type: shoot) or hide? (type: hide)")
    while True:
        option = input("> ").lower().strip()
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
    time.sleep(3)
    print("You see a big dark creature with red eyes, you take a moment to look at it")
    time.sleep(3)
    print("BIG MISTAKE, the creature spots you and comes running towards you")
    time.sleep(3)
    print("You sprint back but stumble over the tracks, the creature is standing over you")
    time.sleep(3)
    print("You turn around and look into its blood red eyes while it turns into your biggest nightmare:a hamster")
    time.sleep(3)
    print("You look at those enormous cheeks, while he uses his gigantic teeth to rip a part of your shoulder out ")
    time.sleep(3)
    print(
        "He turns around and you watch his booty wiggle with joy while he walks away, you're slowly bleeding to death")
    death()


def followSound():
    print("You decide to walk towards the sound")
    time.sleep(3)
    print("*THERE IT IS AGAIN* you hear the screeching again and turn your head")
    time.sleep(3)
    print("Shadows, you see shadows on the wall on the other side of the tracks, next to you there is a ticket booth")
    time.sleep(3)
    print("What do you want to do, get in the ticket booth(type: booth) or follow the shadows(type: shadows)")
    while True:
        option = input("> ").lower().strip()
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
    time.sleep(3)
    print("No trains, no sound at all")
    time.sleep(3)
    print("Do you want to walk towards the Hague Central(type: central) or towards the Uithof(type: uithof)")
    while True:
        option = input("> ").lower().strip()
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
    time.sleep(3)
    print("suddenly you hear a faint screech")
    time.sleep(3)
    print(
        "Do you want to start walking on the tracks towards a station(type: tracks) ,follow the sound(type: follow) or go back (type: back) ")
    while True:
        option = input("> ").lower().strip()
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


def quest1():
    print("hello there...")
    time.sleep(3)
    print("I'm glad you decided to take on my quest")
    time.sleep(3)
    print("Come on follow me")
    time.sleep(3)
    print("say start to start")
    run = input("> ").lower().strip()
    if run == "start":
        print("You walk up to an acient looking door")
        print("man: I can't open this door, legend says only the true master can open it")
        print("you: well I don't want to brag but people have called me a master before")
        print("you walk up to the door")
        print("suddenly the door starts talking")
        print("door: Answer my riddle correctly otherwise you die")
        print("door: There is a house. One enters it blind and comes out seeing. What is it?")
        while True:
            option = input("> ").lower().strip()
            if "school" in option:
                questy()
            else:
                death()


def questy():
    print("door: WELL DAYUUM!!!")
    time.sleep(3)
    print("door: You must be the true master!")
    time.sleep(3)
    print("door: Please continue my lord")
    time.sleep(3)
    print("man: how... how... how did you know that")
    time.sleep(3)
    print("you: Well there is a reason they call me the true master")
    time.sleep(3)
    print("You and the man keep walking")
    time.sleep(3)
    print("man: THERE, there it is")
    time.sleep(3)
    print("man: the goodie serum")
    time.sleep(3)
    print("you see a needle laying on a desk")
    time.sleep(3)
    print("next to the needle there is a railgun frame")
    time.sleep(3)
    print("you put the railgun frame in your backpack")
    i.append('railgun frame')
    time.sleep(3)
    print("what do you want to do?")
    print("take the goodie serum yourself(type: take) or put it in your backpack?(type: keep)")
    while True:
        option = input("> ").lower().strip()
        if option == "take":
            print("you take the goodie serum")
            time.sleep(3)
            print("immediately you start hallucinating")
            time.sleep(3)
            print("you see big fluffy hamsters dancing with joy")
            time.sleep(3)
            print("suddenly you hear a hamster talking")
            time.sleep(3)
            print("hamster: HAHA you stupid, you just overdosed on heroin")
            time.sleep(3)
            print("everything starts to become blacker and blacker......")
            death()
        elif option == "keep":
            print("you put the serum in your backpack")
            i.append('goodie serum')
            time.sleep(3)
            print("you go back to the big yellow hall")
            pathe()


def talk1():
    print("You start walking towards the man")
    time.sleep(3)
    print("he sees you coming towards him")
    time.sleep(3)
    print("he shouts: HEY, are you finally ready for my quest?")
    time.sleep(3)
    print("type: yes or no")
    while True:
        option = input("> ").lower().strip()
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
    time.sleep(3)
    print("Gosh darn it, there is no movie playing at the moment")
    time.sleep(3)
    print("You look around")
    time.sleep(3)
    print("OVER THERE, you faintly see an old man sitting in one of the cinema seats")
    time.sleep(3)
    print("do you want to strangle the man(type: strangle) or do you want to go talk to him(type: talk)")
    while True:
        option = input("> ").lower().strip()
        if option == "strangle":
            print("You walk up to the man, he doesn't seem to be alive")
            time.sleep(3)
            print("You get ready to strike at him")
            time.sleep(3)
            print("The man turns his head and you flinch")
            time.sleep(3)
            print("You decide to still go for the kill")
            time.sleep(3)
            print("The man sees you coming at him and stabs you with a knife he had been hiding")
            time.sleep(3)
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
    time.sleep(3)
    print("You pull the big doors of the room open and you see light")
    time.sleep(3)
    print("You continue walking and see that there is a movie playing")
    time.sleep(3)
    print("You look at the screen and you see that the movie playing is G-Force")
    time.sleep(3)
    print("Those cute little hamsters make great spies")
    time.sleep(3)
    print("Do you want to try and reach the beamer room(type: beamer) or search all the chairs(type: chairs)")
    while True:
        option = input("> ").lower().strip()
        if option == "beamer":
            print("You find a door and open it")
            time.sleep(3)
            print("blood, blood everywhere")
            time.sleep(3)
            print("You almost start to vomit, suddenly you see something on the ground")
            time.sleep(3)
            print("it is a key")
            time.sleep(3)
            print("what could this be used for?")
            time.sleep(3)
            print("you put the key in your inventory")
            i.append('Key-M')
            time.sleep(3)
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
    time.sleep(3)
    print("You take a quick look around and notice that everything has worn down")
    time.sleep(3)
    print("Do you want to go to room 3(type: room 3) or do you want to go to room 8(type: room 8)")
    while True:
        option = input("> ").lower().strip()
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
    time.sleep(3)
    print("the doors are closed")
    time.sleep(3)
    print("do you want to smash the window(type: smash) or go to pathé(type: pathe)")
    while True:
        option = input("> ").lower().strip()
        if option == "smash":
            print("you sprint towards the window")
            time.sleep(3)
            print("you brace yourself whilst you are impacting with the glass")
            time.sleep(3)
            print("you hear a sound of breaking glass as you fall on the floor")
            time.sleep(3)
            print("a warm stream is flowing down your neck")
            time.sleep(3)
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
    time.sleep(3)
    print("You feel that you are weak, like you have been in a coma for the past years")
    time.sleep(3)
    print("As you stand at the top of the stairs you decide")
    time.sleep(3)
    print("Go to the Intersport(type: intersport) or enter Pathé(type: pathe)")
    while True:
        option = input("> ").lower().strip()
        if option == "intersport":
            intersport()
        elif option == "pathe":
            pathe()
        elif option == "i":
            print(i)

        else:
            print(option + " is not an option")


def swimclothing():
    print("you walk to the clothing section")
    time.sleep(3)
    print("you think to yourself: why wouldn't I walk around in some swimwear?")
    time.sleep(3)
    print("You look at the racks")
    time.sleep(3)
    print("you are facing a hard decission")
    time.sleep(3)
    print("do you want to wear a speedo(type: speedo) or a bikini(type: bikini)")
    while True:
        option = input("> ").lower().strip()
        if option == "speedo":
            print("you take a speedo of the mannequin")
            time.sleep(3)
            print("you try the speedo on")
            time.sleep(3)
            print("wait what is that?!")
            i.append('speedo')
            time.sleep(3)
            print("you find a key in the speedo")
            i.append('key-n')
            time.sleep(3)
            print("You walk back to the metro station where it all started")
            start()
        elif option == "bikini":
            print("you put on a bikini")
            i.append('bikini')
            time.sleep(3)
            print("You look in the mirror")
            time.sleep(3)
            print("you look really cute")
            time.sleep(3)
            print("with a huge smile on your face you walk back to the start in your bikini")
            start()
        elif option == "i":
            print(i)

        else:
            print(option + " is not an option")


def swim():
    print("You walk up to the swimattributes")
    time.sleep(3)
    print("Do you want to go to to the water toy's(type: watertoy)or go to the swimclothing(type: swimclothing)")
    while True:
        option = input("> ").lower().strip()
        if option == "watertoy":
            print("You go to the watertoy's and when you arrive you see something on the ground")
            time.sleep(3)
            print("It's a gun, a watergun. You put the watergun in your inventory")
            i.append('watergun')
            decathlon()
        elif option == "swimclothing":
            swimclothing()
        elif option == "i":
            print(i)

        else:
            print(option + " is not an option")


def box():
    print("You chose to hide behind a boxing sack")
    time.sleep(3)
    print("You hear footsteps passing by")
    time.sleep(3)
    print("you are too scared to take a peak")
    time.sleep(3)
    print("you wait about 5 minutes until you are sure there is no one around")
    time.sleep(3)
    print("you come out of your hiding spot and walk back to the toy's")
    time.sleep(3)
    print("there's nothing here")
    time.sleep(3)
    print("do you choose to walk back to the starting point of your adventure(type: start)")
    print("or do you want to go the swimming atributes(type: swim)")
    while True:
        option = input("> ").lower().strip()
        if option == "start":
            start()
        elif option == "swim":
            swim()
        elif option == "i":
            print(i)

        else:
            print(option + " is not an option")


def toy():
    print("You walk up to the toy's")
    time.sleep(3)
    print("suddenly you hear footsteps")
    time.sleep(3)
    print("you start to sprint towards the gym equipment")
    time.sleep(3)
    print("the footsteps are becomming louder and louder")
    time.sleep(3)
    print("Choose fast hide behind a boxing sack(type: box) or between the mannequins(type: mannequin)")
    while True:
        option = input("> ").lower().strip()
        if option == "box":
            box()
        elif option == "mannequin":
            print("You sprint towards the mannequins")
            time.sleep(3)
            print("the footsteps are coming towards you faster and faster")
            time.sleep(3)
            print("you stay as queiet and steady as possible")
            time.sleep(3)
            print("you see a hamster walking by")
            time.sleep(3)
            print("suddenly his cute little nose lifts up and he turns his head")
            time.sleep(3)
            print("you lock eyes")
            time.sleep(3)
            print("he starts charging towards you")
            time.sleep(3)
            print("he bites your leg and rips it off with one movement")
            time.sleep(3)
            print("the last thing you see is the cute pink nose of the hamster coming towards you")
            death()
        elif option == "i":
            print(i)

        else:
            print(option + " is not an option")


def decathlon():
    print("You go on the escelator and start going down, the decathlon is completely empty")
    time.sleep(3)
    print("You can get anything you want from the store")
    time.sleep(3)
    print("Do you want to go towards the toy's (type: toy) or go to the swimattributes (type: swim)")
    while True:
        option = input("> ").lower().strip()
        if option == "toy":
            toy()
        elif option == "swim":
            swim()
        elif option == "i":
            print(i)

        else:
            print(option + "is not an option")


def counter():
    print("You jump over the counter and find lettuce")
    time.sleep(3)
    print("Wait... there is also a key")
    time.sleep(3)
    print("you put the key in your backpack")
    i.append('Key-O')
    time.sleep(3)
    print("Do you eat (type: eat) or keep the lettuce (type: keep)")
    while True:
        option = input("> ").lower().strip()
        if option == "eat":
            print("You eat the lettuce and go back over the counter")
            mcdonalds()
        elif option == "keep":
            print("You keep the lettuce and go back over the counter")
            i.append('lettuce')
            mcdonalds()
        elif option == "i":
            print(i)

        else:
            print(option + "is not an option")


def light():
    print("You're walking towards the light")
    time.sleep(3)
    print("When your eyes are adjusted to the light you see something on the floor")
    time.sleep(3)
    print("You first think they are bullets, but as you're coming closer you realise that they are batteries")
    time.sleep(3)
    print("Do you want to pick up the batteries (type: pick up) or leave them (type: leave) ")

    while True:
        option = input("> ").lower().strip()
        if option == "pick up":
            print("You decided to take the batteries with you")
            i.append('batteries')
            mcdonalds()
        if option == "leave":
            print("You decided to leave the batteries where they are")
            mcdonalds()
        else:
            print(option + "is not an option")


def mcdonalds():
    print("You go inside the mcdonalds")
    time.sleep(3)
    print("You see the counter and a door with bright light on the other side, Also the Milkshake machine is working!!")
    time.sleep(3)
    print("Do you go to the light (type: light), jump over the counter (type: counter), go back (type: back) or drink a milkshake You can drink as many as you want(type: milkshake)")
    while True:
        option = input("> ").lower().strip()
        if option == "light":
            light()
        elif option == "counter":
            counter()
        elif option == "back":
            continuecentral()
        elif option == "milkshake":
            milk[0] += 1
            if milk[0] > 3:
                print("Your milkshake addiction gave you diabetes")
                time.sleep(3)
                print("fun easter egg you found huh?")
                time.sleep(3)
                print("stupid boi")
                time.sleep(3)
                print("you ded")
                death()
            elif milk[0] > 2:
                print("Maybe I should really stop, I'm getting dizzy")
                mcdonalds()
            print("you drink a milkshake")
            time.sleep(3)
            print("wow that sugar really gave me a rush")
            time.sleep(3)
            print("maybe I should take another one")
            time.sleep(3)
            print("you go back to the main hall in the macdonalds")
            mcdonalds()
        elif option == "milk":
            print(milk)
            mcdonalds()
        elif option == "i":
            print(i)

        else:
            print(option + "is not an option")


def track5():
    print("You arrive at track 5")
    print(
        "There is a train standing still, do you enter (type: enter) or talk to the conductor who is standing at the front (type: talk) or do you go back (type: back)")
    while True:
        option = input("> ").lower().strip()
        if option == "enter":
            print("You enter the train, when you look around you see a weird boy standing next to you")
            time.sleep(3)
            print("He seems very exited about the train")
            time.sleep(3)
            print("When you go and talk to him you realise he is autistic")
            time.sleep(3)
            print("You can see that he has a key, you decide to take it from him and run")
            time.sleep(3)
            print("Weird boy: autistic screeching")
            time.sleep(3)
            print("he did not like that, but you have the key")
            i.append('key-N')
            centralstation()
        elif option == "talk":
            print("As you are walking towards the conductor, he starts making weird movements.")
            time.sleep(3)
            print(
                "You sprint to him to help him, but when you get there all you see is a 3 meter tall hamster trowing him away")
            time.sleep(3)
            print("The hamster came out of nowwhere and is now coming after you")
            time.sleep(3)
            print("You look at the big bloody teeth while you try to get in the train")
            time.sleep(3)
            print("You are to slow")
            death()
        elif option == "back":
            centralstation()
        elif option == "i":
            print(i)

        else:
            print(option + "is not an option")

def followT3():
    print("You follow the hamster quietly")
    time.sleep(3)
    print("The hamster doesn't seem to notice you")
    time.sleep(3)
    print("suddenly the hamster stops")
    time.sleep(3)
    print("you see another figure")
    time.sleep(3)
    print("it looks like a man, the man looks a little bit like waluigi")
    time.sleep(3)
    print("Waluigi: My dear hamster! I have heard of someone who is trying to stop our plans of taking over the world")
    time.sleep(3)
    print("Waluigi: Gather all your soldiers at the malieveld and make sure that that little peasant gets crushed")
    time.sleep(3)
    print("Hamster: SIR YES SIR")
    time.sleep(3)
    print("Waluigi: All our hard work from the past 5 years can't be for nothing but I won't worry")
    time.sleep(3)
    print("Waluigi: I heard he was just a kid")
    time.sleep(3)
    print("You are terrified of the man standing there")
    time.sleep(3)
    print("Do you want to confront the man(type: confront) or sneak back towards the main entrance(type: back)")
    while True:
        option = input("> ").lower().strip()
        if option == "confront":
            print("you jump out of the train")
            time.sleep(3)
            print("You: I am not just a kid")
            time.sleep(3)
            print("You: I am the kid who is going to stop you from taking over the world")
            time.sleep(3)
            print("Waluigi has got no expression on his face")
            time.sleep(3)
            print("He puts out his hand and suddenly you are hit by a laser beam of hamster shit")
            time.sleep(3)
            print("The last thing you ever smell is the smell of hamster shit")
            death()
        elif option == "back":
            print("shocked and confused you walk back to the main entrance")
            centralstation()
        elif option == "i":
            print(i)
        else:
            print(option + " is not an option")


def hide():
    print("You are hiding in the train when a hamster starts to walk past")
    time.sleep(3)
    print("You are curious of these giant creatures")
    time.sleep(3)
    print("Do you decide to follow the hamster(type: follow) or to sprint back the the main entrance?(type: back)")
    while True:
        option = input("> ").lower().strip()
        if option == "follow":
            followT3()
        elif option == "back":
            print("you sprint back to the main entrance")
            centralstation()
        elif option == "i":
            print(i)
        else:
            print(option + " is not an option")

def track3():
    print("You arrive at the track")
    time.sleep(3)
    print("You can go either into the train (type: in) or go under the train (type: under)")
    while True:
        option = input("> ").lower().strip()
        if option == "in":
            print("You go into the train and stay there to hide")
            hide()
        elif option == "under":
            print("You cralw under the train and you find magnets")
            print("By the time you come out the hamsters are gone")
            print("You go back to the station, with magnets")
            i.append('magnets')
            centralstation()
        elif option == "i":
            print(i)

        else:
            print(option + "is not an option")


def hidecentral():
    print("You are hiding from the hamsters")
    time.sleep(3)
    print("You decide to follow them to see where they're going")
    time.sleep(3)
    print("After 2min of succesfull following they spot you")
    time.sleep(3)
    print("Hiding is for pussies")
    time.sleep(3)
    print("This is your punishment")
    death()


def centralstation():
    print("You arrive at central station of the Hague")
    time.sleep(3)
    print("It is mostly ruins, there are just a few tracks not covered in stones")
    time.sleep(3)
    print("As soon as you arrive, right behind you the gigant hamsters start to come in through the same entrence")
    time.sleep(3)
    print("They must have followed you")
    time.sleep(3)
    print("Do you hide (type: hide), flee to track 3 or 5 (type: track 3/5) or do you go back (type: back) ")
    while True:
        option = input("> ").lower().strip()
        if option == "hide":
            hidecentral()
        elif option == "track 3":
            track3()
        elif option == "track 5":
            track5()
        elif option == "back":
            continuecentral()
        elif option == "i":
            print(i)

        else:
            print(option + "is not an option")


def quest2W():
    print("You wait and wait")
    time.sleep(3)
    print("nothing happens")
    time.sleep(3)
    print("Just until you want to shout another password")
    time.sleep(3)
    print("the wall suddenly crumbles")
    time.sleep(3)
    print("behind the wall there is light, blue light")
    time.sleep(3)
    print("you start to walk up to the light")
    time.sleep(3)
    print("you notice some things laying on a table")
    time.sleep(3)
    i.append('key-E')
    print("you see a key and plasma")
    i.append('plasma')
    time.sleep(3)
    print("you take them both and walk back to the entrance")
    primark()


def quest2():
    print("girl: Hell yeah, lets do this")
    print("NOTE: This quest is easier with a working flashlight!")
    if 'working flashlight' in i:
        print("it seems you have got the working flashlight")
        print("Lucky you")
    else:
        print("it seems you don't have the working flashlight yet")
        print("do you still want to continue? (yes/no)")
        option = input("> ").lower().strip()
        if option == "yes":
            print("your choice")
        elif option == "no":
            print("You decide to leave the quest")
            primark()
    print("girl: I AM SOOOOOO EXCITED FOR THIS")
    time.sleep(3)
    print("you start follwing here to a dark room")
    time.sleep(3)
    print("girl: I could never guess the passcode on the wall")
    time.sleep(3)
    print("girl: but maybe you can!")
    if 'working flashlight' in i:
        print("You use your flashlight to shine on the wall")
        time.sleep(3)
        print("you see that you have to make a 7 letter word")
        time.sleep(3)
        print("because of your flashlight there is only 1 letter missing")
        time.sleep(3)
        print("the wall says: Wal.igi")
        time.sleep(3)
        print("What is the secret code?")
        option = input("> ").lower().strip()
        if option == "waluigi":
            quest2W()
        else:
            print("you say the password out loud")
            time.sleep(3)
            print("suddenly there is a fat guy in a yellow and purple suit standing in front of you")
            time.sleep(3)
            print("you notice that it is wario riding a hamster")
            time.sleep(3)
            print("the last thing you will ever hear is")
            time.sleep(3)
            print("WAAARIOOOOO")
            death()
    else:
        print("because you have got no flashlight you can only see some letters")
        time.sleep(3)
        print("you see that the passcode is supposed to be 7 letters long")
        time.sleep(3)
        print("the wall says: ..lu.gi")
        time.sleep(3)
        print("What is the secret code?")
        option = input("> ").lower().strip()
        if option == "waluigi":
            quest2W()
        else:
            print("you say the password out loud")
            time.sleep(3)
            print("suddenly there is a fat guy in a yellow and purple suit standing in front of you")
            time.sleep(3)
            print("you notice that it is wario riding a hamster")
            time.sleep(3)
            print("the last thing you will ever hear is")
            time.sleep(3)
            print("WAAARIOOOOO")
            death()


def continuecentral():
    print("You keep going towards central station")
    time.sleep(3)
    print("On your right you see a mcdonalds")
    time.sleep(3)
    print(
        "Do you go in the mcdonalds (type: mcdonalds), go inside central station (type: central) or go back (type: back)")
    while True:
        option = input("> ").lower().strip()
        while True:
            if option == "mcdonalds":
                mcdonalds()
            elif option == "central":
                centralstation()
            elif option == "back":
                CentralTracks()
            elif option == "i":
                print(i)

            else:
                print(option + "is not an option")


def get_guess():
    dashes = "-" * len(secret_word)
    guesses_left = 10
    while guesses_left > -1 and not dashes == secret_word:
        print(dashes)
        print(str(guesses_left))
        guess = input("Guess:")
        if len(guess) != 1:
            print("Your guess must have exactly one character!")
        elif guess in secret_word:
            print("That letter is in the secret word!")
            dashes = update_dashes(secret_word, dashes, guess)
        else:
            print("That letter is not in the secret word!")
            guesses_left -= 1

    if guesses_left < 0:
        print("You lose. The word was: " + str(secret_word))
    else:
        print("waluigi: WAIT HOW DID YOU KNOW THAT IT WAS " + str(secret_word))
        time.sleep(3)
        print("waluigi: It doesn't matter because you won't be able to answer one simple question")
        time.sleep(3)
        print("waluigi: It is greater than God and more evil than the devil. The poor have it, the rich need it and if you eat it you’ll die. What is it?")
        while True:
            option = input("> ").lower().strip()
            if option == "nothing":
                end()
            else:
                print("you answerd wrong")
                time.sleep(3)
                print("waluigi laughs with evil while hamsters devour you")
                time.sleep(3)
                print("don't make such poor choices in life")
                death()


def end():
    print("waluigi: WAIT WAIT")
    time.sleep(3)
    print("waluigi: This is not possible!")
    time.sleep(3)
    print("waluigi jumps of the hamster")
    time.sleep(3)
    print("this is your shot")
    time.sleep(3)
    print("you run towards the jumping waluigi and strike him in the troath")
    time.sleep(3)
    print("waluigi falls to the ground")
    time.sleep(3)
    print("you raise your foot and stomp on waluigi until he stops breathing")
    time.sleep(3)
    print("the hamsters look at you and all of the sudden they start shouting")
    time.sleep(3)
    print("HEIL WALUIGI SLAYER!!!")
    time.sleep(3)
    print("life is good")
    time.sleep(3)
    print("THE END")
    exit()



def update_dashes(secret, cur_dash, rec_guess):
    result = ""

    for i in range(len(secret)):
        if secret[i] == rec_guess:
            result = result + rec_guess

        else:
            result = result + cur_dash[i]

    return result


def endgame():
    print("weird man: You are correct")
    time.sleep(3)
    print("weird man: I think it is time you face the hamsters and their master")
    time.sleep(3)
    print("you walk onto the malieveld and immediately the hamsters start comming at you")
    time.sleep(3)
    print("you are scared shitless but you came this far you will not turn back now")
    time.sleep(3)
    print("just before the hamsters start attacking you hear someone shout")
    time.sleep(3)
    print("STOP")
    time.sleep(3)
    print("you look up and you see waluigi standing on top of 3 hamsters")
    time.sleep(3)
    print("the hamsters grab your arms and legs and take you to him")
    time.sleep(3)
    print("waluigi: Well, well, well")
    time.sleep(3)
    print("waluigi: who do we have here")
    name = input("what is your name? ")
    print("waluigi: well hello " + name)
    time.sleep(3)
    print("waluigi: How did you get past my passcode man")
    time.sleep(3)
    print("waluigi: I guess you have been roaming around for a long time then")
    time.sleep(3)
    print("waluigi: I'll make you a deal")
    time.sleep(3)
    print("waluigi: You walk away right now and I will leave you alone for the rest of your life")
    time.sleep(3)
    print("waluigi: or we play a little game and if you win....")
    time.sleep(3)
    print("waluigi: I'll probably still kill you, but you won't win")
    time.sleep(3)
    print("waluigi: so what is it? (leave / play)")
    option = input("> ").lower().strip()
    if option == "leave":
        print("you chose to leave")
        time.sleep(3)
        print("years move by and you have never seen waluigi again")
        time.sleep(3)
        print("still everyone is either dead or terrified of waluigi and his hamster army")
        time.sleep(3)
        print("when you are 43 you die from loneliness")
        time.sleep(3)
        print("THE END..............")
        exit()
    elif option == "play":
        print("waluigi: Well well, guess someone got them big balls")
        time.sleep(3)
        print("waluigi: I will choose the first game")
        time.sleep(3)
        print("waluigi: I decide that we will play HANGMAN!!")
        time.sleep(3)
        print("you will never guess my word")
        get_guess()






def second():
    print("you take the escalator up to the second floor")
    time.sleep(3)
    print("you are now in the mens section")
    time.sleep(3)
    print("You walk around")
    time.sleep(3)
    print("out of the corner of your eye you see someone")
    time.sleep(3)
    print("you jumped of fear")
    time.sleep(3)
    print("you gather all your courage and walk up to the girl")
    time.sleep(3)
    print("the girl is folding clothes while you walk up to her")
    time.sleep(3)
    print("you walk up to the girl and she turns around and starts talking")
    time.sleep(3)
    print("Hey you, I think I've seen you before")
    time.sleep(3)
    print("are you ready for my quest now?")
    while True:
        option = input("> ").lower().strip()
        if option == "yes":
            quest2()
        elif option == "no":
            print("too bad")
            print("come back when you are ready")
            primark()
        elif option == "i":
            print(i)
        else:
            print(option + " is not an option")


def primark():
    print("Walking up to the primark you notice that all the lights are on")
    time.sleep(3)
    print("time to go on a shopping spree!!")
    time.sleep(3)
    print("do you want to stay on the first floor(type: first) move up to the second floor(type: second) or go back(type: back")
    while True:
        option = input("> ").lower().strip()
        if option == "first":
            print("you walk around on the first floor")
            time.sleep(3)
            print("suddenly you see a flashlight")
            time.sleep(3)
            print("the flashlight has got no batteries in it")
            time.sleep(3)
            print("maybe you can find batteries and make it work")
            time.sleep(3)
            print("you put the flashlight in you backpack")
            i.append('flashlight')
            time.sleep(3)
            print("what do you want to do, go to the second floor(type: second) or go outside?(type: outside)")
        elif option == "outside":
            CentralTracks()
        elif option == "second":
            second()
        elif option == "back":
            CentralTracks()
        elif option == "i":
            print(i)

        else:
            print(option + " is not an option")


def malieveld():
    print("You are walking towards malieveld")
    time.sleep(3)
    if '####RAILGUN####' in i:
        print("Suddenly your railgun starts making a weird sound")
        time.sleep(3)
        print("you pull your railgun out of your backpack")
        time.sleep(3)
        print("as you look up you see a hord of hamsters running towards you")
        time.sleep(3)
        print("you see one hamster with a mustache and a cool haircut")
        time.sleep(3)
        print("that must be their leader")
        time.sleep(3)
        print("you power on your railgun and start firing")
        time.sleep(3)
        print("the hamsters don't stand a chance")
        time.sleep(3)
        print("you kill hundreds every second")
        time.sleep(3)
        print("eventually there are no more hamsters left")
        time.sleep(3)
        print("you saved the world")
        time.sleep(3)
        print("you and your railgun make the perfect team")
        time.sleep(3)
        print("we thank you for your service")
        time.sleep(3)
        print("THE END")
        exit()
    print("As you're getting closer, you see a guy sitting against a tree")
    time.sleep(3)
    print("You are going to talk to him")
    time.sleep(3)
    print("When you're just 5 meters separated he starts talking to you")
    time.sleep(3)
    print("Weird man: So, do you finally know the secret code, or I can't let you pass")
    time.sleep(3)
    print("You can make the secret code with the Keys, the code is 5 letters and it is the name of the one and only Mathemathics master")
    time.sleep(3)
    print("So do you know the secret code. Yes or no?")
    while True:
        option = input("> ").lower().strip()
        if option == "yes":
            print("Weird man: So, what is it then? (give the secret code)")
            while True:
                option = input("> ").lower().strip()
                if option == "menno":
                    endgame()
                else:
                    print("Weird man: YOU FOOL, this is your end")
                    death()
        elif option == "no":
            print("Weird man: Come back when you have the code")
            CentralTracks()
        elif option == "i":
            print(i)
        else:
            print(option + "is not an option")


def CentralTracks():
    print("You are walking towards central station")
    time.sleep(3)
    print("There is more than one way.")
    time.sleep(2)
    print(
        "Do you want to continue going to central station (type: central), go to the primark (type: primark), go to malieveld (type: malieveld) or go back (type: back)")
    while True:
        option = input("> ").lower().strip()
        if option == "central":
            continuecentral()
        elif option == "primark":
            primark()
        elif option == "malieveld":
            malieveld()
        elif option == "back":
            start()
        elif option == "i":
            print(i)
        else:
            print(option + "is not an option")


def start():
    if 'flashlight' in i and 'batteries' in i:
        print("NOTE: You can combine the flashlight and the batteries to make the flashlight work!")
        print("Do you want to combine the Flashlight and the Batteries?")
        print("type: yes or no")
        option = input("> ").lower().strip()
        if option == "yes":
            i.append('working flashlight')
            i.remove('flashlight')
            i.remove('batteries')
            print("You now have a working flashlight!")
        elif option == "no":
            print("You chose to not merge the things")
        else:
            print(option + " is not an option")
    if 'magnets' in i and 'plasma' in i and 'railgun frame' in i and 'batteries' in i:
        print(">>>>>>>>>>>>>>>>>>>>>IMPORTANT<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("YOU CAN NOW CREATE A RAILGUN")
        print("do you want to do this?")
        print("type: yes or no")
        option = input("> ").lower().strip()
        if option == "yes":
            i.append('####RAILGUN####')
            i.remove('magnets')
            i.remove('batteries')
            i.remove('plasma')
            i.remove('railgun frame')
            print("You now have a RAILGUN!!!!!")
        elif option == "no":
            print("You chose to not merge the things")
        else:
            print(option + " is not an option")
    print(
        "what do you want to do, go up the stairs in the direction of the cinema(type: cinema), go back in to the metro station(type: metro)")
    print(
        "start walking in the direction of The Hague Central station(type:central), go inside of the Decathlon(type: decathlon) or walk in the Direction of the Bijenkorf(type: bijenkorf)")

    while True:
        option = input("> ").lower().strip()
        if option == "cinema":
            cinema()
        elif option == "metro":
            metro()
        elif option == "central":
            CentralTracks()
        elif option == "decathlon":
            decathlon()
        elif option == "bijenkorf":
            bijenkorf()
        elif option == "i":
            print(i)
        else:
            print(option + " is not an option")


print(
    "Help guide: throughout the entire story you can type i to open your inventory, You can merge things you find at the start only!!")
print("ENJOY!")
time.sleep(3)
print("*Here you are no soul to be seen...*")
time.sleep(4)
print("*All alone at Spuimarkt in the Hague*")
time.sleep(3)
print("You look around and see you are standing in front of the tram station next to the cinema and the Mac Donalds")
time.sleep(6)
print("*What happened here? It is pitch black outside but there are some lights burning*")
time.sleep(6)
print("")
start()
