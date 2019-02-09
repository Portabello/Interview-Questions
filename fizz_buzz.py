

def fizzbuzz():
    for x in range(1,101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)

def fizzbuzz_no_rechecking():
    for x in range(1,101):
        output = ""
        if x % 3 == 0:
            output += "Fizz"
        if x % 5 == 0:
            output += "Buzz"
        if output == "":
            output = str(x)
        print(output)

fizzbuzz_no_rechecking()
