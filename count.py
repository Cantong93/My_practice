from itertools import count, product


number = int(input("Enter any number: "))

count = 1
while count <= 10:
    product = count * number
    print(product)
    count = count + 1
    

