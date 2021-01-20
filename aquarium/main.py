from aquarium.aquarium_class import Aquarium
from aquarium.fish import Fish
from aquarium.clownfish import Clownfish
from aquarium.tang import Tang
from aquarium.kong import Kong

# creating the objects
aqua = Aquarium()
adam = Clownfish("Adam", 8, "Red", "Yellow")
bella = Tang("Bella", 5, "Blue", False)
charlie = Kong("Charlie", 10, "Gray")
delta = Clownfish("Delta", 6, "purple", "pink")
edward = Tang("Edward", 19, "green", True)
frankie = Kong("Frankie", 10, "white")

# observing empty status
aqua.getStatus()

# adding fishes to aquarium
aqua.addFish(adam)
aqua.addFish(bella)
aqua.addFish(charlie)
aqua.addFish(delta)
aqua.addFish(edward)
aqua.addFish(frankie)

# tests below
print("-----------------")
aqua.getStatus()

print("-----------------")
aqua.removeFish()
aqua.getStatus()

print("-----------------")
aqua.feed()
aqua.feed()
aqua.getStatus()
print("-----------------")

aqua.removeFish()
aqua.getStatus()

print("-----------------")
