import random
import time

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True

                
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0


    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    
    if len(nums) <= 1:
        return nums

    
    mid = len(nums) // 2

    
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    
    return merge(left_list, right_list)


# Verify it works


random_list_of_nums = random.sample(range(1, 1000), 500)
list1 = random_list_of_nums[:]
list2 = random_list_of_nums[:]

print(random_list_of_nums)
start = time.time()
bubble_sort(list1)
print((time.time()-start)*1000)

start = time.time()
merge_sort(list2)
print((time.time()-start)*1000)
print(list1)
