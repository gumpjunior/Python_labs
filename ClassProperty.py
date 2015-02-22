__author__ = 'djiao'

class SoundInterface:        #Also called "Parent Class".

    def __init__(self, className):
        self.className = className

    def make_sound(self):
        pass

    def pos_mark(self):
        print "@, pos_mark(), class ", self.className

class Bark(SoundInterface):

    def __init__(self, className):
        self.className = className

    def make_sound(self):
        print "wong, wong wong ..."

    def pos_mark(self):
        print "@, pos_mark(), class ", self.className

#===========================================================================
# Main func
#===========================================================================

cSoundInterface = SoundInterface("SoundInterface")
cBark = Bark("Bark")

cSoundInterface.make_sound()
cBark.make_sound()

cSoundInterface = cBark
cSoundInterface.make_sound()

