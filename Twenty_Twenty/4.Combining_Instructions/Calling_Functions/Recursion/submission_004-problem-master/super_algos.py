def find_min(element):
    """ In this function finds and returns the minimum element in a list of integers."""
    if len(element) == 0 :
        return -1
    
    for i in element:
        if isinstance(i,int) == False:
            return -1
    if len(element) == 1:
        return element[0]

    if element[0] < element[1]:
        element[1] = element[0]
        
    
    return(find_min(element [1:]))


def sum_all(element):
    """ In this function, we calculate and return the sum of all element in a list of integers"""
    if len(element) == 0 :
        return -1
        
    for i in element:
        if isinstance(i,int) == False:
            return -1
    if len(element) == 1:
        return element[0]

    if len(element) != 1:
        element[1] += element[0] 
        
    return(sum_all(element [1:]))


def find_possible_strings(character_set, n):
    """ In this function we return a list of all possible strings of length n from the provided character_set"""
    character = []
    for i in character_set:

        if isinstance(i,int) == True:
            return [] 
    
    if n == 1:

        return character_set

    if n > 0:
        for i in character_set:
            for char in find_possible_strings(character_set, n-1):
                character.append(i + char)

    return character

    


