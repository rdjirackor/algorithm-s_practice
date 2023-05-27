def selection_sort(list):
    n=len(list)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if list[j]<list[min_index]:
                min_index=j
        list[i],list[min_index]=list[min_index],list[i]    
    return list
print(selection_sort([2,4,1,5,7,4,6,3]))