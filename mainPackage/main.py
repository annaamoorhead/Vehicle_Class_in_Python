#main.py

from vehiclePackage.vehicleClass import *

if __name__ == "__main__":
    # Instantiate an object of type Vehicle
    myCorvette = Vehicle("Car", 120)     # Trigger a call constructor
    myCorvette.printType()               # invoke the method on the object
    
    # Invoke the getter from Maximum speed, store the return value in a variable and print
    maximum_speed = myCorvette.getSpeed()
    print ("Maximum speed:", maximum_speed)
    
    # Instantiate another Vehicle object
    myJaguar = Vehicle("Car")

    # Want a list of 3 vehicles: car, boat, Space Ship
    # You can pick the names and properties
    # Want some friendly output to demo work
    '''
    myCar= Vehicle("Car")
    myBoat = Vehicle ("Boat")
    mySpaceShip= Vehicle ("SpaceShip")
    myVehicleList = myCar.printType(), myBoat.printType(), mySpaceShip.printtype()
    print 
    '''
    
    myVehicles = [  Vehicle("Toyota Avalon", 120)
                  , Vehicle ("Sailboat", 20)
                  , Vehicle("Falcon Heavy",4000)]
    for vehicles in myVehicles:
        vehicles.printType()
        print (vehicles.getSpeed())
        