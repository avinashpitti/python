def disc_calculator(discount):

    def calculate(price):
        return price -(price * discount/100)
    return calculate

ten_percent=disc_calculator(10)
twenty_percent=disc_calculator(20)

print(ten_percent(100))
print(twenty_percent(200))