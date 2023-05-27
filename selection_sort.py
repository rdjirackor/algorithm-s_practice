def selection_sort(list):
    n=len(list)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):

            if list[j]<list[min_index]:
                min_index=j
        list[i],list[min_index]=list[min_index],list[i]
    return list

            
print(selection_sort([21,-1,6789,1234567890,-1234567890,67574,23456,87,99,123,4,0,4,7,32,33,4,5,6,7,8,9,0]))
