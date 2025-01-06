#program after modifying
def sum_even_numbers(nums):
    return sum(num for num in nums if num % 2 == 0)

nums = range(1, 100)
print(sum_even_numbers(nums))  # Calculates the sum of all even numbers