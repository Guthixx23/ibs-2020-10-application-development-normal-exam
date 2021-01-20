from aquarium.fish import Fish


# container class for fish objects
class Aquarium():

    def __init__(self):
        self.fish = []

    # adding a selected fish to aquarium
    def addFish(self, fish):
        self.fish.append(fish)

    # feeding every fish
    def feed(self):
        for i in self.fish:
            i.feed()

    # removing fish at and over 11grams
    def removeFish(self):
        for i in self.fish:
            if i.weight >= 11:
                self.fish.remove(i)

    # printing all fish details in aquarium
    def getStatus(self):
        for i in self.fish:
            i.status()
