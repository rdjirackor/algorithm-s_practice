sorted_nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def bin_search(list, target):
    low = 0
    high = len(list) - 1  # Fix: Subtract 1 here
    while low <= high:
        mid = (high + low) // 2
        if list[mid] < target:  # Fix: Compare list[mid] with the target
            low = mid + 1  # Fix: Increment low by 1
        elif list[mid] > target:  # Fix: Compare list[mid] with the target
            high = mid - 1  # Fix: Decrement high by 1
        else:
            return mid
    return None  # Fix: Return None if the target is not found

#print(bin_search(sorted_nums, 2))

def recur_bin_search(list,target):
    
    if len(list)==0:
        return False
    mid=len(list)//2
    if list[mid]==target:
        return True
    else:
        if target>list[mid]:
            return recur_bin_search(list[mid+1:],target)
        else:
            return recur_bin_search(list[:mid],target)
def verify(rez):
    print("Found:",rez)

nums=[1,2,3,4,5,7,8,9,10]


re=recur_bin_search(nums,15)
verify(re)










