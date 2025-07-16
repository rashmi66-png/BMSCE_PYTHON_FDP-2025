class parent:
    def __init__(self):
        print("This is parent constructor")

class child(parent):
    def __init__(self):
        super().__init__() # calls parent constructor here
        print("This is child constructor")

c= child()