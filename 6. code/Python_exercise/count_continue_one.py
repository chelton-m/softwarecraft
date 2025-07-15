def count_continue_one(lst):
    current_count = 0
    max_count = 0
    for i in lst:
        if i == 1:
            current_count += 1
            max_count = max(current_count, max_count)
        else:
            current_count = 0
    return max_count


nums = [1, 1, 0, 1, 1, 1]
print(count_continue_one(nums))  # 3
