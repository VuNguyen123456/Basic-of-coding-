def composite_ratio(x):
    #keep track of the number of factor that can be produce
    factors = 0 
    #Finding and adding up the number of factors
    for i in range(x):
        if x % (i+1) == 0:
            factors += 1
    #Finding the ratio between the number and the number of factors
    compo_ratio = x/factors
    #Returning result
    return (compo_ratio)
    
def add_em_up(bottom, top):
    #Keeping track of the counter
    counter = 0
    for i in range(top):
        #Adding numbers as the amount of iterations increase
        bottom += (i+1)
        #Finding the number of time the program need to count
        if bottom < top:
            counter += 1
    #Returning result
    return (counter)
            
def wacky_factors(f_list, big_list):
    #Keeping track of the number of factors that can be produced
    num_facs = 0
    #Finding how many factors can be produce 
    for num1 in big_list:
        for num2 in f_list:
            if num1 >= num2 and num1 % num2 == 0:
                num_facs += 1
            else:
                num_facs += 0
    #Return result
    return (num_facs)
    
def vowels_count(letters):
    #Keeping track of all values needed in the program
    count_fi =0
    letter_fi = ''
    count_a = 0
    count_e = 0
    count_i = 0
    count_u = 0
    count_o = 0
    #Finding the largest repeated vowels and it's letter
    for letter in letters:
        #counting how many time vowel a was repeated
        if letter == 'a' or letter == 'A':
            count_a += 1
            #Assigning final count and letter with vowel a 
            if count_a >= count_fi:
                count_fi = count_a
                letter_fi = 'a'
            else:
                count_fi = count_fi
        #counting how many time vowel e was repeated
        elif letter == 'e' or letter == 'E':
            count_e += 1
            #Assigning final count and letter with vowel e if repeated most
            if count_e >= count_fi:
                count_fi = count_e
                letter_fi = 'e'
            else:
                count_fi = count_fi
        #counting how many time vowel i was repeated
        elif letter == 'i' or letter == 'I':
            count_i += 1
            #Assigning final count and letter with vowel i if repeated most
            if count_i >= count_fi:
                count_fi = count_i
                letter_fi = 'i'
            else:
                count_fi = count_fi
        #counting how many time vowel o was repeated
        elif letter == 'o' or letter == 'O':
            count_o += 1
            #Assigning final count and letter with vowel o if repeated most
            if count_o >= count_fi:
                count_fi = count_o
                letter_fi = 'o'
            else:
                count_fi = count_fi
        #counting how many time vowel u was repeated
        elif letter == 'u' or letter == 'U':
            count_u += 1
            #Assigning final count and letter with vowel u if repeated most
            if count_u >= count_fi:
                count_fi = count_u
                letter_fi = 'u'
            else:
                count_fi = count_fi
        else:
            count_fi += 0
        #Store the result into a string
        result_str = ("Most Frequent: \'" + str(letter_fi) + "\'"+" Count: " + 
                      str(count_fi))
    #Returning result
    return (result_str)
