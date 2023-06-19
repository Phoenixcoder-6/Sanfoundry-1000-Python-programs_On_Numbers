""" Armstrong Number in Python: Armstrong Number is an integer such that the sum of the cubes of its digits is equal to the number itself. Armstrong numbers are 0, 1, 153, 370, 371, 407, etc.

Formula to calculate Armstrong Number:
wxyz = pow(w,n) + pow(x,n) + pow(y,n) + pow(z,n)


Problem Description :
Write a Python Program to check if a number is an Armstrong number. If the number is an Armstrong then display “it is an Armstrong number” else display “it is not an Armstrong number”.

Problem Solution :
1. Take in an integer and store it in a variable.
2. Convert each digit of the number to a string variable and store it in a list.
3. Then cube each of the digits and store it in another list.
4. Find the sum of the cube of digits in the list and check if it is equal to the original number.
5. Print the final result.
6. Exit.

Source Code: """

num=int(input("Enter any integer number:"))
a=list(map(int,str(num)))
b=list(map(lambda x:x**3,a))
sum1 = sum(b)

if(sum1==num):
    print("Armstrong Number")
else:
    print("Not an armstrong number")
