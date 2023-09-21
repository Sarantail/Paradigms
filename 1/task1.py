def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        max_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[j] > numbers[max_idx]:
                max_idx = j
                numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]


numbers = [1, -2, 3, -4, 5, 6]
sort_list_imperative(numbers)
print(numbers)
