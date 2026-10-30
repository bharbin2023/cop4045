class ParkingPermit:
    def __init__(self, name, months_purchased, fee_schedule):
        self.name = name
        self.months_purchased = months_purchased
        self.fee_schedule = fee_schedule
    
    def cost(self)->float:
        raise NotImplementedError
    
    def __str__(self):
        return (f"Name: {self.name}, {self.cost()}")
    
    def __repr__(self):
        return f"ParkingPermit({self.name}, {self.months_purchased}, {self.fee_schedule})"

class StudentPermit(ParkingPermit):
    def __init__(self, name, months_purchased, fee_schedule, vehicles_registered):
        super().__init__(name, months_purchased, fee_schedule)
        self.vehicles_registered = vehicles_registered

    def cost(self):
        if self.vehicles_registered  <= 1:
            return (self.fee_schedule["Student"] * self.months_purchased) 
        return self.fee_schedule["Student"] * self.months_purchased + self.fee_schedule["Cars"] * (self.vehicles_registered -1)

    def __str__(self):
        return f"{self.name} - ${self.cost():.2f}"
                    
        
    def __repr__(self):
        return self.__str__()

class FacultyPermit(ParkingPermit):
    def __init__(self, name, months_purchased, fee_schedule, garage_access):
        super().__init__(name, months_purchased, fee_schedule)
        self.garage_access = garage_access

    def cost(self):
        return (self.fee_schedule["Faculty"] * self.months_purchased) + (self.fee_schedule["Garage"] * self.garage_access)
    
    def __str__(self):
        return f"{self.name} - ${self.cost():.2f}"

    def __repr__(self):
        return f"Faculty({self.name}, {self.months_purchased}, {self.fee_schedule})"
def summarize_list(permits : list[ParkingPermit]):
    revenue = 0
    for i in permits:
        print(i)
        revenue += i.cost()
    return revenue
    

permits = []
if __name__ == '__main__':
    fee_sched = {
        "Faculty" : 40.00,
        "Student" : 25.00,
        "Garage" : 15.00,
        "Cars" : 10.00
    }

    student1 = StudentPermit("James", 9, fee_sched,2)
    student = StudentPermit("Jackie", 9, fee_sched,1)
    faculty1 = FacultyPermit("Christine", 7, fee_sched, True)
    faculty2 = FacultyPermit("Chris", 7, fee_sched, False)

    permits = [student, faculty2, faculty1, student1]

    print(f"Revenue: ${summarize_list(permits): .2f}")
