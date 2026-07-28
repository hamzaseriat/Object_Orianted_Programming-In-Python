import random
import time 


class Car:
    
    def __init__(self, speed, name, model,Car_is_moving):
        self.speed = speed
        self.name = name
        self.model = model
        self.Car_is_moving = Car_is_moving

    def increment_speed(self, amount=1):
        self.speed += amount
        return self.speed
    def Stop_The_car(self):
        self.Car_is_moving = False
        


# Car sınıfından türeyen alt sınıf (Child Class)
class ElectricCar(Car):
    def __init__(self, speed, name, model, battery_capacity):
        # Üst sınıfın (Car) __init__ metodunu çağırarak speed, name ve model'i tanımlıyoruz
        super().__init__(speed, name, model,Car_is_moving=True)
        # Alt sınıfa özgü yeni özellik
        self.battery_capacity = battery_capacity

    # Üst sınıftaki metodu genişletip/ezip (override) super() ile kullanabiliriz
    def increment_speed(self, amount=1):
        # Üst sınıftaki hız artırma mantığını aynen çalıştırıyoruz
        super().increment_speed(amount)
        print(f"{self.name} sessizce hızlandı! Güncel hız: {self.speed}")

    def increment_randomly(self):
        change = random.randint(-15,15)
        new_speed = self.speed + change
        if new_speed >=350:
           self.speed = 350
           print(f"Maksiimum hıza ulaşıldı. {self.speed}km/s")
        elif new_speed <= 0:
           self.speed = 0
           self.Stop_The_car()
        else:
           self.speed = new_speed
           print(f"Yeni araç hızı: {self.speed} km/s")
        return self.speed
           

        

# Kullanım
tesla = ElectricCar(200, "Tesla Model S", "P100D", "100 kWh")

print(tesla.name)            # Tesla Model S
print(tesla.battery_capacity) # 100 kWh

tesla.increment_speed(15)    # super() sayesinde hem hızı artırır hem de yeni mesajı yazar
while tesla.Car_is_moving:
  tesla.increment_randomly()
  time.sleep(6)

