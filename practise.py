numbers = []

while True:
    num = input("Enter a number (or 'done' to finish): ")
    
    if num.lower() == 'done':
        break
    
    try:
        num = float(num)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a number or 'done' to finish.")

if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    print("The average is:", average)
else:
    print("No numbers were entered.")
