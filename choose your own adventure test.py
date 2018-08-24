
print("Welcome to 'THE SHELL'")
print("\n You are stuck in the shell. \n You must find your way out and survive. \n Choose wisely.")
startgame = input("\nStart Game?\nType 'yes' or 'no'\n\n")
if startgame == "yes":
    print("\nGood choice. Now,\nYou heard a noise in the kitchen.\nWhat do you do?\n")
else:
    print("\nWrong answer.\nYou died.\n")
    sys.exit()

round_1 = input("\nOption 1: continue walking down the hall\nor\nOption 2: check in the kitchen\nType in # option\n")
# YOU WALK DOWN THE HALL
if round_1 == "1":
    print("\n You trip running on the dusty rug.\n The killer now knows where you are, but fortunately for you, stubs his pinky toe on the edge of the table.\n You are able to run and lock yourself into a dark room.\n")

# youre trapped in the room
    round_2 = input("\nTurn on lights?\n\nType 'yes' or 'no'\n")

    # you turn on lights YOU DIED
    if round_2 == "yes":
        print("\n You met eyes with a demon, fell back, and stepped on a thumbtack.\n You died of blood loss.\n Next time carry bandaids.\n")
        print("\n\nGAME OVER\n")
        exit()
            
    # you dont turn on lights
    if round_2 == "no":
        print("\n Turns out the killer has a fear of the dark,so he never checks the room.\n But you know he's waiting outside.\n Do you:\n")

    else:
        print("\ninvalid answer. start over\n")
        exit()

    round_3 = input("\nOption 1: open door and try to escape\nor\nOption 2: stay inside the room\nType in # option\n")

    #open door
    if round_3 == "1":
        print("\n You hit the killer while swinging the door open, knocking him out.\n You find the exit and escape.\n Congrats!\n You escaped 'THE SHELL'\n\n")
        print("________$$$$_______________")
        print("_______$$__$_______________")
        print("_______$___$$______________")
        print("_______$___$$______________")
        print("_______$$___$$_____________")
        print("________$____$$____________")
        print("________$$____$$$__________")
        print("_________$$_____$$_________")
        print("_________$$______$$________")
        print("__________$_______$$_______")
        print("____$$$$$$$________$$______")
        print("__$$$_______________$$$$$$")
        print("_$$____$$$$____________$$$")
        print("_$___$$$__$$$____________$$")
        print("_$$________$$$____________$")
        print("__$$____$$$$$$____________$")
        print("__$$$$$$$____$$___________$")
        print("__$$_______$$$$___________$")
        print("___$$$$$$$$$__$$_________$$")
        print("____$________$$$$_____$$$$")
        print("____$$____$$$$$$____$$$$$$")
        print("_____$$$$$$____$$__$$")
        print("_______$_____$$$_$$$")
        print("________$$$$$$$$$$")
        print("\n\nthats it goodbye")
        exit()

    #stay inside room you DEAD
    if round_3 == "2":
        print("\n You died of starvation waiting in the room.\n Carry snacks next time.")
        print("\n\nGAME OVER\n")
        exit()
    else:
        print("\ninvalid answer. start over\n")
        exit()
#i tried adding break but it kept saying it was out of the loop and idk


# YOU CHECK THE KITCHEN   
if round_1 == "2":
    print("\n You wasted time but you found a pair of scissors.\n You hear the killer running towards you now.\n\n Do you:")
else:
    print("\ninvalid answer. start over\n")
    exit()

round_4 = input("\nOption 1: hold up the scissors as a weapon\nor\nOption 2: hide in the over-sized pantry\nType in # option.\n")

# you defend. YOU DIED
if round_4 == "1":
    print("\n The killer shows himself holding up a kitten.\n You are deadly allergic to cats.\n Always bring an EpiPen with you")
    print("\n\nGAME OVER\n")
    exit()

# hide in pantry
if round_4 == "2":
    print("\n The killer passes you and checks the other rooms.\n\nDo you:")
else:
    print("\ninvalid answer. start over")
    exit()

round_5 = input("\nOption 1: stay in pantry\nor\nOption 2: make a run towards the exit with your weapon\n")
#you DEAD
if round_5 == "2":
    print("\n You tripped and stabbed yourself.\n Never run with scissors.\n")
    print("\n\nGAME OVER\n")

#you win
if round_5 == "1":
    print("\n You stayed in there with enough food and waterfor a month.\n By the the killer gets bored and moves on to his next weekend.\n You survived,, i guess?\n Congrats.\n")
    print("________$$$$_______________")
    print("_______$$__$_______________")
    print("_______$___$$______________")
    print("_______$___$$______________")
    print("_______$$___$$_____________")
    print("________$____$$____________")
    print("________$$____$$$__________")
    print("_________$$_____$$_________")
    print("_________$$______$$________")
    print("__________$_______$$_______")
    print("____$$$$$$$________$$______")
    print("__$$$_______________$$$$$$")
    print("_$$____$$$$____________$$$")
    print("_$___$$$__$$$____________$$")
    print("_$$________$$$____________$")
    print("__$$____$$$$$$____________$")
    print("__$$$$$$$____$$___________$")
    print("__$$_______$$$$___________$")
    print("___$$$$$$$$$__$$_________$$")
    print("____$________$$$$_____$$$$")
    print("____$$____$$$$$$____$$$$$$")
    print("_____$$$$$$____$$__$$")
    print("_______$_____$$$_$$$")
    print("________$$$$$$$$$$")
    print("\n\nthats it goodbye")
    exit()
else:
    print("\nNot a valid answer.\nStart Over (im sorry im too lazy)")
    exit()

game()

