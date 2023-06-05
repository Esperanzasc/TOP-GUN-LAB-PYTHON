def find_maximum(numbers):
    if not numbers:
        return None

    max_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number

    return max_number

numbers = [10, 2, 5, 74, 90]
maximum = find_maximum(numbers)
print("El número máximo es: ", maximum)

