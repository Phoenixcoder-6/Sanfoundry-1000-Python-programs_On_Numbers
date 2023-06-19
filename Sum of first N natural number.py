""" Problem Description
The program takes in the the number of terms and finds the sum of first N Natural Numbers.

Problem Solution:
1. Create a variable and store the number of terms in that variable
2. Create another variable to store the summation
3. run a for loop to sum each and every term 
4. Print the result
5.Exit

Source Code: """

N= int(input("Enter the term:"))
sum=0
for i in range(1,N+1):
    if(N>1):
        sum=sum+i

print("The sum is:",sum)
