def larger_of_two(x, y):
    return x if x > y else y

def largest_of_three(a, b, c):
    return larger_of_two(larger_of_two(a, b), c)

# Example usage:
print(largest_of_three(10, 20, 15))  # Output: 20


