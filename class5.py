'''
✍️ 연습문제1
'''
class Human:
    def cry(self,tell):
        print(tell *2)

human = Human()
human.cry("엉엉")
human.cry("흑흑")    

'''
✍️ 연습문제2 - 1
'''
class Gugudan:
    def print(self,n):
        self.n = n
        for i in range(1,10):
            print(f"{n}x{i}={n*i}")
m = Gugudan()
m.print(3)

'''
연습문제 2-2
'''
class Car:
	def __init__(self, wheel, price):
		self.wheel = wheel
		self.price = price
		
car = Car(2, 1000)
print(car.wheel)
print(car.price) 	
'''
연습문제 3
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name}({self.age}세) 객체 생성")

    def introduce(self):
        print(f"저는 {self.name}이고, {self.age}세입니다.")

class Person1(Person):
		pass

class Worker(Person):
    def __init__(self, name, age, work):
        super().__init__(name, age)
        self.work = work

    def working(self):
        print(f"{self.work} {self.name}이 일을 합니다.")
worker1 = Worker("김인턴", 25, "개발자")
worker1.introduce()
worker1.working()