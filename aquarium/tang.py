from aquarium.fish import Fish

class Tang(Fish):

    def __init__(self, memory_loss):
        Fish.__init__(self)
        self.memory_loss = memory_loss

    def feed(self):
        self.weight += 1

