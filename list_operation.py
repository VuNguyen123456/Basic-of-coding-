def shift_elems(elems, rt_shift = 1, filler = 'X'):
    #For loop to insert filler
    for i in range(rt_shift):
        elems.insert(i,filler)
    #For loop to shift the elems to the right
    for i in range(rt_shift):
        del elems[-1]
    return elems
    
def find_mode(lst):
    #create 2 empty lists and 1 empty dictionary
    new_lst = []
    the_lst = []
    dict = {}
    for i in range(len(lst)):
        #Filter out the elements that already appear before
        if lst[i] not in new_lst:
            new_lst.append(lst[i])
            count = 0
            #Getting the elements as key and time they got repeated as values
            #Impliment them into a dictionary
            for j in range(len(lst)):
                if lst[i] == lst[j]:
                    count += 1
                dict[lst[i]] = count
    #Finding the biggest value in the dictionary
    biggest = 0
    for value in dict.values():
        if value > biggest:
            biggest = value
    #Getting the elements that repeated the most time into a list
    for key in dict.keys():
        if dict[key] == biggest:
            the_lst.append(key)
    return the_lst
            
         
def find_median(lst2):
    #Get the averange of the 2 element in the middle if lenght of list is even
    if len(lst2) % 2 == 0:
        median = round((lst2[len(lst2)//2]+lst2[(len(lst2)//2)-1])/2,3)
    #Get the middle element of the list if the lenght of the list is odd
    elif len(lst2) % 2 == 1:
        median = lst2[len(lst2)//2]
    #If there is nothing in the list return None
    else: 
        median = None
    return median

def averages(lst3):
    #Return this if the list provided is empty
    total = 0
    dict_info = {}
    if len(lst3) == 0:
        dict_info['mean'] = None
        dict_info['mode'] = []
        dict_info['median'] = None
    #Getting the mode, mean, median and the list value into a dictionary
    else:
        for i in range(len(lst3)):
            total += lst3[i]
        mean = round(total/len(lst3),2)
        dict_info['mean'] = mean
        dict_info['mode'] = find_mode(lst3)
        dict_info['median'] = find_median(lst3)
    return dict_info

def add_chars(some_list, some_str):
    #Base case
    if len(some_list) == 0:
        return []
    else:
    #Append the first value of some_list into the new list
        new_list = []
        new_list.append(some_list[0])
        #Append the first value of some_str if some_str is not empty
        if len(some_str) > 0:
            new_list.append(some_str[0])
        #Recursion case
        return new_list + add_chars(some_list[1:], some_str[1:])
