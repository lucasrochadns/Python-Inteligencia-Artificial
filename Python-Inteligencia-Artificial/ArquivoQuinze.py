
#Multiple Inheritance
class Swimmer:
    def swim(self):
        return "Swim in the pool"

class Cyclist:
    def cycling(self):
        return "Cycling on the road"


class Triathlete(Swimmer, Cyclist):
    def running_marathon(self):
        return "Running in the marathon"


#Test Inheritance Multiple
athlete = Triathlete()
print(f" Triathlete: {athlete.running_marathon()}, Swimmer: {athlete.swim()}, Cyclist: {athlete.cycling()}")