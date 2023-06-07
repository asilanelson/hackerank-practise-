def calculate_pi(num_terms):
    pi = 0
    sign = 1
    for i in range(num_terms):
        term = sign / (2 * i + 1)
        pi += term
        sign *= -1
    return pi * 4

num_terms = int(input("Enter the number of terms to calculate pi: "))
print("Calculating pi with", num_terms, "terms...")
print("Approximated value of pi:", calculate_pi(num_terms))
