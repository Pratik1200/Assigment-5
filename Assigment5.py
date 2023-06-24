# Take input from the user of 5 numbers
numbers = []
for _ in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Calculate the sum of all the elements in the list
sum_of_numbers = sum(numbers)
print("Sum:", sum_of_numbers)

# Find the smallest number
smallest_number = min(numbers)
print("Smallest number:", smallest_number)

# Find the largest number
largest_number = max(numbers)
print("Largest number:", largest_number)

# Display list in ascending order
ascending_order = sorted(numbers)
print("Ascending order:", ascending_order)

# Display list in descending order
descending_order = sorted(numbers, reverse=True)
print("Descending order:", descending_order)

# Convert list into tuple
numbers_tuple = tuple(numbers)
print("Tuple:", numbers_tuple)

# Delete the list
del numbers
print("List deleted.")
