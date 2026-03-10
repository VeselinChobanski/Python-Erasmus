import math
input = list(input("Въведи уравнение: ").split(" "))

root = ()
if int(input[0]) == 0:
    print("Special case")
else:
    d = -pow(int(input[1]),2) + 4 * (int(input[0] * int(input[2])))
    if d == 0:
        root = -int(input[1] / 2 * int(input[0] ))
        print(f"one root {root} ")
    elif d > 0:
        root = ((-input[1] + math.sqrt(d)) /  (2 * int(input[0] )),(-input[1] - math.sqrt(d)) /  (2 * int(input[0] ) ))
        print(f"two results : result1{root}")
