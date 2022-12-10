
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)
    
def convert_to_word_list(text):
        
    text_lowercase = text.lower()
    text_split = split(",.?  ", text_lowercase)
    filtered_text_list = list(filter(lambda word: word, text_split))
    return filtered_text_list


def words_longer_than(length, text):

    text_lowercase = text.lower()
    text_split = split(",.?  ", text_lowercase)
    words_longer_than = list(filter(lambda word: len(word) > length, text_split))
    return words_longer_than


def words_lengths_map(text):

    dic = {}
    filtered_text_list = convert_to_word_list(text)
    for word in filtered_text_list:
        if len(word) in dic:
            dic[len(word)] += 1
        else:
            dic[len(word)] = 1
    return dict(sorted(dic.items()))


def letters_count_map(text):
    
    dic = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,\
            "l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,\
            "w":0,"x":0,"y":0,"z":0} 
    filtered_text_list = convert_to_word_list(text)
    filtered_text = "".join(map(str,filtered_text_list))
    for letter in filtered_text:
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] = 1 
    return dic


def most_used_character(text):

    if not text:
        return None
    dic = letters_count_map(text)
    max_value = max(dic.values()) 
    max_keys = [key for key, value in dic.items() if value == max_value]
    most_used_character = max_keys
    return ', '.join(map(str, most_used_character))
    
