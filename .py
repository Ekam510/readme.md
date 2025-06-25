   # Task 1: Check if a Number is Even or Odd
   number = int(input("Enter an integer: "))
   
   if number % 2 == 0:
       print(f"{number} is even.")
   else:
       print(f"{number} is odd.")


   # Task 2: Sum of Integers from 1 to 50
   total_sum = 0
   
   for number in range(1, 51):
       total_sum += number
   
   print(f"The sum of integers from 1 to 50 is: {total_sum}")
   
