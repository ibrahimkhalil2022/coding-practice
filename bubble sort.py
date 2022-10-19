


def bubble_sort(nums):
    # We set swapped to true sp the loop looks runs at least onec

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                #swap the elements
                nums[i],  nums[i + 1] = nums[i+1], nums[i]
                #set the flag to true so we 'll loop again
                swapped = True

#verify it works

random = [5, 3,2,4,5,7,4,5,9,78,5,432,665,0]
bubble_sort(random)
print(random)
