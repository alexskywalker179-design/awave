from entities import Socket, Food, Microwave

my_socket = Socket(model="VGH-30", voltage="220V")
food = Food("Sour cream", 2, 30)
foods = []
foods.append(food)
my_microwave = Microwave("LG", 7, "Подогрев", foods)
print(foods[0].name)

print(my_microwave.model)
print(my_socket.voltage)
my_microwave.put_to_microwave(food)

