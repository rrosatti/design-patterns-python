class MakeMeal:

    def prepare(self): pass
    def cook(self): pass
    def eat(self): pass

    def go(self):
        self.prepare()
        self.cook()
        self.eat()

class MakePizza(MakeMeal):
    def prepare(self):
        print "Prepare Pizza"

    def cook(self):
        print "Cook Pizza"

    def eat(self):
        print "Eat Pizza"

class MakeRice(MakeMeal):

    def prepare(self):
        print "Prepare Rice"

    def cook(self):
        print "Cook Rice"

    def eat(self):
        print "Eat Rice"

def main():
    makePizza = MakePizza()
    makePizza.go()

    print 25*"+"

    makeRice = MakeRice()
    makeRice.go()

if __name__ == "__main__":
    main()
