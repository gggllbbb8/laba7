#1
list=(map(int,input().split()))
a=sorted(list)

print('maximym=',a[-1],'minimym=',a[0])



#2

def max_subarray(nums):
    if not nums:
        return [],0
    max_sum=nums[0]
    current_sum=nums=[0]
    start=0
    end=0
    temp_start=0
    for i in range(1,len(nums)):
        if current_sum<0:
            current_sum=nums[i]
            temp_start=i
        else:
            current_sum+=nums[i]
            
        if current_sum>max_sum:
            max_sum=current_sum
            start=temp_start
            end=i
        return nums[start:end+1],max_sum
    sub_arr,total=max_subarray(arr)
    print('подмассив:',sub_arr)
    print('сумма', total)
