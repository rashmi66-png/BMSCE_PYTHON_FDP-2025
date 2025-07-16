class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class student(person):
    def __init__(self,name,age, USN):
        super().__init__(name, age)
        self.USN=USN

    def printdetails(self):
        print(f"student name is {self.name}")
        print(f"student age is {self.age}")
        print(f"student USN is {self.USN}")


s= student("John",23,"123")
s.printdetails()

