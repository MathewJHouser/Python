class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def get_pressure(self):
        return "Tire Pressure: {} psi".format(self.__pressure)

    def pump(self, psi):
        self.pressure += psi


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.status = "Off"

    def start(self):
        self.status = "On"

    def stop(self):
        self.status = "Off"

    def get_state(self):
        return "{} engine is turned {}".format(self.fuel_type, self.status)


class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires


city_tires = Tires(15)
offroad_tires = Tires(18)
electric_engine = Engine("Electric")
petrol_engine = Engine("Petrol")
city_car = Vehicle(123456, electric_engine, city_tires)
fwd_car = Vehicle(654321, petrol_engine, offroad_tires)



