def remove_odd(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list


original = [1, 2, 3, 4, 5, 6, 7, 8]
filtered = remove_odd(original)

print("Original list:", original)
print("Even numbers only:", filtered)