class ParkingPermit:
    def __init__(self, name, months_purchased, fee_schedule):
        self.name = name
        self.months_purchased = months_purchased
        self.fee_schedule = fee_schedule
    
    def cost(self):
        pass
    
    def __str__(self):
        return "Name: {}, Months Purchased: {}, Fee Schedule: {}"
    
    def __repr__(self):
        return "ParkingPermit({},{},{})"

class StudentPermit(ParkingPermit):
    def __init__(self, name, months_purchased, fee_schedule, vehicles_registered):
        super().__init__(name, months_purchased, fee_schedule)
        self.vehicles_registered = vehicles_registered

    def cost(self):
        if self.vehicles_registered  <= 1:
            return (self.fee_schedule["Student"] * self.months_purchased) 
        return self.fee_schedule["Student"] * self.months_purchased + self.fee_schedule["Cars"] * self.vehicles_registered

class FacultyPermit(ParkingPermit):
    def __init__(self, name, months_purchased, fee_schedule, garage_access):
        super().__init__(name, months_purchased, fee_schedule)
        self.garage_access = garage_access

    def cost(self):
        return (self.fee_schedule["Faculty"] * self.months_purchased) + (self.fee_schedule["Garage"] * self.garage_access)

    

