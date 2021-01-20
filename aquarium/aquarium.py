from aquarium.fish import Fish

class Aquarium():


    def __init__(self):
        self.fish = []


    def addFish(self, fish):
        self.fish.append(fish)

    def feed(self):
        for i in self.fish:
            i.feed()

    def removeFish(self):
        for i in self.fish:
            if i.weight >= 11:
                self.fish.remove(i)

    def getStatus(self):
        for i in self.fish:
            i.status()