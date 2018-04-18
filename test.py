class testing:

    def __init__(self):
        self.a = 2
        self.b = 3

    def main(self):
        self.doThatMath(self.a, self.b)
        self.printThatLine(self.sum)

    def doThatMath(self, a, b):
        self.sum = a + b
        return self.sum

    def printThatLine(self, sum):
        print(sum)


t = testing()
t.main()