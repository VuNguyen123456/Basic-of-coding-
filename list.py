def indices(some_list, another_list):
    #Create a blank list
    result = []
    #Iterating through some_list
    for i in range(len(some_list)):
        #Append the index position of repeated word
        if some_list[i]==another_list[i]:
            result.append(i)
    return result


def compute(lst1, lst2, lst3):
    result = []
    #Iterating through list 1
    for i in range(len(lst1)):
        #If the value is False in list 3 
        if lst3[i] == False:
            #List 1 value - list 2 value on the same index
            lst1[i] -= lst2[i]
        #If the value is False in list 3
        elif lst3[i] == True:
            #List 1 value + list 2 value on the same index
            lst1[i] += lst2[i]
    result = lst1
    return result

    
def replace_elems(lst1, lst2, n):
    result = []
    #If list 1 is bigger than list 2
    if len(lst1) > len(lst2):
        #Going through lst2 and replace the n'th element of lst 2 = lst1
        for i in range(n-1,len(lst2),n):
            lst2[i] = lst1[i]
        result = lst2
    #if list 2 is bigger or equal to list 1
    elif len(lst1) <= len(lst2):
        #Going through lst1 and replace the n'th element of lst 1 = lst2
        for i in range(n-1,len(lst1),n):
            lst1[i] = lst2[i]
        result = lst1
    return result

def extra_copies(some_list):
    result = 0
    new_list = []
    #Iterating though length of some_list
    for i in range(len(some_list)):
        #Appending the new element in some_list to new_list 
        #So that if the same element appear again it will move to a new element
        if some_list[i] not in new_list:
            new_list.append(some_list[i])
            #Iterating through some_list length again
            for k in range(len(some_list)):
            #If the element of some_list at k = element at i, increment 1
                if k !=i and some_list[k] == some_list[i]:
                    result += 1
    return result
