def has_unique_characters(s):

    letters = []


    for i in range(len(s)):
        char = s[i]  

        
        if char in letters:
            return False  
        letters.append(char) 

    return True  


print(has_unique_characters("Hello")) 
print(has_unique_characters("World"))  