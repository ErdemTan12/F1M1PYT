import time

factory = ["Auto"]
distribution = []
shop = []
print("factory", factory)
factory.remove("Auto")
time.sleep(1)
print("factory", factory)

distribution.append("Auto")
time.sleep(1)
print("distribution", distribution)
distribution.remove("Auto")
time.sleep(1)
print("distribution", distribution)

shop.append("Auto")
time.sleep(1)
print("shop", shop)
shop.remove("Auto")
time.sleep(1)
print("shop", shop)