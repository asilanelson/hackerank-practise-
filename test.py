import math

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def calculate_prime_numbers(limit):
    prime_numbers = []
    for num in range(2, limit+1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers

def calculate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

def perform_heavy_computations():
    for _ in range(10):
        calculate_factorial(500)
        calculate_prime_numbers(500)
        calculate_fibonacci_sequence(50)

perform_heavy_computations()
