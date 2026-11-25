
class MicrowaveEntity:
    type_of_entity = None
    
    def __init__(self):
        type_of_entity = self.type_of_entity
    
class Socket(MicrowaveEntity):
    voltage = 0,
    
    def __init__(self):
        voltage = self.voltage


class Food(MicrowaveEntity):
    name = None,
    quantity = 0
    temperature = 21
    
    def __init__(self):
        name = self.name
        quantity = self.quantity  
        temperature = self.temperature

class Microwave(MicrowaveEntity):
    model = None,
    capacity_limit = 10,
    mode = None,
    foods = []    
    
    def __init__(self):
        model = self.model
        capacity = self.capacity
        foods = self.foods
     
    def put_to_microwave(self, food):
        if self.capacity_limit<=0:
            self.foods.append(food)
            self.capacity_limit -= 1
            print(f"{food}Еда успешно помещена в микровалновку!")
        else: 
            print(f"Нет свободного места для {food}!")
        
    def freeze(self):
        for f in self.foods:
            if f["temperature"] > 200:
                print("Предупреждение о перегреве микровалновки. Ваша температура выше положенных на " + f["temperature"]-200)
                f["temperature"] = 200
            
            