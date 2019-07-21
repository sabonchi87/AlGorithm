

def maxCrossingSum(arr, low, mid, high) : 
      
    # Include elements on left of mid. 
    sm = 0; left_sum = -10000000
      
    for i in range(mid, low-1, -1) : 
        sm = sm + arr[i] 
          
        if (sm > left_sum) : 
            left_sum = sm 
            max_left =i
      
      
    # Include elements on right of mid 
    sm = 0; right_sum = -1000000
    for i in range(mid + 1, high + 1) : 
        sm = sm + arr[i] 
          
        if (sm > right_sum) : 
            right_sum = sm 
            max_right =i
      
    Max_sum=left_sum + right_sum
    # Return sum of elements on left and right of mid 
    return [max_left,max_right,Max_sum]
    
    # Returns sum of maxium sum subarray in aa[l..h] 
def maxSubArraySum(arr, low, high) : 
      
    # Base Case: Only one element 
    if (low== high) : 
        return (low, high, arr[low])
    else: 
    
    # Find middle point 
       mid = (low + high) // 2
       (left_low, left_high, left_sum)=maxSubArraySum(arr, low, mid)
       (right_low, right_high, right_sum) =maxSubArraySum(arr,mid+1, high)
       (cross_low, cross_high, cross_sum)=maxCrossingSum(arr, low, mid, high)

       if left_sum >= right_sum and left_sum >= cross_sum:
               return (left_low, left_high, left_sum)
       elif right_sum >= left_sum and right_sum >= cross_sum:
               return (right_low, right_high, right_sum)
       else:
               return (cross_low, cross_high, cross_sum)

     
    
               
               
#arr = [5,10,-24,7,10 ,-3 ,2 ,8 ]               
arr = [14,-8,-9,27,-3,15,-16,12 ] 
#arr=[13,-3,-25,20,-3,-16,-23,18]
#arr=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
#arr = [-5,-10,-12,-7,-10 ,-3 ,-2 ,-8 ] 
n = len(arr) 
low=0
high=n-1
mid = (low + high) // 2
print( maxSubArraySum(arr, low, high) )
#max_sum_r=maxSubArraySum(arr, low, mid+1) 
#print("Maximum contiguous sum is ", max_sum_l,left,right) 
#print("Maximum contiguous sum is ", max_sum_r,mid+1,high)