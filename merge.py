def mergesort(list):
    if len(list)>1:
        left=list[:len(list)//2]
        right=list[len(list)//2:]
    
        mergesort(right)
        mergesort(left)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                list[k]=left[i]
                i+=1
            else:
                list[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            list[k]=left[i]
            k+=1
            i+=1
        while j<len(right):
            list[k]=right[j]
            j+=1
            k+=1
    return list

print(mergesort([16,2,4,2,5,6,3,7]))
