#===========================================================================
# Readme:
# () This is the example in P18-19 on book <Design Pattern>.
# () Class inheritance figure is in P13.
# () Skill: (1) Program to an interface. (2) Change performance action
#       dynamically.
#===========================================================================
__author__ = 'djiao'

#===========================================================
# Calss definition
#===========================================================

class MakeSound:

    def __init__(self, className):
        self.className = className

    def make_sound(self):
        pass

class Quack(MakeSound):

    # Automatically inherit the init func.
    def make_sound(self):
        print "quack, quack, ..."

class Squeak(MakeSound):

    def make_sound(self):
        print "squeak, squeak, ..."

#===========================================================
# Parent class, defined based on both fly and quack.
#===========================================================

class GeneralDuck():

    def __init__(self, className, quackBehavior):
        self.className = className
        self.quackBehavior = quackBehavior

    def perform_quack(self):                    # Will overwrite the "quack" method in base class "quack".
        self.quackBehavior.make_sound()           # Is "self" here required ??

    # Setting behavior dynamically
    def set_quack_behavior(self, newQuack):
        self.quackBehavior = newQuack

#===========================================================================
# Main func
#===========================================================================

if __name__ == "__main__":

    # Make a GeneralDuck by the interface method.
    cQuack = Quack("quack")
    GeneralDuck = GeneralDuck("GeneralDuck", cQuack)
    GeneralDuck.perform_quack()                     #call the one defined in extended class.

    # Change the quack sound of GeneralDuck dynamically.
    cSqueak = Squeak("squeak")
    GeneralDuck.set_quack_behavior(cSqueak)
    GeneralDuck.perform_quack()

