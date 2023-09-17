import random
import string
# Coding-Dcoding of any text
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
choice = input("Enter 1 for coding and 0 for decoding : ")
if (choice == "1"):
    text = input ("Enter the text for coding : ")
    if (len(text) >= 3):
        code = ''
        text = text.split(" ")
        text1 = ''
        for word in text :
            if(len(word) >= 3):
                pre = post = ''
                pre += pre.join(random.choices(lower,k=3))
                post += post.join(random.choices(lower,k=3))
                word1 = pre + word[1:] + word[0] + post
            elif (len(word)==2) :
                word1 = word[1]+word[0]
            else :
                word1 = word
            text1 = text1 + ' ' + word1
    elif (len(text) == 2):
        text1 = text[1] + text[0]
    else:
        text1 = text
    print("The encoded text is : ",text1)
elif (choice == "0") :
    text = input ("Enter the encoded text for decoding : ")
    text = text.split(" ")
    text1 = ''
    if (len(text) >= 3):
        for word in text :
            if len(word) >= 3 :
                word1 = word[-4] + word[3:len(word)-4]
            elif(len(word) == 2) :
                word1 = word[1] + word[0]
            else:
                word1 = word
            text1 = text1 + ' ' + word1
    elif (len(text) == 2):
        text1 = text[1] + text[0]
    else:
        text1 = text
    print("The decoded text is : ",text1)
else :
    print("Oops! wrong choice !!!")