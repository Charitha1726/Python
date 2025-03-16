def sum_of_numbers(*args):
    return sum(args)

def product_of_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Example usage:
print(sum_of_numbers(1, 2, 3, 4))  # Output: 10
print(product_of_numbers(1, 2, 3, 4))  # Output: 24

