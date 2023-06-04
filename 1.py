def maxProduct(nums):
    
    max_product = nums[0]
    min_product = nums[0]
    result = max_product
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
             max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product, min_product)
    
    return result
        
print(maxProduct([2,-3,-4,6]))