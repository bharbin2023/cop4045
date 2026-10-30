class ParkingPermit:
    def __init__(self, name, months_purchased, fee_schedule):
        self.name = name
        self.months_purchased = months_purchased
        self.fee_schedule = fee_schedule
    
    def cost(self):
        pass

class StudentPermit(ParkingPermit):
    def __init__(self, name, months_purchased, fee_schedule, vehicles_registered):
        super().__init__(name, months_purchased, fee_schedule)
        self.vehicles_registered = vehicles_registered

    def cost(self):
        return (25.00 * self.months_purchased) + (10.00 * self.vehicles_registered)

class FacultyPermit(ParkingPermit):
    def __init__(self, name, months_purchased, fee_schedule, garage_access):
        super().__init__(name, months_purchased, fee_schedule)
        self.garage_access = garage_access

    def cost(self):
        return (40.00 * self.months_purchased) + (15.00 * self.garage_access)
