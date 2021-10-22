def count_rotations_linear(nums):
    position = nums[0]                 # What is the intial value of position?
    
    while position <= len(nums):                     # When should the loop be terminated?
        
        # Success criteria: check whether the number at the current position is smaller than the one before it
        if position > 0 and nums[position] > nums[position+1]:   # How to perform the check?
            return position
        
        # Move to the next position
        position += 1
    
    return -1


nums = [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]

print(count_rotations_linear(nums))



