#.....if else statement practice
marks = int(input("Enter the mark : "))
if marks > 90 :
    print("The grade is A")
elif marks > 80 and marks <=90 :
    print("The grade is B")
elif marks >= 60 and marks <= 80:
    print("The grade is c")
elif marks <60:
    print("The grade is D")
else:
    print("You are Fail")
