maximum = int(input(" Please enter the maximum number: "))
total =0

for num in range(1, maximum + 1):
    if(num % 2 == 0):
        print("{0}".format(num))
        total = total + num

print("The total is: {0} = {1}".format(num, total))