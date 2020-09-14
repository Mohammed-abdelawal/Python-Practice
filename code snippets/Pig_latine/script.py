# Keep these 2 lines
text_to_translate = input("Text to translate: ")
VOWELS = "aeiouyAEIOUY"


res = ""
for i in text_to_translate.split():

    if i[0] in VOWELS:
        res += i+'yay '

    else:
        c = ""
        count = 0
        while(i[count] not in VOWELS):
            c += i[count]
            count+=1
        res += (i[count:]+c+'ay ')
        

# Keep this line
print("Translation:", res)
