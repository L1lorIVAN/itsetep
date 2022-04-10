import random
class Student:
    def __init__(self,name):
        self.name = name
        self.gladness = 5.0
        self.progress = 0
        self.reputation = 0
        self.money = 50
        self.alive = True
    def to_study(self):
        print("time to study")
        self.progress+=0.12
        self.gladness-=1

    def teacher_test(self):
        print("Time to test")
        if self.progress > 2:
            self.progress+=1
            self.gladness+=8
            self.reputation+=8
        elif self.progress < 2:
            self.progress-=0.2
            self.gladness-=10
            self.reputation-=3
    def fight(self):
        print("Time to FIGHT")
        live_cube = random.randint(1,2)
        if live_cube==1:
            print("U win")
            self.reputation+=6
            self.gladness+=10
        elif live_cube==2:
            print("U lose")
            self.reputation-=4
            self.gladness-=7
    def to_chill(self):
        print("Rest time")
        self.gladness+=5
    def go_Dining_room(self):
        print("time to lunch")
        self.gladness+=6
    def is_live(self,):
        if self.progress < -0.5:
            print("Cast out....")
            self.alive=False
        elif self.reputation < -14:
                print("Lox")
                self.alive = False
        elif self.gladness < -15:
            print("depresion")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness={self.gladness}")
        print(f"Progress={round(self.progress,2)}")
        print(f"Money={self.money}")
        print(f"Repution={self.reputation}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "live"
        print(f"{day:=^50}")
        self.end_of_day()
        live_cube= random.randint(1, 5)
        if live_cube==1:
            self.to_study()
        elif live_cube==2:
            self.go_Dining_room()
        elif live_cube==3:
            self.to_chill()
        elif live_cube==4:
            self.fight()
        elif live_cube==5:
            self.teacher_test()
nick=Student(name="Pablo")
for day in range(60):
    if nick.alive==False:
        break
    nick.live(day)