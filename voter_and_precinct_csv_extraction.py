def voterPrecinct(voterFile, voterName):
    #Open the file to read
    file = open(voterFile)
    #Skip the first line that contain the title
    file.readline()
    #Clean the file and split it to a list
    for line in file:
        line = line.split(",")
        for i in range(len(line)):
            line[i] = line[i].strip('\n ')
        #return the result if the name in the file matches the name provided
        if line[0].lower() == voterName.lower():
            return 'Name: '+c(voterName)+' Precinct: '+c(line[3])
            


def findPrecinctInfo(precFile, precName):
    #Open the file to read and skip the first line that contain the title
    file = open(precFile)
    file.readline()
    string = ''
    #Clean the file and split it to a list
    for l in file:
        l = l.split(",")
        for i in range(len(l)):
            l[i] = l[i].strip('\n ')
        #if the precName in file = precName provided return string
        if clean(l[0]) == precName.lower():
            string = f'{c(clean(l[0]))} {c(l[2])} {c(l[3])} {c(l[4])}'
    return string
            
#Helper function to clean the word            
def clean(word):
    new = ''
    for char in word:
        #If char is a space keptit
        if char == ' ':
            new += ' '
        #If char not in alphabet then throw it out
        elif char.isalpha() == True:
            new += char
    return new.lower()
    
#Helper function to capitalized the first letter of the word
def c(msg):
    #Split the word
    new_word = ''
    msg = msg.lower()
    msg = msg.split(' ')
    #Iterating though each character
    for i in range(len(msg)):
        for j in range(len(msg[i])):
            #if the character is at index 0 capitalized it 
            if j == 0:
                new_word += msg[i][j].upper()
            else:
                new_word += msg[i][j]
        if msg[i] != msg[-1]: 
            new_word += ' '
    return new_word


def pollingPrecincts(precFile):
    #Open the file to read and skip the first line that contain the title   
    file = open(precFile)
    file.readline()
    dic = {}
    for line in file:
        try:
            line = line.split(",")
            for i in range(len(line)):
                line[i] = line[i].strip('\n ')
            #Convert to lower case
            line[0] = line[0].lower()
            line[4] = line[4].lower()
            #Creating key in a dict and append list in that key
            if line[4] not in dic:
                dic[line[4]] = [line[0]]  
            elif line[4] in dic:
                dic[line[4]].append(line[0])
        except FileNotFoundError:
            return "File Not Found"    
    #Apending the number count into each key value
    for key in dic:
        dic[key].append(len(dic[key]))
    return dic

def voter_data(flat_data):
    new_list = []
    #if the list provided doesn't have at least 3 element return empty list
    if len(flat_data) < 3:
        return []
    #Iterating though each name in list
    for i in range(0,len(flat_data),3):
        dic = {}
        #Creating a key for each name as value
        dic['Full Name'] = flat_data[i]
        try:
            #If met the requirement creat a key for value
            if 0 <float(flat_data[i+1]) < 1:
                dic['Participation Rate'] = float(flat_data[i+1])
            else:
                raise ValueError()
        #If an index Error occur 
        except IndexError:
            del dic
        #If requirement not met
        except ValueError:
            dic['Participation Rate'] = 0
        try:
            #If met the requirement creat a key for value
            if 10000<=int(flat_data[i+2])<=99999:
                dic['Zip Code'] = int(flat_data[i+2])
            else:
                raise Exception()
        #If an index Error occur 
        except IndexError:
            continue
        except Exception:
        #If requirement not met
            dic['Zip Code'] = 0   
        new_list.append(dic)
    return new_list
