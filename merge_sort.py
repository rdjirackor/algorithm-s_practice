def mergesort(list):
    if len(list)>1:
        left_list=list[:len(list)//2]
        right_list=list[len(list)//2:]
        mergesort(left_list)
        mergesort(right_list)



        i=j=k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list[k]=left_list[i]
                i+=1
            else:
                list[k]=right_list[j]
                j+=1
            k+=1
        while i<len(left_list):
            list[k]=left_list[i]
            i+=1
            k+=1

        while j<len(right_list):
            list[k]=right_list[j]
            j+=1
            k+=1
    return list
    
print(mergesort([19,2,3,4,5,6,7,8,9,10]))


















"""def mergesort(list):
    n=len(list)
    halfed=n//2
    if n==1:
        return list
    else:
        left=list[:halfed]
        mergesort(left)
        right=list[halfed:]
        mergesort(right)
        return list
print(mergesort([2,3,4,5,6,6]))
"""        