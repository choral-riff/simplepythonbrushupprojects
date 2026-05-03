########################################################
# bubble sort in python 
# basically the biggest value bubbles up from each complete run through the array 

# Example: [7,3,9,10,12,11]

# Step 1: [7,3,9,10,12,11]
# Step 2: [7,3,  9,10,12,11] #7 and 3 need to swap 
# Step 3: [3,7,  9,10,12,11] #swapped
# Step 4: [3,  7,9,  10,12,11] #7 and 9 are okay 
# Step 5: [3,7,  9,10,  12,11] # 9 and 10 are okay
# Step 6: [3,7,9,  10,12,  11] # 10 and 12 are okay 
# Step 7: [3,7,9,10,  12,11] # 12 and 11 need to swap 
# Step 8: [3,7,9,10,  11,12] 

# This was one complete run of the bubble sort, and it bubbled up the biggest value. 
# Through each successive run, the second smallest value gets pushed up.

# in the following code, i have included swapped boolean stopper 
# just in case we do not need to go through runs once the arr is sorted. 
########################################################
my_arr = [7, 3, 9, 12, 11]

n = len(my_arr)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_arr[j] > my_arr[j+1]:
            my_arr[j], my_arr[j+1] = my_arr[j+1], my_arr[j]
            swapped = True 
    if not swapped:
        break

print("Sorted array:", my_arr)
