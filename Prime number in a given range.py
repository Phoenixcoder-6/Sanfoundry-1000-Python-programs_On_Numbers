# First, we will take the input:  
lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
print("The prime numbers are:")

for numbers in range(lower_value, upper_value+1):
    if numbers >1:
        for i in range(2, numbers):
            if (numbers % i == 0):
                break
        else:
            print(numbers)



