num = float(input("digite um valor inteiro"))
num = int(num)
if(num%3 == 0 and num%5 != 0):
    print("Fizz")
elif(num%5 == 0 and num%3 != 0):
    print("Buzz")
elif(inteiro%3 == 0 and inteiro %5 == 0):
    print("FizzBuzz")
else:
    print(num)
