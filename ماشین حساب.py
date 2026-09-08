numbers = input("enter two numbers: ")
a, b = numbers.split()

operation = input("enter operation (+, -, *, /): ")

a = int(a)
b = int(b)

if operation == "+":
    print(a + b)
elif operation =="-":
      print(a - b)
elif operation == "*":
     print(a * b)
elif operation == "/":
    if b != 0:
         print(a / b)
    else:
          print("error")
else:
    print("lnvalid operaton")