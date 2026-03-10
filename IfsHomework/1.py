apples = int(input("Apples: "))
babanas = int(input("Babanas: "))
sandwitches = int(input("Sandwitches: "))
pizza = int(input("Pizza: "))

total_calories = (apples* 52) + (babanas * 89) + (sandwitches * 250) + (pizza * 285)

if total_calories <= 2000:
    print("Normal")
else:
    print("Over")