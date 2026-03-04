marks = float(input("enter Your Score: ")) #taking marks as input and converting it to float
if(80<marks<=100): #checking if the marks are between 80 and 100
    print("Grade A")#printing grade A if the marks are between 80 and 100
elif(60<marks<=80): #checking if the marks are between 60 and 80
    print("Grade B") #printing grade B if the marks are between 60 and 80
elif(40<marks<=60): #checking if the marks are between 40 and 60
    print("Grade c")#printing grade C if the marks are between 40 and 60
else:
    print("Fail")#printing fail if the marks are less than or equal to 40