def letter_count(s):
    count_dict = {} 


    for i in range(len(s)):
        char = s[i] 

       
        if char in count_dict:
            count_dict[char] += 1
        else:
        
            count_dict[char] = 1

    return count_dict  


print(letter_count("hello"))  
print(letter_count("pneumonoultramicroscopicsilicovolcanoconiosis"))
