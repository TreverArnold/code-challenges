def generate_hashtag(s):
    words = s.strip().split()
    if len(words) == 0 or words[0] == "":
        return False
    
    hashtag = "#" + "".join(word.capitalize() for word in words) 
    
    if len(hashtag) > 140:
        return False
    
    return hashtag
