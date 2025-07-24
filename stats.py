def count_words (contents):
    words = contents.split()
    word_num = 0
    for word in words:
        word_num+=1
    return word_num
def character_count(contents):
    character_dict = {}
    for characters in contents:
        lowercharacters = characters.lower()
        if lowercharacters in character_dict:
            character_dict[lowercharacters] += 1
        else:
            character_dict[lowercharacters] = 1
    return character_dict
def sorted_dict(character_dict):
        def sort_on(item):
            return item["num"]
        list_of_dict=[]
        for key, value in character_dict.items():
            new_dict = {"char":key,"num":value}
            list_of_dict.append(new_dict)
        list_of_dict.sort(reverse=True, key=sort_on)
        return list_of_dict
