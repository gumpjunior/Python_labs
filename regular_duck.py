__author__ = 'djiao'


class fly:

    def __init__(self, className):
        self.className = className

    def fly(self):
        print "Output at class ", self.className


class quack:

    def __init__(self, className):
        self.className = className

    def quack(self):
        print "Output at class ", self.className

class regularDuck(fly, quack):

    def __init__(self, className):      # will this var "className" overwrite the one defined in base class "fly.py"??
        self.className = className

    #def fly(self):     # inherit directly from parent class.

#    def quack(self):
#        print "Output at class ", self.className
#        print "gaga, ga..."

regularDuck = regularDuck("regularDuck")

regularDuck.fly()
regularDuck.quack()
