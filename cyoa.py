# Garrett Kuns

# Project 1: Choose Your Own Adventure

def start_story():
    print("You wake up with a pounding headache barely able to open your eyes. " +
    "You reach over and put on your glasses to go grab a drink of water. Sitting up, you notice something is off. " +
    "There are three doors where the night before there was only one. At least that's what you remember. Slowly gettng up " +
    "you make your way towards the newly discovered doors. None of them look like your door and all of them look out of place. " +
    "Do you aproach the doors or do you go back to bed as this is all a bad dream?")
    # write to file
    f = open("cyoa.txt", "w")
    f.write("\nYou wake up with a pounding headache barely able to open your eyes. " +
    "\nYou reach over and put on your glasses to go grab a drink of water. Sitting up, you notice something is off. " +
    "\nThere are three doors where the night before there was only one. At least that's what you remember. Slowly gettng up " +
    "\nyou make your way towards the newly discovered doors. None of them look like your door and all of them look out of place. " +
    "\nDo you aproach the doors or do you go back to bed as this is all a bad dream?\n")
    f.close()

    print("")

def door():
    print("You make your way to the doors and notice that they are all different. They seem out of place. Hesitantly you " +
    "look at each door not seeing your door anywhere. So which door do you choose?")
    f = open("cyoa.txt", "a")
    f.write("\nYou make your way to the doors and notice that they are all different. They seem out of place. Hesitantly you " +
    "\nlook at each door not seeing your door anywhere. So which door do you choose?\n")
    f.close()
    print("")

def bed():
    print("You decide to go back to bed and hope this is all a bad dream. You lay down and close your eyes. " +
    "You feel yourself falling asleep and then you wake up again. You wake up back in your room with nothing unusual. " +
    "You walk around looking at everything before noticing the footprints on your floor. They end at the wall. " +
    "Do you examine the footprints or ignore them?")
    f = open("cyoa.txt", "a")
    f.write("\nYou decide to go back to bed and hope this is all a bad dream. You lay down and close your eyes. " +
    "\nYou feel yourself falling asleep and then you wake up again. You wake up back in your room with nothing unusual. " +
    "\nYou walk around looking at everything before noticing the footprints on your floor. They end at the wall. " +
    "\nDo you examine the footprints or ignore them?\n")
    f.close()
    print("")

def footprints():
    print("You walk over to the footprints and notice they are each a different shoe print. You examine each and " +
    "notice they are all about the same size ending at different points in front of the wall. Dow you follow the " +
    "footprints to the wall or do you leave them alone?")
    f = open("cyoa.txt", "a")
    f.write("\nYou walk over to the footprints and notice they are each a different shoe print. You examine each and " +
    "\nnotice they are all about the same size ending at different points in front of the wall. Dow you follow the " +
    "\nfootprints to the wall or pretend it is nothing?\n")
    f.close()
    print("")

def footprintsFollow():
    print("You follow the footprints to the wall and notice handprints that match your own. You panic and shuffle " +
    "to the bathroom to splash water on your face. The refreshing water does little to distract you from the " +
    "reflection in the mirror that is not you.")
    f = open("cyoa.txt", "a")
    f.write("\nYou follow the footprints to the wall and notice handprints that match your own. You panic and shuffle " +
    "\nto the bathroom to splash water on your face. The refreshing water does little to distract you from the " +
    "\nreflection in the mirror that is not you.\n")
    f.close()
    print("")

def footprintsIgnore():
    print("You decide to ignore the footprints and leave your room shutting the door behind you. " +
    "You make your way to the bathroom and get ready for school. As you make your way back to your room you " +
    "catch a glimpse of something...... but no it is just your reflection. Early mornings can do this to you. " +
    "Besides all weeks start off a little weird. You get ready for the day and head out the door.")
    f = open("cyoa.txt", "a")
    f.write("\nYou decide to ignore the footprints and leave your room shutting the door behind you. " +
    "\nYou make your way to the bathroom and get ready for school. As you make your way back to your room you " +
    "\ncatch a glimpse of something...... but no it is just your reflection. Early mornings can do this to you. " +
    "\nBesides all weeks start off a little weird. You get ready for the day and head out the door.\n")
    f.close()
    print("")

def bedIgnore():
    print("You decide to ignore the footprints and leave your room shutting the door behind you. " +
    "You walk down you stairs and enjoy breakfast. You have school today so you can't be late. " +
    "Walking out the door you notice the footprints again, all different shoes and can't ignore the steps that " +
    "soung like they are coming from your room.")
    f = open("cyoa.txt", "a")
    f.write("\nYou decide to ignore the footprints and leave your room shutting the door behind you. " +
    "\nYou walk down you stairs and enjoy breakfast. You have school today so you can't be late. " +
    "\nWalking out the door you notice the footprints again, all different shoes and can't ignore the steps that " +
    "\nsoung like they are coming from your room.\n")
    f.close()
    print("")

def door1():
    print("You walk up to the first door and notice it is made of wood. You try to open the door and it is locked. " +
    "You look around and see a key on the ground. Do you pick up the key or do you go to the next door?")
    f = open("cyoa.txt", "a")
    f.write("\nYou walk up to the first door and notice it is made of wood. You try to open the door and it is locked. " +
    "\nYou look around and see a key on the ground. Do you pick up the key or do you go to the next door?\n")
    f.close()
    print("")

def door1enter():
    print("You pick up the key and try to open the door. You turn the key and the door opens. " +
    "You walk through the door and find yourself in an old castle hallway lined with paintings. " +
    "You look left and right down the two hallways. Do you go left or right?")
    f = open("cyoa.txt", "a")
    f.write("\nYou pick up the key and try to open the door. You turn the key and the door opens. " +
    "\nYou walk through the door and find yourself in an old castle hallway lined with paintings. " +
    "\nYou look left and right down the two hallways. Do you go left or right?\n")
    f.close()
    print("")

def door1left():
    print("You walk down the left hallway and see a small door at the end with light coming from under it. " +
    "There is a faint smell of cooking bread that fills your nose. Moving towards the door, you notice the hallway " +
    "is getting smaller and smaller. By the time you get to the door, your on your hands and knees. You hear voices " +
    "coming from the other side of the door. Do you knock or do you peek in?")
    f = open("cyoa.txt", "a")
    f.write("\nYou walk down the left hallway and see a small door at the end with light coming from under it. " +
    "\nThere is a faint smell of cooking bread that fills your nose. Moving towards the door, you notice the hallway " +
    "\nis getting smaller and smaller. By the time you get to the door, your on your hands and knees. You hear voices " +
    "\ncoming from the other side of the door. Do you knock or do you peek in?\n")
    f.close()
    print("")

def door1peak():   
    print("You decide to peak in and see a small room with a table and chairs. There are people sitting and " +
    "talking but something is off. They are all looking at you. And if that was creepy enough, they all look " +
    "just like you. To the exact detail. You turn around and run back down the hallway. You hear a loud bang " +
    "and the door slams shut. You run down the hallway and see the door is locked. You try to open it but it " +
    "won't budge. You scream as the shadows slink towards you and FLASH you wake up in your bed.")
    f = open("cyoa.txt", "a")
    f.write("\nYou decide to peak in and see a small room with a table and chairs. There are people sitting and " +
    "\ntalking but something is off. They are all looking at you. And if that was creepy enough, they all look " +
    "\njust like you. To the exact detail. You turn around and run back down the hallway. You hear a loud bang " +
    "\nand the door slams shut. You run down the hallway and see the door is locked. You try to open it but it " +
    "\nwon't budge. You scream as the shadows slink towards you and FLASH you wake up in your bed.\n")
    f.close()
    print("")

def door1peakRight():   
    print("You decide to peak in and see a huge room with a table and chairs. There are people sitting and " +
    "talking but something is off. They are all looking at you. And if that was creepy enough, they all look " +
    "just like you. To the exact detail. You turn around and run back down the hallway. You hear a loud bang " +
    "and the door slams shut. You run down the hallway and see the door is locked. You try to open it but it " +
    "won't budge. You scream as the shadows slink towards you and FLASH you wake up in your bed.")
    f = open("cyoa.txt", "a")
    f.write("\nYou decide to peak in and see a huge room with a table and chairs. There are people sitting and " +
    "\ntalking but something is off. They are all looking at you. And if that was creepy enough, they all look " +
    "\njust like you. To the exact detail. You turn around and run back down the hallway. You hear a loud bang " +
    "\nand the door slams shut. You run down the hallway and see the door is locked. You try to open it but it " +
    "\nwon't budge. You scream as the shadows slink towards you and FLASH you wake up in your bed.\n")
    f.close()
    print("")

def door1retreat():
    print("You decide to retreat back down the hallway and see the door is locked. You try to open it but it " +
    "won't budge. You scream as the shadows slink towards you and FLASH you wake up in your bed.")
    f = open("cyoa.txt", "a")
    f.write("\nYou decide to retreat back down the hallway and see the door is locked. You try to open it but it " +
    "\nwon't budge. You scream as the shadows slink towards you and FLASH you wake up in your bed.\n")
    f.close()
    print("")

def door1knock():
    print("You decide to knock on the door. It opens and you see a small kitchen with a table and chairs. " +
    "There are three people sitting around the table. The all look familar but you can't place them. " +
    "They are all talking about you. You hear them say 'He is here' and 'He is awake'. " +
    "You hear a door open and close and footsteps coming towards you. Do you run or do you hide?")
    f = open("cyoa.txt", "a")
    f.write("\nYou decide to knock on the door. It opens and you see a small kitchen with a table and chairs. " +
    "\nThere are three people sitting around the table. The all look familar but you can't place them. " +
    "\nThey are all talking about you. You hear them say 'He is here' and 'He is awake'. " +
    "\nYou hear a door open and close and footsteps coming towards you. Do you run or do you hide?\n")
    f.close()
    print("")

def door1hide():
    print("You decide to hide in the closet. You hear the footsteps get closer and closer. " +
    "You hear the sliding of metal on stone as a sharp object is plunged through the door. " +
    "You hear the footsteps walk away and the door open. You hear a voice say 'He is gone'. " +
    "You feel the warmth running down your leg as you gasp. Squinting hard, you focus on your breaths in and out." +
    "You open your eyes and focus on your bedroom ceiling. Looking down that warmth was more embarrassing than blood. ")
    f = open("cyoa.txt", "a")
    f.write("\nYou decide to hide in the closet. You hear the footsteps get closer and closer. " +
    "\nYou hear the sliding of metal on stone as a sharp object is plunged through the door. " +
    "\nYou hear the footsteps walk away and the door open. You hear a voice say 'He is gone'. " +
    "\nYou feel the warmth running down your leg as you gasp. Squinting hard, you focus on your breaths in and out." +
    "\nYou open your eyes and focus on your bedroom ceiling. Looking down that warmth was more embarrassing than blood. \n")
    f.close()
    print("")

def door1run():
    print("You spin around and sprint back the way you came. Huffing the entire way you don't dare look back." +
    "You reach the door and rip it open without missing a beat. Moving down the hallway you slam into a huge person " +
    "and scream. You look up at a very familiar face. You seem to have grown drastically. And the other you stares " +
    "right back at you seeming just as confused. And what is that smell?")
    f = open("cyoa.txt", "a")
    f.write("\nYou spin around and sprint back the way you came. Huffing the entire way you don't dare look back." +
    "\nYou reach the door and rip it open without missing a beat. Moving down the hallway you slam into a huge person " +
    "\nand scream. You look up at a very familiar face. You seem to have grown drastically. And the other you stares " +
    "\nright back at you seeming just as confused. And what is that smell?\n")
    f.close()
    print("")

def door1right():
    print("You walk down the right hallway that seems never ending. As your walking you notice the stones on the floor " +
    "are getting bigger and bigger. You pass a box with rusty cleaning tools as you continue on. Ahead, you see a doorway " +
    "with a cloth hanging from it and the sound of rambling coming from behind. A putrid smell comes from inside as you move " +
    "closer. You go to take a look but a shadow startles you and you pull back. Do you peak behind the curtains or retreat to your room?")
    f = open("cyoa.txt", "a")
    f.write("\nYou walk down the right hallway that seems never ending. As your walking you notice the stones on the floor " +
    "\nare getting bigger and bigger. You pass a box with rusty cleaning tools as you continue on. Ahead, you see a doorway " +
    "\nwith a cloth hanging from it and the sound of rambling coming from behind. A putrid smell comes from inside as you move " +
    "\ncloser. You go to take a look but a shadow startles you and you pull back. Do you peak behind the curtains or retreat to your room?\n")
    f.close()
    print("")

def door2():
    print("You walk up to the second door and notice it is made of metal. You try to open the door and it is locked. " +
    "You look around and see a key on the ground. Do you pick up the key or do you go to the next door?")
    f = open("cyoa.txt", "a")
    f.write("\nYou walk up to the second door and notice it is made of metal. You try to open the door and it is locked. " +
    "\nYou look around and see a key on the ground. Do you pick up the key or do you go to the next door?\n")
    f.close()
    print("")

def door2enter():
    print("You pick up the key and try to open the door. You turn the key and the door opens. " +
    "You walk through the door and find yourself in a grand room with tables full of food. People in formal " +
    "attire are sitting at the tables talking and dancing. There are dressing rooms on your left with a suit " +
    "just your size. On your right is a table full of luxorious gifts. Do you steal a gift and return through " +
    "the door or dress up and attend the party?")
    f = open("cyoa.txt", "a")
    f.write("\nYou pick up the key and try to open the door. You turn the key and the door opens. " +
    "\nYou walk through the door and find yourself in a grand room with tables full of food. People in formal " +
    "\nattire are sitting at the tables talking and dancing. There are dressing rooms on your left with a suit " +
    "\njust your size. On your right is a table full of luxorious gifts. Do you steal a gift and return through " +
    "\nthe door or dress up and attend the party?\n")
    f.close()
    print("")

def door2steal():
    print("You walk over to the table and quickly pick up some fine jewelry. You stuff a few more things into your pocket " +
    "and run back to the door. You open the door and run back to the room with the three doors. You close the door and " +
    "turn around hitting something solid but soft. You look down and see a small child. The child looks up at you and " +
    "says 'Thank you for the gift'. Do you give it to them or do you ignore them and return to bed?")
    f = open("cyoa.txt", "a")
    f.write("\nYou walk over to the table and quickly pick up some fine jewelry. You stuff a few more things into your pocket " +
    "\nand run back to the door. You open the door and run back to the room with the three doors. You close the door and " +
    "\nturn around hitting something solid but soft. You look down and see a small child. The child looks up at you and " +
    "\nsays 'Thank you for the gift'. Do you give it to them or do you ignore them and return to bed?\n")
    f.close()
    print("")

def door2give():
    print("You walk over to the child and give them the gift. The child smiles and runs off. You return to bed and " +
    "fall asleep. You wake up the next morning and find yourself in your bed. You look around and see the child " +
    "sitting on your bed. The child looks up at you and says 'Don't you remember'?")
    f = open("cyoa.txt", "a")
    f.write("\nYou walk over to the child and give them the gift. The child smiles and runs off. You return to bed and " +
    "\nfall asleep. You wake up the next morning and find yourself in your bed. You look around and see the child " +
    "\nsitting on your bed. The child looks up at you and says 'Don't you remember?'\n")
    f.close()
    print("")

def door2return():
    print("You ignore the child and return to bed. You fall asleep and wake up the next morning. You look around " +
    "and see the child sitting on your bed. The child looks up at you and says 'I am sorry' and he runs off with your underwear.")
    f = open("cyoa.txt", "a")
    f.write("\nYou ignore the child and return to bed. You fall asleep and wake up the next morning. You look around " +
    "\nand see the child sitting on your bed. The child looks up at you and says 'I am sorry' and he runs off with your underwear.\n")
    f.close()
    print("")

def door2dress():
    print("You walk into the dressing room and change into a suit. You walk out of the room and see a table with a cute " +
    "young girl sitting there. You make your way to the table and slide into the chair across from her. You see her communicating " + 
    "with someone but cannot see them on the other side of her. Do you interrupt her conversation or try to peak and see who she is talking to?" +
    "Do you interrupt her or do you wait.")
    f = open("cyoa.txt", "a")
    f.write("\nYou walk into the dressing room and change into a suit. You walk out of the room and see a table with a cute " +
    "\nyoung girl sitting there. You make your way to the table and slide into the chair across from her. You see her communicating " + 
    "\nwith someone but cannot see them on the other side of her. Do you interrupt her conversation or try to peak and see who she is talking to?" +
    "\nDo you interrupt her or do you wait.\n")
    f.close()
    print("")

def door2wait():
    print("You wait and see who she is talking to and are shocked to see your father. You sit there agast as he continues " +
    "talking before you hear your mothers name. The beautiful girl turns around and you smile sheepishly as she puts her hand " +
    "on your cheek and says 'It's so good to see you'. You wake up with tears in your eyes as you old wrinkled hands hold her picture.")
    f = open("cyoa.txt", "a")
    f.write("\nYou wait and see who she is talking to and are shocked to see your father. You sit there agast as he continues " +
    "\ntalking before you hear your mothers name. The beautiful girl turns around and you smile sheepishly as she puts her hand " +
    "\non your cheek and says 'It's so good to see you'. You wake up with tears in your eyes as you old wrinkled hands hold her picture.\n")
    f.close()
    print("")

def door2interrupt():
    print("You clear your throat as you interoduce yourself. The young lady turns around and smiles at you. She politely introduces " +
    "herself and to you surprise has the same name as your mother. She grabs your hand tenderly and pats the top of it saying " +
    "'I thought you better than to interrupt someone.' You nod slowly trying to take it all in before her previous conversation " +
    "resumes. You sit there for a long while before you start to fade.")
    f = open("cyoa.txt", "a")
    f.write("\nYou clear your throat as you interoduce yourself. The young lady turns around and smiles at you. She politely introduces " +
    "\nherself and to you surprise has the same name as your mother. She grabs your hand tenderly and pats the top of it saying " +
    "\n'I thought you better than to interrupt someone.' You nod slowly trying to take it all in before her previous conversation " +
    "\nresumes. You sit there for a long while before you start to fade.\n")
    f.close()
    print("")

def door3():
    print("You walk up to the third door and notice it is made of stone. You try to open the door and it is locked. " +
    "You look around and see a key on the ground. Do you pick up the key or do you go to the next door?")
    f = open("cyoa.txt", "a")
    f.write("\nYou walk up to the third door and notice it is made of stone. You try to open the door and it is locked. " +
    "\nYou look around and see a key on the ground. Do you pick up the key or do you go to the next door?\n")
    f.close()
    print("")

def door3enter():
    print("You pick up the key and try to open the door. You turn the key and the door opens. " +
    "You walk through the door and fall a couple feet to a mossy floor. You cut your hand on something " +
    "sharp that retreats at your presence. Do you follow the object to tend to your hand?")
    f = open("cyoa.txt", "a")
    f.write("\nYou pick up the key and try to open the door. You turn the key and the door opens. " +
    "\nYou walk through the door and fall a couple feet to a mossy floor. You cut your hand on something " +
    "\nsharp that retreats at your presence. Do you follow the object to tend to your hand?\n")
    f.close()
    print("")

def door3follow():
    print("You follow the object to a small cave. You walk in and see a small creature with a large head and a " +
    "long tail. It is holding a small piece of cloth in its hand. Do you remove the cloth or leave it?")
    f = open("cyoa.txt", "a")
    f.write("\nYou follow the object to a small cave. You walk in and see a small creature with a large head and a " +
    "\nlong tail. It is holding a small piece of cloth in its hand. Do you remove the cloth or leave it?\n")
    f.close()
    print("")

def door3cloth():
    print("You take the cloth that starts to fall apart in your hand. You try to grasp all the pieces but the creature " +
    "just looks at you. It snarls as you move towards it and pulls back wardingly. You return to catching all the cloth " +
    "pieces but to no avail. You're hand starts to blacken where you cut it and the color seems to be running " +
    "up your veins. You panick and your fright startles the creature who lunges at you. The last thing you remember is the " +
    "firey burning running up your arm.")
    f = open("cyoa.txt", "a")
    f.write("\nYou take the cloth that starts to fall apart in your hand. You try to grasp all the pieces but the creature " +
    "\njust looks at you. It snarls as you move towards it and pulls back wardingly. You return to catching all the cloth " +
    "\npieces but to no avail. You're hand starts to blacken where you cut it and the color seems to be running " +
    "\nup your veins. You panick and your fright startles the creature who lunges at you. The last thing you remember is the " +
    "\nfirey burning running up your arm.\n")
    f.close()
    print("")

def door3leave():
    print("You leave the cloth where it is and walk out of the cave. You walk back to the door and open it. You walk out " +
    "and see a small trail that leads under your bed. You look but there is nothing there. You hear your mom yell your name " +
    "and hurry down to her rushed call. To your joy she has surprised you with a puppy that is missing a leg. Regardless it is " +
    "as happy as ever.")
    f = open("cyoa.txt", "a")
    f.write("\nYou leave the cloth where it is and walk out of the cave. You walk back to the door and open it. You walk out " +
    "\nand see a small trail that leads under your bed. You look but there is nothing there. You hear your mom yell your name " +
    "\nand hurry down to her rushed call. To your joy she has surprised you with a puppy that is missing a leg. Regardless it is " +
    "\nas happy as ever.\n")
    f.close()
    print("")

def door3tend():
    print("You pull back and look at your hand with the trickle of blood that is falling. As it hits the ground the" +
    "area around you starts to move and you feel dizzy. The morphing of the trees and the twisting of the light is" +
    "enough to make you nautious. Right before you think you're going to loose it, everything stops and you open" +
    "your eyes to three out of place doors.")
    f = open("cyoa.txt", "a")
    f.write("\nYou pull back and look at your hand with the trickle of blood that is falling. As it hits the ground the" +
    "\narea around you starts to move and you feel dizzy. The morphing of the trees and the twisting of the light is" +
    "\nenough to make you nautious. Right before you think you're going to loose it, everything stops and you open" +
    "\nyour eyes to three out of place doors.\n")
    f.close()
    print("")

def doors(choice):
    if choice == "door1":
        valid = False
        pick = "pick up"
        next = "next door"
        while valid == False:
            user_input = input("Enter 'Pick Up' or 'Next Door': ")
            if user_input.lower() == pick.lower():
                f = open("cyoa.txt", "a")
                f.write("\nPick Up\n")
                f.close()
                valid = True
                door1enter()
                choice = "door1enter"
                door_entered(choice)
            elif user_input.lower() == next.lower():
                f = open("cyoa.txt", "a")
                f.write("\nNext Door\n")
                f.close()
                valid = True
                choice = "door2"
                doors(choice)
            else:
                print("That is not a valid input. Please try again.")
    elif choice == "door2":
        valid = False
        pick = "pick up"
        next = "next door"
        while valid == False:
            user_input = input("Enter 'Pick Up' or 'Next Door': ")
            if user_input.lower() == pick.lower():
                f = open("cyoa.txt", "a")
                f.write("\nPick Up\n")
                f.close()
                valid = True
                door2enter()
                choice = "door2enter"
                door_entered(choice)
            elif user_input.lower() == next.lower():
                f = open("cyoa.txt", "a")
                f.write("\nNext Door\n")
                f.close()
                valid = True
                choice = "door3"
                doors(choice)
            else:
                print("That is not a valid input. Please try again.")
    elif choice == "door3":
        valid = False
        pick = "pick up"
        next = "next door"
        while valid == False:
            user_input = input("Enter 'Pick Up' or 'Next Door': ")
            if user_input.lower() == pick.lower():
                f = open("cyoa.txt", "a")
                f.write("\nPick Up\n")
                f.close()
                valid = True
                door3enter()
                choice = "door3enter"
                door_entered(choice)
            elif user_input.lower() == next.lower():
                f = open("cyoa.txt", "a")
                f.write("\nNext Door\n")
                f.close()
                valid = True
                choice = "door1"
                doors(choice)
            else:
                print("That is not a valid input. Please try again.")

# These are the different options for each door the user enters
def door_entered(choice):
    if choice == "door1enter":
        valid = False
        left = "left"
        right = "right"
        while valid == False:
            user_input = input("Enter 'Left' or 'Right': ")
            if user_input.lower() == left.lower():
                f = open("cyoa.txt", "a")
                f.write("\nLeft\n")
                f.close()
                valid = True
                door1left()
                choice = "left"
            elif user_input.lower() == right.lower():
                f = open("cyoa.txt", "a")
                f.write("\nRight\n")
                f.close()
                valid = True
                door1right()
                choice = "right"
            else:
                print("That is not a valid input. Please try again.")
    elif choice == "door2enter":
        valid = False
        steal = "Steal"
        dress = "Dress"
        while valid == False:
            user_input = input("Enter 'Steal' or 'Dress': ")
            if user_input.lower() == steal.lower():
                f = open("cyoa.txt", "a")
                f.write("\Steal\n")
                f.close()
                valid = True
                door2steal()
                choice = "steal"
            elif user_input.lower() == dress.lower():
                f = open("cyoa.txt", "a")
                f.write("\nDress\n")
                f.close()
                valid = True
                door2dress()
                choice = "dress"
            else:
                print("That is not a valid input. Please try again.")
    elif choice == "door3enter":
        valid = False
        follow = "follow"
        tend = "tend"
        while valid == False:
            user_input = input("Enter 'Follow' or 'Tend': ")
            if user_input.lower() == follow.lower():
                f = open("cyoa.txt", "a")
                f.write("\nFollow\n")
                f.close()
                valid = True
                door3follow()
                choice = "follow"
            elif user_input.lower() == tend.lower():
                f = open("cyoa.txt", "a")
                f.write("\nTend\n")
                f.close()
                valid = True
                door3tend()
                choice = "tend"
            else:
                print("That is not a valid input. Please try again.")

    # door 1 left or right choices
    if choice == "left":
        valid = False
        peek = "peek"
        knock = "knock"
        while valid == False:
            user_input = input("Enter 'Peek' or 'Knock': ")
            if user_input.lower() == peek.lower():
                f = open("cyoa.txt", "a")
                f.write("\nPeek\n")
                f.close()
                valid = True
                door1peak()
                choice = "peek"
            elif user_input.lower() == knock.lower():
                f = open("cyoa.txt", "a")
                f.write("\nKnock\n")
                f.close()
                valid = True
                door1knock()
                choice = "knock"
            else:
                print("That is not a valid input. Please try again.")
    elif choice == "right":
        valid = False
        peek = "peek"
        retreat = "retreat"
        while valid == False:
            user_input = input("Enter 'Peek' or 'Retreat': ")
            if user_input.lower() == peek.lower():
                f = open("cyoa.txt", "a")
                f.write("\nPeek\n")
                f.close()
                valid = True
                door1peakRight()
            elif user_input.lower() == retreat.lower():
                f = open("cyoa.txt", "a")
                f.write("\nRetreat\n")
                f.close()
                valid = True
                door1retreat()
            else:
                print("That is not a valid input. Please try again.")

    # door 1 know or peek
    if choice == "knock":
        valid = False
        run = "run"
        hide = "hide"
        while valid == False:
            user_input = input("Enter 'Run' or 'Hide': ")
            if user_input.lower() == run.lower():
                f = open("cyoa.txt", "a")
                f.write("\nRun\n")
                f.close()
                valid = True
                door1run()
            elif user_input.lower() == hide.lower():
                f = open("cyoa.txt", "a")
                f.write("\nHide\n")
                f.close()
                valid = True
                door1hide()
            else:
                print("That is not a valid input. Please try again.")
    
    # door 1 knock run or hide
    if choice == "run":
        valid = False
        run = "run"
        hide = "hide"
        while valid == False:
            user_input = input("Enter 'Run' or 'Hide': ")
            if user_input.lower() == run.lower():
                f = open("cyoa.txt", "a")
                f.write("\nRun\n")
                f.close()
                valid = True
                door1run()
            elif user_input.lower() == hide.lower():
                f = open("cyoa.txt", "a")
                f.write("\nHide\n")
                f.close()
                valid = True
                door1hide()
            else:
                print("That is not a valid input. Please try again.")
    
    # door 2 dress choices
    if choice == "steal":
        valid = False
        give = "give"
        goback = "return"
        while valid == False:
            user_input = input("Enter 'Give' or 'Return': ")
            if user_input.lower() == give.lower():
                f = open("cyoa.txt", "a")
                f.write("\nGive\n")
                f.close()
                valid = True
                door2give()
            elif user_input.lower() == goback.lower():
                f = open("cyoa.txt", "a")
                f.write("\nReturn\n")
                f.close()
                valid = True
                door2return()
            else:
                print("That is not a valid input. Please try again.")
    elif choice == "dress":
        valid = False
        wait = "wait"
        interrupt = "interrupt"
        while valid == False:
            user_input = input("Enter 'Wait' or 'Interrupt': ")
            if user_input.lower() == wait.lower():
                f = open("cyoa.txt", "a")
                f.write("\nWait\n")
                f.close()
                valid = True
                door2wait()
            elif user_input.lower() == interrupt.lower():
                f = open("cyoa.txt", "a")
                f.write("\nInterrupt\n")
                f.close()
                valid = True
                door2interrupt()
            else:
                print("That is not a valid input. Please try again.")

    # door 3 follow or tend
    if choice == "follow":
        valid = False
        take = "take"
        leave = "leave"
        while valid == False:
            user_input = input("Enter 'Take' or 'Leave': ")
            if user_input.lower() == take.lower():
                f = open("cyoa.txt", "a")
                f.write("\nTake the Cloth\n")
                f.close()
                valid = True
                door3cloth()
            elif user_input.lower() == leave.lower():
                f = open("cyoa.txt", "a")
                f.write("\nLeave\n")
                f.close()
                valid = True
                door3leave()
            else:
                print("That is not a valid input. Please try again.")

# This is the start of the story
start_story()

# User hears initial story and can choose either to approach the doors or go back to bed
valid = False
choice = ""
app = "approach"
toBed = "bed"
while valid == False:
    user_input = input("Enter 'Approach' or 'Bed': ")
    if user_input.lower() == app.lower():
        valid = True
        f = open("cyoa.txt", "a")
        f.write("\nApproach\n")
        f.close()
        door()
        choice = "door"
    elif user_input.lower() == toBed.lower():
        valid = True
        f = open("cyoa.txt", "a")
        f.write("\nBed\n")
        f.close()
        bed()
        choice = "bed"
    else:
        print("That is not a valid input. Please try again.")

# user approaches the doors and can choose which door to go to
if choice == "door":
    valid = False
    doorOne = "door 1"
    doorTwo = "door 2"
    doorThree = "door 3"
    while valid == False:
        user_input = input("Enter 'Door 1', 'Door 2', or 'Door 3': ")
        if user_input.lower() == doorOne.lower():
            valid = True
            f = open("cyoa.txt", "a")
            f.write("\nDoor 1\n")
            f.close()
            door1()
            choice = "door1"
        elif user_input.lower() == doorTwo.lower():
            valid = True
            f = open("cyoa.txt", "a")
            f.write("\nDoor 2\n")
            f.close()
            door2()
            choice = "door2"
        elif user_input.lower() == doorThree.lower():
            valid = True
            f = open("cyoa.txt", "a")
            f.write("\nDoor 3\n")
            f.close()
            door3()
            choice = "door3"
        else:
            print("That is not a valid input. Please try again.")
elif choice == "bed":
    valid = False
    footprint = "footprint"
    ignore = "ignore"
    while valid == False:
        user_input = input("Enter 'Footprint' or 'Ignore': ")
        if user_input.lower() == footprint.lower():
            valid = True
            f = open("cyoa.txt", "a")
            f.write("\nFootprint\n")
            f.close()
            footprints()
            choice = "footprint"
        elif user_input.lower() == ignore.lower():
            valid = True
            f = open("cyoa.txt", "a")
            f.write("\nIgnore\n")
            f.close()
            bedIgnore()
            choice = "ignore"
        else:
            print("That is not a valid input. Please try again.")

# user chooses footprint and follows the footprints to explore more
if choice == "footprint":
    valid = False
    follow = "follow"
    ignore = "ignore"
    while valid == False:
        user_input = input("Enter 'Follow' or 'Ignore': ")
        if user_input.lower() == follow.lower():
            valid = True
            f = open("cyoa.txt", "a")
            f.write("\nFollow\n")
            f.close()
            footprintsFollow()
            choice = "following"
        elif user_input.lower() == ignore.lower():
            valid = True
            f = open("cyoa.txt", "a")
            f.write("\nIgnore\n")
            f.close()
            footprintsIgnore()
            choice = "ignore"
        else:
            print("That is not a valid input. Please try again.")

# user chooses a door and can choose to pick up the key or go to the next door
# This is set up in functions as the user can move between doors prior to moving on
doors(choice)
door_entered(choice)

