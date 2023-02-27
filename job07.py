i = 1
while i <= 100:
    if i % 5 == 0 and i % 3 == 0:
        print (str(i) + "FizzBuzz")
    elif i % 5 == 0:
        print (str(i) + "Buzz")
    elif i % 3 == 0:
        print(str(i) + "Fizz")
    i = i + 1
