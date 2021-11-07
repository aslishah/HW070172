# Programming exercisesfor chapter 2 (Python)

# 1. Modify the programme convert.py to print an introduction

# convert.py

def main():
    print(" This program converts Celsius temps to Fahrenheit")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()

# 2. A statement at the end to pause the programme to allow you to read.
def main():
    print(" This program converts Celsius temps to Fahrenheit")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    input("Press the <ENTER> key to quit")

main()

# 3. Modify the avg.py to find the average of three exam scores. 

def main():
    print("This program computes the average of two exam scores.")

    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the scores is:", average)

main()

# 4.  Modify convert programme with a loop torun 5 times

def main():
    for i in range (5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
        print()

main()

# 5 modify the covnert programme so that it prints Celsius and F every 10 degrees from 10  to 100

def main():
    print ("This programme converts a range of C degrees into F")
    print()
    print ("Celsius", "Fehrenheit")
    for celsius in (10,20,30,40,50,60,70,80,90,100): #I am still not sure abt how to write this with range. 
        fahrenheit = 9/5 * celsius + 32
        print("______________")
        print(celsius, "\t", "|", fahrenheit)
        print()

main()

# 6. Modify  the futval.py programme to enter the years as well.

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years for your investment: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print(f"The value in {years} years is:", principal)

main()

# 7. This programme calculates total investment of fixed amount over years

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    investment = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years for your investment: "))

    for i in range(years):
        investment = investment * (1 + apr)
        total_investment=investment * years

    print(f"Total investment in {years} years is:", total_investment)

main()

# 8. Will do this later and seubmit before class. I did't really understand the calculation. 
# 9. This programme converts F to Celsius degrees
def main():
    print(" This program converts  Fahrenheit to  Celsius")
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit - 32)*5/9
    print("The temperature is", celsius, "degrees Celsius.")

main()

# 10. def main():
    print(" This program converts km to  miles")
    kilometers = eval(input("What is the distance in km? "))
    miles = kilometers*0.62
    print("The distance in miles is",  miles, "miles.")

main()

# 11. A programme  to convert  kilograms to  pounds
def main():
    print(" This program converts kilograms to  pounds")
    kilograms = eval(input("What is the weight in kg? "))
    pounds = kilograms/0.454
    print("The weight in pounds is",  pounds, "pounds.")

main()
# 12.  Write a caclulator that that allows user to type a mathematical expression

def main():
    print()  #print empty lines with print() function
    print("This is a calculator") #This statement tells  what your programme  does
    print() #another blank line
    for i in range (3): #the  loop that defines how many mathematical expression you can run
        mathem_expression = eval(input("White the mathematical expression here: ")) # you are already familiar with this; in above cases you  entered numbers, here you are adding a mathmatical expression (summation,deletetion etc) which will also be evaluated with the function eval()
        print(mathem_expression)   #Print the result of the evaluation of your mathematical expression
        #print(input,"=",mathem_expression) I wanted to write another line to print  the mathematical expression on the same line too, but didn't know how  to do it
main()
