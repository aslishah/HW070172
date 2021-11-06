# Homework 1 
### Exercise  1
def hello():
    print('Hello, world')
    print('Hello','world!')
    print(3)
    print(3.0)
    print(2+3)
    print(2.0+3.0)
    print("2"+"3")
    print("2+3=", 2+3)
    print (2*3)
    print(2**3)
    print(7/3)
    print (7//3)
    

    

### Exercise 2: Chaos programme
def main():
    print("This programme illustrates a chaotic funtion")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in  range (10):
        x = 3.9*x*(1-x)
        print(x)
        
main()

### Exercise 3: modified chaos programme
  
def main():
    print("This programme illustrates a chaotic funtion")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in  range (10):
        x = 2.0*x*(1-x)
        print(x)
        
main()

### The main difference seems to be that when used 3.9 the result is  more chaotic. 
### When used 2.0 many of results are identical.

#Exercise 4: 20 values

def main():
    print("This programme illustrates a chaotic funtion")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in  range (20):
        x = 2.0*x*(1-x)
        print(x)
        
main()

### Exercise 5. Modify to user-defined number of values

n= eval(input("How many numbers should I  print? "))
def main():
    print("This programme illustrates a chaotic funtion")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in  range (n):
        x = 2.0*x*(1-x)
        print(x)
        
main()

### Exercise 6. Different formulae

def main():
    print("This programme illustrates a chaotic funtion")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in  range (100):
        x = 3.9*x*(1-x)
        print(x)
main()     

def main():
    print("This programme illustrates a chaotic funtion")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in  range (100):
        x = 3.9*(x-x*x)
        print(x)
main()

def main3():
    print("This programme illustrates a chaotic funtion")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in  range (100):
        x = 3.9*x-3.9*x*x
        print(x)
main3()

#Explanation: Looks like a list of 100 random numbers between 0 and  1

### Exercise 7. Different formula
def main():
    print("This program illustrates a chaotic function")
    x1 = eval(input("Enter the first seed between 0 and 1: "))
    x2 = eval(input("Enter the second seed between 0 and 1: "))
    print()
    print("input", x1, x2)
    for i in range(10):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print("      ", x1, x2)

main()
