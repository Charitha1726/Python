def outer_function(a, b):
    def inner_function(a, b):
        return a + b
    result = inner_function(a, b)
    return result + 5

# Example usage:
print(outer_function(3, 4))  # Output: 12

