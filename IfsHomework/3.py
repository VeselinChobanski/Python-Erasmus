gender = input("Enter gender: ")
age = int((input("Enter age: ")))
weight = int(input("Enter weight: "))
length = int(input("Enter length: "))
activity = int(input("Activity: "))
calories = int(input("Enter calories: "))

recomended_calories = 0.00
if gender == "male":
    recomended_calories = 10* weight + 6.25 * length - 5 * age +5
elif gender == "female":
    recomended_calories = 10 * weight + 6.25 * length - 5 * age -161

if activity == 1:
    recomended_calories *= 1.2
elif activity ==2:
    recomended_calories *= 1.55
elif activity == 3:
    recomended_calories *= 1.9

print(f"recomended {recomended_calories}")
if recomended_calories - calories > 0:
    print(f"{abs(recomended_calories - calories)} по малко ")
elif calories - recomended_calories < 0:
    print(f"{abs(recomended_calories - calories)} повече ")

print(f"recomended {recomended_calories}")