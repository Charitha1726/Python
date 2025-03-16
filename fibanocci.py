def fibonacci(n_terms, a=0, b=1, count=0):
    if count < n_terms:
        print(a, end=" ")
        fibonacci(n_terms, b, a + b, count + 1)

# Example usage:
fibonacci(5)  # Output: 0 1 1 2 3

