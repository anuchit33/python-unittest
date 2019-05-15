

class Lift:
    status = 'STOP'
    def __init__(self,current_floor=1,floor_max=100,floor_min=1,weight_max=1000):
        self.current_floor = current_floor
        self.floor_max = floor_max
        self.floor_min = floor_min
        self.weight_max = weight_max
        self.beep = False

    def getCurrentFloor(self):
        return self.current_floor
    
    def callAt(self,floor):
        self.call_at = floor
        if not self.is_valid_floor(floor):
            self.status = 'STOP'
        elif self.current_floor > floor:
            self.status = 'DOWN'
        elif self.current_floor < floor:
            self.status = 'UP'
        else:
            self.status = 'STOP'

        self.current_floor = floor
        
    def start(self,floor,weight=0):
        self.selected = floor
        self.weight = weight

        self.beep = weight > self.weight_max
        if not self.is_valid() or self.current_floor == floor:
            self.status = 'STOP'
        elif self.current_floor > floor:
            self.status = 'DOWN'
        elif self.current_floor < floor:
            self.status = 'UP'
        self.current_floor = floor

    def getStatus(self):
        return self.status
    

    def getBeep(self):
        return self.beep

    def is_valid_floor(self,floor):
        return floor<=self.floor_max and floor >=self.floor_min
    def is_valid(self):
        return self.selected < self.floor_max and self.weight<=self.weight_max