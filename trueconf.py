class Trueconf:
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode
    
    def give(self, index):
        self.lines = []
        self.f = open(self.file, 'r')
        
        for line in self.f:
            self.lines.append(line)
        
        return self.lines[index - 1]

my = Trueconf("test.true", "read")
print(my.give(1))