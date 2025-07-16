class India:
    def capital(self):
        print("Delhi")

class USA:
    def capital(self):
        print("Washington DC")

objIND=India()
objUSA=USA()

objIND.capital()# same func printing washngton DC here
objUSA.capital()# same func printing newdelhi here


# here in the above program I can say that capital function has become polymorphic in nature---

