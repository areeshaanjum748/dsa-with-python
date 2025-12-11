def find_sum(nums, k):
    
    res = []
    nums.sort()
    
    left = 0
    right = len(nums) - 1
    
    while(left < right):
        
        sum_val = nums[left] + nums[right]
        
        if sum_val < k:
            left += 1
            
        elif sum_val > k:
            right -= 1
            
        else:
            res.append(nums[left])
            res.append(nums[right])
            break
            
    # Replace this placeholder return statement with your code
    return res
