price = float(input("Enter price: "))
vip = input("Are you VIP: ")
express_delivery = input("Do you want express delivery : ")
is_weekend = input("Is it weekend : ")

price_delivery = 0
total_price = 0
if price < 100:
    price_delivery = 5
    if vip == "yes":
        price_delivery = 2
    if express_delivery == "yes":
        price_delivery +=10

if is_weekend == "yes" and express_delivery == "yes":
    price_delivery += 3

print(price_delivery)
print(price_delivery + price)

