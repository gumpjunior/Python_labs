__author__ = 'djiao'

#===========================================================================
# Calss definition
#===========================================================================

class fly:

    def __init__(self, className):
        self.className = className

    def fly(self):
        print "Quack at class ", self.className

class quack:

    def __init__(self, className):
        self.className = className

    def quack(self):
        print "Quack at class ", self.className

#===========================================================
# Parent class, defined based on both fly and quack.
#===========================================================

class regularDuck(fly, quack):

    def __init__(self, className):      #"className" here will overwrite the one defined in base class "fly.py",
                                        #and "quack.py". And all the funcs in base class use var "className" will
                                        #use the value assigned here.
        self.className = className

    #def fly(self):     # inherit directly from parent class, if same, no need to re-define.

    def quack(self):                    # Will overwrite the "quack" method in base class "quack".
        print "Quack: gaga, ga..."

#===========================================================================
# Main func
#===========================================================================

regularDuck = regularDuck("regularDuck")

regularDuck.fly()                       #call the one defined in base class. Also output class Duck's name.
regularDuck.quack()                     #call the one defined in extended class.
