age = int(input("enter Your Age: "))#taking age as input and converting it to integer

if(age<=5):#checking if the age is less than or equal to 5
    print("Toodler")#printing Toddler if the age is less than or equal to 5 

elif(5<age<=12):#checking if the age is between 5 and 12
    print("You are Child")# printing Child if the age is between 5 and 12

elif(12<age<=19):#checking if the age is between 12 and 19
    print("Teenager")#printing Teenager if the age is between 12 and 19

elif(19<age<=50):#checking if the age is between 19 and 50
    print("Adult")#printing Adult if the age is between 19 and 50
    
else:
    print("senior citizen")#printing senior citizen if the age is greater than 50