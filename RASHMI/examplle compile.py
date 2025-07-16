class mom:
    def cook(self):
        print("Indian")

class Daughter(mom):
    # pass
# can be used if you don't want to give method
    def cook(self):
        print ("Chinese")

m=mom()
d= Daughter()

m.cook()
d.cook() # cook function is overhidden
# if inheritance is not there here then it is not called over hiding