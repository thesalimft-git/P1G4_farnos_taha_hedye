# oop : Object Oriented Programing
# class    ==> map, 
# object   ==> instance
# method   ==> function
# property ==> variable

class Car:
    def __init__(self, model, color, brand):
        self.model = model
        self.color = color
        self.brand = brand
    
    def show_info(self):
        print(self.model, self.brand, self.color)
    
car1 = Car(2025, 'blue', 'mvm')
car2 = Car(2024, 'red', 'pego')
      
car1.show_info()   # 2025 mv blue