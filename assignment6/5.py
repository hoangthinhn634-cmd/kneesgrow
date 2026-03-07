def remove_odd(numbers):
    result = []

    for n in numbers:
        if n % 2 == 0:
            result.append(n)

    return result


original = [1, 2, 3, 4, 5, 6, 7, 8]

new_list = remove_odd(original)

print("Original list:", original)
print("Without odd numbers:", new_list)