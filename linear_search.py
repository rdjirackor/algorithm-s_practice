def linear_search(list,target):
    for i in range(len(list)):
        if list[i]==target:
            return i
    return None
#This is a practice of what i learnt about linear search, should return the position of what is being searched for in the list       

print(linear_search([1,2,3,4,5,6,7,8,9],0))