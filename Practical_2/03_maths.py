import math                          #importing math module to perform mathematical operations
a = int(input("Enter the Number: ")) #taking number as input
if(0<a<10):                           #checking if the number is a single digit number
    print("square of number is:",a**2) #calculating the square of the number and printing the result
elif(10<=a<100):                       #checking if the number is a two digit number
    print("square root of number is:",math.sqrt(a)) #calculating the square root of the number using math.sqrt() function and printing the result
else:   
    print("cube root of number is:",a**(1/3)) #calculating the cube root of the number and printing the result