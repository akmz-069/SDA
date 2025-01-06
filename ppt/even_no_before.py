#program before modifying
def sum_even_numbers(nums):
    even_numbers = [num for num in nums if num % 2 == 0]    # Inefficient: Creates a new list unnecessarily
    return sum(even_numbers)

nums = range(1, 100)
print(sum_even_numbers(nums))  # Calculates the sum of all even numbers
