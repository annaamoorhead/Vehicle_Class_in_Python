#vehicleClass.py


class Vehicle:
    '''
    Vehicle Class
    This class models a vehicle on a used car lot
    Change Order: We need to add maximum speed to the model
    Change Order: We need a way to 'read' maximum speed from the model
    Change Order: Some developers need to use the constructor without having to provide a max speed
    '''
    # Constructor. It's called when... we instantiates an object of vehicle type (will always use __init__)
    def __init__(self, type, max_speed= None):
        '''
        @param type: the kind of vehicle 
        @param max_spped: maximum speed the vehicle can run, defaults to None
        '''
        self.type = type;
        self._thisisprivate = 42 # This a weak attempt to 'support' data hiding
        self.max_speed = max_speed
    # A instance method. It operates an instance of the Vehicle class
    def printType(self):
        print(self.type);
        
    def getSpeed (self):    # 'a getter'
        return self.max_speed

if __name__ == "__main__":
    # Some code to test the class would go here.
    # If there's no code, just pass
    pass
