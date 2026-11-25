
file_name=input("Enter the name of the file: ")#reading the file's name from the user

file=open(file_name,'r',encoding='utf8')#we open the file in reading mode and encoding utf-8



words={}
letters={}

def remove_punctuations_split(line):
    punctuations = ["!",".","-","?",","," ","\n"]
    no_punctuations=[]
    temporary=''
    for character in line:
        if character not in punctuations:
            temporary=temporary +character
            
        else:
            no_punctuations.append(temporary)
            temporary=''
            
    return no_punctuations

def put_word(word,words):
    
    
    if word in words:
        words[word]=words[word]+1
    else:
       words[word]=1

def put_letter(letter,letters):
    
    
    if letter in letters:
        letters[letter]=letters[letter]+1
    else:
        letters[letter]=1
        
#def split_method(string):
#    value=[]
#    temporary=''
#    for character in string:
#        if character==' ':
#            #print(character)
#            value.append(temporary)
#            temporary=''
#        else:
#            temporary=temporary+character
            
#    return value
        
        



print("Reading the contents of the file...")

file_lines=file.readlines()

for line in file_lines:
    line=remove_punctuations_split(line)
    for word in line:
        
        
        put_word(word,words)
        for letter in word:
            put_letter(letter,letters)
            
file.close()
            
#for key in words.keys():
#    print(key,' ' ,words[key])
    
#for key in letters.keys():
#    print(key,' ',letters[key])

words_file=open("words.txt",'w')

max_letters={}
max_words={}    

for i in range(1,11):
    max_word=max(words,key=words.get)
    max_words[max_word]=words[max_word]
    del words[max_word]

words_list=[]

for word in max_words.keys():
    words_list.append(word)
    
words_list.sort()

for i in range(0,len(words_list)):
    
    print("word number " +  str(i)+" is : " +i)

for word in words_list:
    words_file.write(word + " "+ str(max_words[word])+ "\n")
    




   
words_file.close()

characters_file=open("characters.txt",'w')


for i in range(1,11):
    max_letter=max(letters,key=letters.get)
    max_letters[max_letter]=letters[max_letter]
    del letters[max_letter]

letters_list=[]

for letter in max_letters.keys():
    letters_list.append(letter)
    
letters_list.sort()

for letter in letters_list:
    characters_file.write(letter + " "+ str(max_letters[letter])+ "\n")    

characters_file.close()










