'''
Exercitiul 1:
 În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

 Variabila este o zona din memorie care stocheaza o valoare si care devine
activa cand i se atribuie o valoare. Are nume unic si incepe cu litera mica.
Pe durata exxecutiei programului isi poate schimba valoarea si tipul de date.
'''

'''
Exercitiul 2:
 Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :
'''
# string
nume_produs = 'Casti in ear wireless'
# int
an_fabricatie = 2020
# float
pret = 168.33
# bool
in_stoc = True

'''
Exercitiul 3:
 Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
'''
print('nume produs este de tip: ', type(nume_produs))
print('anul fabricatiei este de tip: ', type(an_fabricatie))
print('pretul este de tip: ', type(pret))
print('in_stoc este de tip: ', type(in_stoc))
print('  ')

'''
Exercitiul 4:
Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
'''
pret = round(pret)
print(f'noul pret rotunjit {pret} este de tip:', type(pret), '\n')

'''
Exercitiul 5:
Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''
print(f'numele produsului este de tip: ', type(nume_produs))
print(f'anul fabricatiei {an_fabricatie} este de tip: ', type(an_fabricatie))
print('in_stoc este de tip: ', type(in_stoc))
print(f'pretul produsului {pret} este de tip: ', type(pret), 'il facem de tip float')
pret = float(pret)
print(f'pretul produsului {pret} este acum de tip: ', type(pret),'\n')


'''
Exercitiul 6:
Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
'''
nume = input("Introdu numele: \n")
prenume = input("Introdu prenumele: \n")
print('Numele complet are ', len(nume) + len(prenume), 'caractere\n')

'''
 Exercitiul 7:
 Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
'''
lungimea = int(input("Introdu lungimea: \n"))
latimea = int(input("Introdu latimea: \n"))
print(f'Aria dreptunghiului este {lungimea * latimea}\n')

'''
Exercitiul 8:
Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the'
'''
coral = 'Coral is either the stupidest animal or the smartest rock'
print(f'"the" apare de ', + coral.count('the '), ' ori\n')

'''
Exercitiul 9:
 Același string.
● Afișează de câte ori apare cuvântul 'the';
● Printează rezultatul..
'''



'''
Exercitiul 10:
Același string.
● Folosiți un assert ca să verificați dacă acest string conține doar numere.
'''

txt = input("Introdu textul: ")
for i in range(len(txt)-1):
    assert(txt[i].isnumeric())
print("Textul contine numai numere")


'''
Optional 1:
Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.'''

value = input("Introdu un string: \n")
print("Ai introdus: ", "'" + value + "'")

if len(value)%2:
    print("txt impar - litera din mijloc e " + value[int((len(value)-1)/2)])
else:
    print("txt par")
print("Gata")


'''
Optional 2: Folosind assert, verifică dacă un string este palindrom.
'''
value = input("Introduceti un string: \n")
print("Ai introdus: " + value + " ")
assert len(value)>1
palindrom=True
for i in range(int((len(value)-int(len(value)%2)/2))):
    if value[i]!=value[len(value)-1-i]:
        palindrom=False
        print("Nu este palindrom")
        assert palindrom==True
if palindrom==True:
    print("Perfect - \""+ value + "\" e palindrom")
print("Gata")

'''
Optional 3: 
Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
'''
value = input("Introduceti un string: \n")
print("Ai introdus: " + value + " ")
lista=value.split(" ")
print (lista)

for i in range(len(lista)):
    print(lista[i])

'''
4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
'''
value = input("Introduceti un string: \n")
print("Ai introdus: " + value + " ")
# lista=value.split(" ")
prima=value[0]

# #pt prvimul cuvant
# print(lista[0][0]+lista[0][1:len(lista[0])-1:1].replace(prima,prima.upper())+lista[0][len(lista[0])-1])

#tot stringu
print(prima+value[1:len(value)-1:1].replace(prima, prima.upper())+value[len(value)-1])

'''
5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
eg: parola abc => ***
parola abcd => ****
'''

user = input("login:")
parola = input("Password:")
print("nume utilizator " + user+ " iar parola e " + "*"*len(parola))
parola_hash=""
for i in range(len(parola)):
    parola_hash+="*"
print(parola_hash)
print("gata")