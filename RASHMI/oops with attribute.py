class student:
    def __init__(self, Name, USN):
        self.Name = Name
        self.USN = USN
#  create a class, assign attriabutes

    def printDetails(self):
        print(f"Name is {self.Name}")
        print(f"USN is {self.USN}")
#create method

s1=student("Rashmi", 123)
s2=student("abhi", 456)
s1.printDetails()
s2.printDetails()
#object created 