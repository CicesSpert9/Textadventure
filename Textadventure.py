# Great job so far! I'm adding comments throughout to help you organize better
# and to help you further throughout your code!
import time

# I would suggest split into multiple functions rather than one whole block
# An example of how to separate this into cleaner chunks would be:

# Climb Tree function --> Handles the beginning yes/no for climbing the tree
# Grabbing Bird Eggs function --> Handles the rest of the left side of the tree
# Enter a House function --> Handles the "Enter a house" portion of the tree
# Grab a stick/enter cave --> Handles the rest of the tree (this can maybe be combined or separated, your choice!)
def climbtree():
    global pickbirdegg
    exploretree = input("You are an explore with a friend named Joe that is curious about a forest nearby. Nearby, you find an intruiging tree that you would like to climb. Do you want to climb it?").lower()
    # Clause for climbing tree : yes option
    if exploretree == "yes":
        pickbirdegg = input("You find an bird egg in a nest. Pick up bird egg").lower()
        pickbirdegg()

    if exploretree == "no":
        global enterhouse
        enterhouse = input("You find a house nearby. Would you like to enter?").lower()
        enterhouse()


def enterhouse():
    if enterhouse == "yes":
        fight = input("A dark figure is approaching.").lower()
        fight()
    
    if enterhouse == "no":

def fight():



def grabbirdegg():
    if pickbirdegg == "yes":
            # Based off your map, you throw the eggs at Joe & then die ;p but if you changed the story thats fine!
        print("you picked up the bird egg and died because the egg had a sharp edge with poison around the shell and you accidently got a cut from it.").lower()
        
        # Make sure here you add the clause for a "no" option for grabbing the bird eggs

    # Clause for climbing tree : no option
    if exploretree == "no":
         
         # Entering the house : yes option
         if enterhouse == "yes":
             fightorhide = input("A figure is approaching. Hide or fight with your bare hands? ").lower()
             
             # What if the user doesn't type in hide/fight, what would happen?
             #  ^--> You should be thinking this throughout your project!!
             if fightorhide == "hide":
                 print("You have hidden behind the sofa")
             if fightorhide == "fight":
                 print("There is a grumpy old lady")

        # Entering the house : no option
            
