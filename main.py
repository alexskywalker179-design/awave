from entities import Food, Socket
def Microwave(Food):
    food = [
        "Суп",
        "Плов",
        "Пицца",
        "Хот_дог",    
        "Шаурма",
        "Стейк",
        "Курица",]
def Microwave(Socket):
   socket = [
       "220V",
       "110V",
       "12V",]
def Microwave(temperature):
    temperature = [
        "21",
        "50",
        "100",
        "150",
        "200",]
    for t in temperature:
        if t > 200:
            print("Микровалновка перегрелась! Температура выше 200 градусов!")
def Microwave(mode):
    mode = [
        "Разморозка",
        "Подогрев",
        "Жарка",
        "Выпечка",]
def Microwave(capacity_limit):
    capacity_limit = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",]
def Voltage(Socket):
    socket = [
        "220V",]
    for v in socket:
        if v != "220V":
            print("Микровалновка не поддерживает данное напряжение! Пожалуйста, используйте 220V.")
def Button(clicked):
    clicked = (
        "Вкл", # TODO: баг, это нужно перенести выше
        "Выкл")
    if clicked == "Вкл":
        print("Микровалновка включена!")
    else:
        print("Микровалновка выключена!") 
    two_clicked = []
    if two_clicked:
        print(f"Выбор блюда: {Food}")
def Microwave(door):
    door = [
        "Открыта",
        "Закрыта",]
    if door == "Открыта":
        print("Микровалновка открыта!")
    else:
        print("Микровалновка закрыта!")        
    
    

