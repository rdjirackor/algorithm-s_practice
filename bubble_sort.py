def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                temporary_variable=list[j+1]
                list[j+1]=list[j]
                list[j]=temporary_variable
    return list
list_of_numbers_to_be_ordered=[99,2,11,100,1000,3,2,1,3,4,5,6,6,90]

def bubble_sort_recur(list, unsorted_portion):
    if unsorted_portion<=1:
        return list
    for j in range(unsorted_portion-1):
        if list[j]>list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    bubble_sort_recur(list,unsorted_portion-1)
    return list
#print(bubble_sort_recur(list_of_numbers_to_be_ordered,len(list_of_numbers_to_be_ordered)))



def bubble_sort_back(list):
     for i in range(len(list)):
          for j in range(len(list)-1):
               if list[j]<list[j+1]:
                    temp=list[j]
                    list[j]=list[j+1]
                    list[j+1]=temp
     return list
print(bubble_sort_back(list_of_numbers_to_be_ordered))