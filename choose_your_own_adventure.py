name = input("What's you name? ")
print("Welcome",name,"to your adventure!")

answer = input("You come to a fork in the road. Do you go left or right? (left/right) ").lower()
if answer == "left":
    answer = input("You go left and walk deep into a forrest, the wind is blowing the branches of the trees and you start to think you hear voices in the distance, you can't be sure but you think you hear a voice call out '"+name.upper()+"!'. Do you go towards the voice or run? (voice/run) ").lower()
    if answer == "voice":
        print("You move through the thick forrest and eventually find a leprechaun who gives you a pot of gold. You WIN!")
    elif answer == "run":
        print("You start to sprint and trip on the root of a tree and fall and pass out.")
    else:
        print("You get abducted by aliens, you're never seen again")
elif answer == "right":
    answer = input("You walk for a few hours and come to the edge of a cliff. Do you try to climb down or look for a bridge? (climb/bridge) ").lower()  
    if answer == "climb":
        print("You instantly slip and fall down the cliff.")
    elif answer ==  "bridge":
        answer = input("You spot an old bridge in the distance and head towards it. It's shaking in the wind and barely attached to the edge of the cliff. Do you try to cross? (yes/no) ").lower()
        if answer == "yes":
            print("You move slowly across the bridge and have almost made it the whole way across when suddenly you get stuck by lightening")
        elif answer == "no":
            print("You take another look around and see there's a band new bridge that leads you right back to your house. You make it home succesfully. YOU WIN!")
        else:
            print("You take too long to decide, you die.")
    else:
        print("You're too tired to try something different, you die.")
else:
    print("You tried to go straight and walked into a wall and died.")

print("Thanks for playing",name)