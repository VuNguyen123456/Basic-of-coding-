def findRecommendations(matches):
    copy = []
    sub = []
    #Make a deep copy of the list
    for value in matches:
        copy.append(value)
    matches.clear()
    #Iterate throught the int value in the list
    for i in range(2, len(copy), 3):
        sub = []
        #If the score is larger than 80 then add the information to a list
        if copy[i] >= 80:
            sub.append(copy[i-2])
            sub.append(copy[i-1])
            sub.append(copy[i])
            matches.append(sub)
    bigNum = -1
    bigLoc = -1
    #Add a heart in the list that have the most point
    if len(matches) > 0:
        for k in range(len(matches)):
            if matches[k][2] > bigNum:
                bigNum = matches[k][2]
                bigLoc = k
        matches[bigLoc].append("\u2665")
    
def compressInfo(datingTrack):
    copy2 = []
    #Make a copy of the list
    for value2 in datingTrack:
        copy2.append(value2)
    datingTrack.clear()
    new_list = []
    count = 0
    newer_list = []
    #Interating though the list and comparing values
    for i in range(len(copy2)):
        #Letting the function count the value if the value is new 
        if copy2[i][0] not in new_list:
            new_list.append(copy2[i][0])
            sub_tuple =()
            count = 0
            #Counting the number of repeated value
            for k in range(len(copy2)):
                if copy2[i][0]==copy2[k][0]:
                    count += 1
                sub_tuple = (copy2[i][0], count)
            #Appending tuples
            datingTrack.append(sub_tuple)

                
                
def combineInfo(profileInfo, datingTrack):
    #Iterating through 2 list and compare their value
    for i in range(len(profileInfo)):
        for k in range(len(datingTrack)):
            #If their value are the same then modify the list
            if profileInfo[i][1] == datingTrack[k][0]:
                profileInfo[i].append(datingTrack[k][1])


def setofNames(profiles, location):
    output = {}
    output = set(output)
    #Iterating though the dictionary lists value 
    for i in profiles.values():
        #Comparing the location of person and the location wanted
        if location == i[2]:
            #Add people name to a set
            output.add(i[0])
    return output
