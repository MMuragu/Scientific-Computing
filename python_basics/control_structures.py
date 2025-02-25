def classify_number(num):
    return "Even" if num % 2 == 0 else "Odd"

# Asking the user for an integer input
user_input = int(input("Enter an integer: "))
print(f"The number {user_input} is {classify_number(user_input)}.")


#Uses a for loop to generate a list of even numbers from 1 to 50 and prints the list.
even_numbers = []
for i in range(1, 51):
    if i % 2 == 0:
        even_numbers.append(i)

# Print the list of even numbers
print("List of even numbers from 1 to 50:")
print(even_numbers)



# Use a while loop to print numbers from 10 down to 1 in reverse order
print("Numbers from 10 to 1 in reverse order:")
count = 10
while count >= 1:
    print(count, end=" ")
    count -= 1
print()  