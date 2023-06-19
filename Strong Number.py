""" Problem Description
The program takes a number and checks if it is a strong number.

Problem Solution
1. Take in an integer and store it in a variable.
2. Using two while loops, find the factorial of each of the digits in the number.
3. Then sum up all the factorials of the digits.
4. Check if the sum of the factorials of the digits is equal to the number.
5. Print the final result.
6. Exit.

Source Code: """

Num=int(input("Enter the number to check:"))
s=0
n= Num
while(Num>0):
    digit=Num%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    s=s+ fact
    Num=Num//10

if(s==n):
    print("Strong Number")
else:
    print("Not a strong number")
