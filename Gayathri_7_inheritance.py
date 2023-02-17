class Jets:
    model = None
    country = 0

    def __init__(self,name,country):
        self.type = "Jet"
        self.area = "Air"
        self.name = name
        self.origin = country

class F14(Jets):

    def __init__(self):
        self.name = "F14"
        self.origin = "USA"
        self.engine = 2
        self.seat = 2
        self.tail = 2
        # these values are set as default values for instances created for jet class
        super().__init__(self.name,self.origin)
        # to access attributes in Jet(Base) class

    def __str__(self):
        return (f" Object belongs to class {self.__class__.__name__}\n"
              "Attributes of this class :\n"
              "Name   : {self.name}\n"
              "Origin : {self.origin}\n"
              "Type   : {self.type}\n"
              "Area   : {self.area}\n"
              "Engine : {self.engine}\n"
              "Seat   : {self.seat}\n"
              "Tail   : {self.tail}\n")

        # to get the attributes of class

f1 = F14()
print(f1)



