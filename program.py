
import collections
from collections import Counter

# Ζητάμε από τον χρήστη το όνομα του αρχείου που θέλει να ανάλυσει
file_name=input("Enter the name of the file: ")

# Άνοιγμα αρχείου με encoding utf8 για σωστή ανάγνωση ελληνικών χαρακτήρων
file=open(file_name,'r',encoding='utf8')

# Λεξικά για αποθήκευση των μετρήσεων λέξεων και γραμμάτων
words={} #Λίστα για αποθήκευση λέξεων
letters={} #Λίστα για αποθήκευση γραμμάτων


# Συνάρτηση για αφαίρεση σημείων στίξης από μια γραμμή
# Αντικαθιστά κάθε σημείο στίξης με κενό
def remove_punctuations(line):
    punctuations = ["!",".","-","?",",","|"]  # Λίστα σημείων στίξης που θέλουμε να αφαιρέσουμε
    no_punctuations="" #Σε αυτό το σημέιο, δημιουργούμε μια νέα συμβολοσειρά χωρίς σημεία στίξης
    
    for character in line: #Εξετάζει κάθε χαρακτήρα της γραμμής
        if character not in punctuations: #Ελέγχει όλους τους χαρακτήρες, εάν δεν είναι σημεία στίξης
            no_punctuations=no_punctuations +character #Αν ο χαρακτήρας δεν είναι σημείο στίξης, τον προσθέτουμε στη λέξη.
            
        else: #Αλλιώς σε περίπτωση που είναι
            no_punctuations=no_punctuations+" " #Κάνει αντικατάσταση με κενό διάστημα
            
    return no_punctuations #Επιστρέφει το τελικό κείμενο

# Συνάρτηση για προσθήκη λέξης στη λίστα (ή αύξηση του μετρητή της)
def put_word(word,words):
    # Ελέγχουμε αν η λέξη υπάρχει ήδη στη λίστα
    if word in words:
        words[word] += 1 #Αυξάνει τον μετρητή της λέξης κατά 1
    else:
       words[word] = 1 #Αν δεν υπάρχει η λέξη, την εμφανίζει για πρώτη φορά


# Συνάρτηση για προσθήκη γράμματος στο λεξικό (ή αύξηση του μετρητή του)
def put_letter(letter, letters):
    # Αγνοούμε τα κενά διαστήματα (δεν θέλουμε να μετράμε κενά)
    if letter.strip() == "": #Αφαιρεί τα κένα πριν και μετά από κάθε χαρακτήρα
        return #Σταματάει αν είναι κενό
    if letter in letters:
        letters[letter] += 1 #Αν έχει εμφανιστεί το γράμμα, αυξάνει τον μετρητή του κατά 1
    else:
        letters[letter] = 1  #Αν δεν υπήρχε προηγουμένως, το εμφανίζει για πρώτη φορά
        
#Μέσω αυτής της συνάρτησης, δημιουργήσαμε την δική μας μέθοδο split()
def split_method(string):
    value=[]  # Λίστα για αποθήκευση των λέξεων
    temporary=''  # Προσωρινή μεταβλητή για συσσώρευση χαρακτήρων
    for character in string:
        if character==' ':  # Αν βρούμε κενό, σημαίνει ότι τελείωσε η λέξη
            if temporary: #"Μαζεύει" τους χαρακτήρες μέχρι να βρει κενό
                value.append(temporary)  # Προσθέτουμε τη λέξη στη λίστα
                temporary=''  # Αδειάζει και ξεκινάει με την επόμενη λέξη
        else:
            temporary=temporary+character  # Μαζεύει τους χαρακτήρες της εκάστοτε λέξης
            
    return value
        
print("Reading the contents of the file...")

file_lines=file.readlines() # Διαβάζουμε όλες τις γραμμές του αρχείου


for line in file_lines: 
    line = remove_punctuations(line) #Καλείται η συνάρτηση remove_punctuations ώστε να αφαιρέσει τα σημεία στίξης από κάθε γραμμή
    for word in split_method(line):  #Καλείται η συνάρτηση split_method για να χωρίσει τη γραμμή σε λέξεις

        put_word(word, words) #Καλειται η συνάρτηση για την αποθήκευση της λέξης στη λίστα με δύο ορίσματα: τη λέξη και τη δομή
        for letter in word: #Βρόχος επανάληψης, κάνει loop και περνάει κάθε γράμμα της λέξης
            put_letter(letter, letters) #Προσθήκη γράμματος στην λίστα

file.close()
            
# Ανοίγουμε αρχείο εξόδου για τις λέξεις
words_file=open("words.txt",'w')

# Λίστα για αποθήκευση των 10 πιο συχνών λέξεων και γραμμάτων
max_letters={}
max_words={} 

# Εξάγουμε τις 10 πιο συχνές λέξεις 
for i in range(1,11):
    max_word=max(words,key=words.get)  # Βρίσκουμε τη λέξη με τη μεγαλύτερη συχνότητα
    max_words[max_word]=words[max_word]  # Την αποθηκεύουμε
    del words[max_word]

words_list=[] #Δημιουργία μίας κενής λίστας

for word in max_words.keys(): #Επιστρέφει όλες τις λέξεις του λίστας
    words_list.append(word) #Αφαιρεί τις λέξεις και τις προσθέτει στο τέλος της λίστας
    
words_list.sort()

# Γράφουμε κάθε λέξη με τη συχνότητά της
for word in words_list:
    words_file.write(word + " "+ str(max_words[word])+ "\n") #Το \n προσθέτει νέα γραμμή μετά από κάθε λέξη για να είναι σε ξεχωριστή γραμμή

# Κλείνουμε το αρχείο
words_file.close()

# Ανοίγουμε αρχείο εξόδου για τα γράμματα
characters_file=open("characters.txt",'w')

# Εξάγουμε τα 10 πιο συχνά γράμματα (τα ίδια με λέξεις)
for i in range(1,11):
    max_letter=max(letters,key=letters.get)  # Βρίσκουμε το γράμμα με τη μεγαλύτερη συχνότητα από την λίστα max_letters
    max_letters[max_letter]=letters[max_letter]  # Το αποθηκεύουμε σε μια νέα λίστα
    del letters[max_letter] #Διαγράφει το γράμμα από την αρχική λίστα για να βρει το επόμενο πιο συχνό στο επόμενο βήμα.

letters_list=[]

for letter in max_letters.keys(): #Παίρνει μόνο τα γράμματα από το max_letters
    letters_list.append(letter) #Μέσω της μέθοδου append τα προσθέτει στη λίστα letters_list
    
letters_list.sort()#Ταξινομεί τα γράμματα σε αλφαβητική σειρά

# Γράφουμε κάθε γράμμα με τη συχνότητά του
for letter in letters_list:
    characters_file.write(letter + " "+ str(max_letters[letter])+ "\n") #Το \n προσθέτει νέα γραμμή μετά από κάθε γράμμα για να είναι σε ξεχωριστή γραμμή

# Κλείνουμε το αρχείο
characters_file.close()