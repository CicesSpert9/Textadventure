def climbtree():
    exploretree = input("You are an explore with a friend named Joe that is curious about a forest nearby. Nearby, you find an intruiging tree that you would like to climb. Do you want to climb it?").lower()
    if exploretree == "yes":
        pickbirdegg = input("You find an bird egg in a nest. Pick up bird egg").lower()
        if pickbirdegg == "yes":
            print("you picked up the bird egg and died because the egg had a sharp edge with poison around the shell and you accidently got a cut from it.").lower()
    if exploretree == "no":
         enterhouse = input("You find a house nearby. Would you like to enter?").lower()
         if enterhouse == "yes":
             fightorhide = input("A figure is approaching. Hide or fight with your bare hands? ").lower()
             if fightorhide == "hide":
                 print("You have hidden behind the sofa")
             if fightorhide == "fight":
                 print("There is a grumpy old lady")
                 
