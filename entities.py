
class MicrowaveEntity:
    type_of_entity = None
    
    def __init__(self):
        self.type_of_entity = self.type_of_entity
    
class Socket(MicrowaveEntity):
    model = None,
    voltage = 0
    
    def __init__(self, model, voltage):
        self.voltage = voltage
        self.model = model

class Food(MicrowaveEntity):
    name = None,
    quantity = 0
    temperature = 21
    
    def __init__(self, name, quantity, temperature):
        self.name = name
        self.quantity = quantity
        self.temperature = temperature

class Microwave(MicrowaveEntity):
    model = None,
    capacity_limit = 10,
    mode = None,
    foods = []    
    
    def __init__(self, model, mode, capacity_limit, foods):
        self.model = model
        self.capacity_limit = capacity_limit
        self.mode = mode
        self.foods = foods
     
    def put_to_microwave(self, food):
        if self.capacity_limit <= 0:
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
            
            