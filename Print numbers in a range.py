""" Problem Description :
The program takes in the upper limit and prints all numbers within the given range using recursive function.

Problem Solution
1. Define a recursive function.
2. Define a base case for that function that the number should be greater than zero.
3. If number is greater than 0, call the function again with the argument as the number minus 1.
4. Print the number.
5. Exit.

Source Code: """
def num(upper):
    if(upper>0):
        num(upper-1)
        print(upper)
upper=int(input("Enter the upper limit:"))
print(num(upper))
