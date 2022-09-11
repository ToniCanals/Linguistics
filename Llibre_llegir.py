import time
start = time.time()
from collections import defaultdict


fhand = open(r"C:\Users\T.C\Documents\Info examens\Romeo.txt")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        #counts[word] = counts.get(word, 0) + 1
        if len(word)>=8:#Provam paraules més llargues
            matches = '-,.()=9876543210[]#://_"'
            if any (x in word for x in matches) == False:# Estaria com adalt però entraven enumeracions enlloc de paraules # Afegim l'any per asegurarmos de que no agafam cap paraula que tengui aquests simbols
                counts[word]= counts.get(word,0) +1

#Estaria interessant mirar de fer split() per aconseguir les paraules amb comes

#We want to solve if the dictionary has this type of repetitions "a" vs "A" separated as two diferet ones and combine them with the sum of the values

new_counts= defaultdict(int)
for key, val in counts.items():
    new_counts[key.lower()] += val


lst= list()
for key,val in new_counts.items():
    newtup = (val,key) #Ordre diferent
    lst.append(newtup)


lst = sorted(lst,reverse=True)# sorted posa de manera predeterminada en odre ascendent, noltros volem les més freqüents primer per tal de després poder agafar els n primers
    

lst_final=list()
for val,key in lst[:100]:
    newtup = (key,val)
    lst_final.append(newtup)



end = time.time()
print("Ha tardat en còrrer {} segons".format(end - start))
#----------------------------------------
import numpy as np
import matplotlib.pyplot as plt

word, frequency = zip(*lst_final)

indices = np.arange(len(lst_final))
plt.bar(indices, frequency, color='r')
plt.xlabel("Words")
plt.ylabel("Frequency of words")
plt.xticks(indices, word, rotation='vertical')
plt.tight_layout()
plt.show()