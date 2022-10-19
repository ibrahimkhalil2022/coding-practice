

def insertion_sort(nums):

    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]

        # And keep a reference of the index of the previous element

        j = i -1

        # Move all items of the sroted segment forword if they are larger than
        # the item to insert

        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -=1

        # Insert the item

        nums[j + 1] = item_to_insert


# verify it works

random_list_of_nums = [9,0,32,1,25,7,9,3]
insertion_sort(random_list_of_nums)
print(random_list_of_nums)
