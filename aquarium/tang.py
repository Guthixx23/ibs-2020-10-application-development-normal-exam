from aquarium.fish import Fish


class Tang(Fish):

    def __init__(self, name, weight, color, memory_loss):
        Fish.__init__(self)
        self.name = name
        self.weight = weight
        self.color = color
        self.memory_loss = memory_loss

    # overriden method from fish class, memory loss is printed too
    def status(self):
        print(
            str(self.name) + ", weight: " + str(self.weight) + ", colour: " + str(self.color) + ", memory loss: " + str(
                self.memory_loss))
