class Computer:
    def __init__(self):
        super().__init__()
        self.memory=128
class Display:
    def __init__(self):
        super().__init__()
        self.resolution="4k"

class SmartPhone(Display,Computer):
    def print_info(self):
        print(self.resolution)
        print(self.memory)
iphone=SmartPhone
iphone.print_info()