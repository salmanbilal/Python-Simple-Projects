
# Calculator

"""
About:
Date: 30/05/2021
Author: Salman Bilal
https://twitter.com/salmanb34055398
"""

import math as mathematics

from random import randint

# Operations

operations = """===========================\n"+" for Addition;\n"-" for Subtraction;\n"*" for Product;\n"/" for Division;
"s" for Sin in Trignometry;\n"t" for Tan in Trignometry;\n"c" for Cos is Trignometry;\n"*2" for Square;\n"*3" for Cube;
"**" for Specified Power;\n"/2" for Square Root;\n"r" for getting random number between Specified Numbers;
"0" to break the loop
==========================="""

# Creating the Function

# Don't know why......

def calc():

    # Creating a History file

    # Just to store History's data

    with open("history.txt", "a") as history:

        # To run the loop until we Type 0

        while True:

            # Printing Operations

            print("Operations:\n" + operations)

            # Telling which operation should I perform

            operation_for_performing = input("Which operation would you Like to perform:\n\t")

            # Box where calculation occurs

            calculation_box = []

            # for Addition

            if operation_for_performing == "+":
                
                numbers = ""

                # While numbers doesn't equal 0 continue suming all numbers

                while numbers != 0:

                    numbers = int(input("Number(Type 0 if you want to Stop the Loop): "))
                    
                # Appending and Running of loop

                    if numbers == 0:

                        break
                
                    else:

                        calculation_box.append(numbers)

                        continue

                # Iterating in Calculation_Box [Array] and Finding all number's sum total    

                j = 0

                for i in calculation_box:

                    i += j

                    j = i

                    continue

                # Blocking of Error

                try:

                    print(f"Sum of all the numbers is {i}")
                
                except Exception as err:

                    print(err)

                # Appending Data in History File

                history.write(f"{i}\n")

                continue

            # for Product

            elif operation_for_performing == "*":
                
                numbers = ""
                
                # While numbers doesn't equal 1 continue multipling all numbers

                while numbers != 0:

                    numbers = int(input("Number(Type 1 if you want to Stop the Loop): "))

                # Appending and Running of loop

                    if numbers == 1:

                        break
                    
                    else:

                        calculation_box.append(numbers)

                        continue

                # Iterating in Calculation_Box [Array] and Finding all number's product total

                j = 1

                for i in calculation_box:

                    i = i * j

                    j = i

                    continue

                # Blocking of Error

                try:

                    print(f"Product of all the numbers is {i}")

                except Exception as err:

                    print(err)

                # Appending Data in History File

                history.write(f"{i}\n")

                continue

            # for finding Square

            elif operation_for_performing == "*2":
                
                power = lambda num: num * num

                res = power(int(input("Number: ")))

                print(f'Square of given number is {res}')

                # Appending Data in History File

                history.write(f"{res}\n")

                continue
            
            # for finding Cube

            elif operation_for_performing == "*3":
                
                power = lambda num: num * num * num

                res = power(int(input("Number: ")))
            
                print(f'Cube of given number is {res}')

                # Appending Data in History File

                history.write(f"{res}\n")

                continue

            # for finding Square Root

            elif operation_for_performing == "/2":
                
                num = int(input("Number: "))

                res = mathematics.sqrt(num)
            
                print(f"Square Root of given number is {res}")

                # Appending Data in History File
                history.write(f"{res}\n")

                continue

            # for finding Specific Power of Specific Number

            elif operation_for_performing == "**":
                
                power = lambda number, root: number ** root

                res = power(int(input("Number: ")), int(input("With the Power of: ")))
            
                print(f"Given Number to the power of Given Power is equal to {res}")

                # Appending Data in History File

                history.write(f"{res}\n")

                continue

            # for finding Tan in Trignometry

            elif operation_for_performing == "t":
                
                num = int(input("Number: "))

                res = mathematics.tan(num)
            
                print(f"Tan of given number is {res}")

                # Appending Data in History File

                history.write(f"{res}\n")

                continue

            # for finding Cos in Trignometry

            elif operation_for_performing == "c":
                
                num = int(input("Number: "))

                res = mathematics.cos(num)
            
                print(f"Cos of given number is {res}")

                # Appending Data in History File

                history.write(f"{res}\n")

                continue

            # for finding Sin in Trignometry

            elif operation_for_performing == "s":
                
                num = int(input("Number: "))

                res = mathematics.sin(num)
                
                print(f"Sin of given number is {res}")

                # Appending Data in History File

                history.write(f"{res}\n")

                continue

            # for getting Random Number between Specified Numbers

            elif operation_for_performing == "r":

                start_num = int(input("Numbers from where should we start: "))

                end_num = int(input("Numbers from where should we end: "))

                res = randint(start_num, end_num)
                
                print(f"Random Number from {start_num} to {end_num} is {res}")

                # Appending Data in History File

                history.write(f"{res}\n")

                continue

            # for Division
            elif operation_for_performing == "/":
                
                num1 = int(input("Number to Divide: "))

                num2 = int(input("Divided by: "))

                res = num1 / num2

                print(f"By Dividing these Two Numbers we get : {res}")

                print("Note: if you divide multiple numbers re-run the code")

                # Appending Data in History File

                history.write(f"{res}\n")

                continue

            # for Subtraction

            elif operation_for_performing == "-":
                
                numbers = ""

                # While numbers doesn't equal 0 continue subtracting all numbers

                while numbers != 0:

                    numbers = int(input("Number(Type 0 if you want to Stop the Loop): "))
                    
                # Appending and Running of loop

                    if numbers == 0:

                        break

                    else:

                        calculation_box.append(numbers)

                        continue

                # Iterating in Calculation_Box [Array] and Finding all number's sum total    

                j = 0

                for i in calculation_box:

                    i -= j

                    j = i

                    continue

                # Blocking of Error

                try:

                    print(f"By Subtractiing all the numbers we get: {i}")

                except Exception as err:

                    print(err)

                # Appending Data in History File

                history.write(f"{res}\n")

                continue

            # Break the Loop

            elif operation_for_performing == "0":

                print("Thank You!")

                break

            # "Not such operation found" Message

            else:

                print("Not Such Operation Found")

                continue


# Calling the Function

# To run all above things

# Using Try-Except to check what is wrong in our code

try:

    calc()

except Exception as err:

    print(err)
