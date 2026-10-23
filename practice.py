def net_price(price, discount = 0, tax = 0.05):
    return price * (1 - discount) * (1 + tax)

print(net_price(10000, 0.24 , 0))