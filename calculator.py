def main():
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    print()

    if num2 == 0:
        print("cannot divide by zero.")
    else:
        total = num1 + num2
        diff = num1 - num2
        product = num1 * num2
        quotient = num1 // num2
        print("The sum of {} and {} is {}\n".format(num1, num2, total))
        print("The different of {} and {} is : {}\n".format(num1, num2,diff))
        print("The product of {} and {} is: {}\n".format(num1, num2,product))
        print("the product of {} and {} is: {}\n".format(num1,num2,quotient))





main()

