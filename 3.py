import random
class Human:
    def __int__(self,name="Human", job=None, home=None, car=None):
        self.name=name
        self.money=100
        self.gladness=50
        self.satietly=50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        pass
    def get_car(self):
        pass
    def get_job(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass
    def shopping(self, manage):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
    def to_repair(self):
        pass
    def days_indexes(self, day):
        pass
    def is_alive(self):
        pass
    def live(self, day):
        pass
class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel=brand_list[self.brand]["fuel"]
        self.strength=brand_list[self.brand]["strength"]
        self.consumption=brand_list[self.brand]["consumption"]
    brands_of_car={"Toyota Crown S170 Royal Saloon":{" fuel": 70, "consumption":12.2, "strength":220},
                    "BMW E38 750il 95":{" fuel":95, "consumption":15.2, "strength":3},
                   "Lexus": {" fuel":70, "consumption":11.5, "strength":264},
                   "Mercedes":{" fuel":62, "consumption:":8.7, "strength":150},}
    def drive(self):
        if self.strength>0 and self.fuel>=self.consumption:
            self.fuel-=self.consumption
            self.strength-=1
            return True
        else:
            print("the car cannot move")
            return False
class House:
    def __int__(self):
        self.mess=0
        self.food=0

class Job:
    def __int__(self,job_list):
        self.job=random.choice(list(job_list))
        self.salary=job_list[self.job]["salary"]
        self.gladness_lass=job_list[self.job]["gladness_less"]
    job_list={
        "Java developer":{"salary": 50, "gladness_less": 10},
        "Python developer":{"salary": 40, "gladness_less": 3},
        "C++ developer":{"salary": 45, "gladness_less": 25},
        "Rust developer":{"salary": 70, "gladness_less": 1},
        "C# developer":{"salary": 90, "gladness_less": 2}}
    def get_home(self):
        self.home=House
    def get_car(self):
        self.car=Auto(brands_of_car)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job=Job(job_list)