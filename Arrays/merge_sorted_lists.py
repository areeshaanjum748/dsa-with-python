def merge_lists(nums1, nums2):
    
    # if first array is empty, return second
    if not nums1:
        return nums2
    
    # if second array is empty, return first
    if not nums2:
        return nums1
        
    res = []
    i = j = 0
    
    n = len(nums1)
    m = len(nums2)
    
    while(i < n and j < m):
        
        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
            
        else:
            res.append(nums2[j])
            j += 1
            
    if i < n:
        res.extend(nums1[i:])
        
    if j < m:
        res.extend(nums2[j:])
    
    # Replace this placeholder return statement with your code
    return res
