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
        self._name = "F14"
        self._origin = "USA"
        self._engine = 2
        self._seat = 2
        self._tail = 2
        # these values are set as default values for instances created for jet class
        super().__init__(self._name,self._origin)
        # to access attributes in Jet(Base) class

    def engine(self):
        return self._engine
    
    
    def seat(self):
        return self._seat
    
    
    def tail(self):
        return self._tail

f1 = F14()
print(f1.engine())
print(f1.seat())
print(f1.tail())



