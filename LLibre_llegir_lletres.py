#Letter frecuency within book
import time
import string
start = time.time()
from collections import defaultdict

name_of_book = "Romeo and Juliet"

fhand = open(r"C:\Users\T.C\Documents\Info examens\Romeo.txt")
alphabet = list(string.ascii_letters)
counts = dict()
counts_vowel_consonant = {'vowels':0,'consonants':0}
for line in fhand:
    words = line.split()
    for word in words:
    	for character in word:
		    if character in alphabet:
		    	counts[character] = counts.get(character,0) + 1 #Let's now compare total number of vowels vs consonants
		    	if character in ("A","E","I","O","U","a","e","i","o","u"):
		    		#name1="vowel"
		    		counts_vowel_consonant['vowels'] = counts_vowel_consonant['vowels'] + 1
		    		# 0 --> vowel
		    	else:
		    		#name2="consonant"
		    		counts_vowel_consonant['consonants'] = counts_vowel_consonant['consonants'] + 1
		    		# 1 --> consonant
		    else:
		    	continue

#Estaria interessant mirar de fer split() per aconseguir les paraules amb comes


lst2 = list()
for key,val in counts_vowel_consonant.items():
    newtup = (val,key)
     #Ordre diferent
    lst2.append(newtup)


lst2 = sorted(lst2,reverse=True)# sorted posa de manera predeterminada en odre ascendent, noltros volem les més freqüents primer per tal de després poder agafar els n primers


lst_final2 = list()
for val,key in lst2:
    newtup = (key,val)
    lst_final2.append(newtup)

print(lst_final2)


#----------------------------

new_counts= defaultdict(int)
for key, val in counts.items():
    new_counts[key.lower()] += val

lst = list()
for key,val in new_counts.items():
    newtup = (val,key) #Ordre diferent
    lst.append(newtup)


lst = sorted(lst,reverse=True)# sorted posa de manera predeterminada en odre ascendent, noltros volem les més freqüents primer per tal de després poder agafar els n primers
print(lst)
print(len(lst))    

lst_final = list()
for val,key in lst:
    newtup = (key,val)
    lst_final.append(newtup)

""" 
Queda afegir nom columnes a,b,c,d... i vocals, consonants  FET

Diferent color per a vocals i consonants a el primer gràfic amb una llegenda, blau vocals vermell consonants

Estudi de percentatge de contribució de cada lletra a nombre total de consonants, vocals i total.

"""



end = time.time()
print("Ha tardat en còrrer {} segons".format(end - start))
#----------------------------------------
import numpy as np
import matplotlib.pyplot as plt

character, frequency = zip(*lst_final)
typeofchar,frequency2 = zip(*lst_final2)


fig, ax = plt.subplots(1,2)
ax1,ax2 = ax.ravel()

indices = np.arange(len(lst_final))
indices2 = np.arange(len(lst_final2))



lst_vowels=list()
lst_consonants=list()
for key,val in lst_final:
	if key in ("a","e","i","o","u"):
		newtup = (key,val)
		lst_vowels.append(newtup)
	else:
		newtup = (key,val)
		lst_consonants.append(newtup)

char1, freq1 = zip(*lst_vowels)
char2, freq2 = zip(*lst_consonants)

indices_vowel = np.arange(len(lst_vowels))
indices_consonants = np.arange(len(lst_consonants))

print(lst_consonants)
print(lst_vowels)



#We want to separate character into character_vowel and character_consonant and merge both of them with different colours iin ax[0]
#Problem is we have their frecuency assciated to them, that will be lost so we must 

#print(indices)
#ax[0].bar(indices, frequency, alpha = 0.75, color = 'r')

for letter in lst_vowels:
	ax1.bar(indices_vowel, freq1, alpha = 0.75, color = 'b')
for letter in lst_consonants:
	ax1.bar(indices_consonants, freq2, alpha = 0.75, color = 'r')
	
# for i in range(10, 20):
#     ax.get_children()[i].set_color("blue")



ax[1].bar(indices2, frequency2, alpha = 1, color = 'g')




ax1.set_xticks(indices)
ax1.set_xticklabels(character)




ax2.set_xticks(indices2)
ax2.set_xticklabels(typeofchar)









plt.setp(ax[0], xlabel='Letters')
plt.setp(ax[0], ylabel='Number of times it appears')
plt.setp(ax[1], xlabel='Vowels vs Consonants')
plt.setp(ax[1], ylabel='Number of times it appears')



plt.suptitle("Study of linguistic properties of {}".format(name_of_book))

plt.tight_layout()
plt.show()


