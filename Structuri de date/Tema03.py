# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ● Afișeaz-o
print('-'*50)
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale, '\n')

# ● Inversează ordinea folosind slicing și suprascrie această listă.
note_muzicale = note_muzicale[::-1]

# ● Printează varianta actuală (inversată).
print("Notele muzicale inversate: ", note_muzicale, "\n")

# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
note_muzicale.reverse()

# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.
print("Iata notele in starea initiala: ", note_muzicale, '\n')


# 2. De câte ori apare ‘do’?

print("Nota 'do' apare de: ", note_muzicale.count("do"), "ori\n")

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.

lista_1 = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
print((lista_1))
print(lista_2)
lista_3 = lista_1 + lista_2
# print(lista_3)
# lista_1.extend(lista_2)
# print(lista_1)


# 4.
# ● Sortează și afișază lista generată la exercițiul anterior.
# ● Sortează numărul 0 folosind o funcție.
# ● Afișaza iar lista.

# print('**** **** ****\n')
# print(f'lista noastra este: {lista_3}\n')
# index_0 = lista_3.index(0)
# print(f'cifra 0 are indexul {index_0}')
# lista_3.remove(0)
# print(f'dupa inlaturarea lui 0 lista devine: {lista_3}\n')



# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală.
# ● Lista nu este goală.

# print('-'*50)
# if len(lista_3) == 0:
#     print('Lista este goala\n')
# else:
#     print('Lista nu este goala\n')


# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.

# print('-'*50)
# lista_3.clear()
# print(f'am sters toate elementele din lista. lista arata astfel: {lista_3}\n')


# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.

# print('-'*50)
# if len(lista_3) == 0:
#     print('Lista este goala\n')
# else:
#     print('Lista nu este goala\n')

# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)

# print('-'*50)
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1.keys())


# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie

# print('-'*50)
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1.values())
# #sau
# print(dict1['Ana'], dict1['Gigel'], dict1['Dorel'])

# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare

# print('-'*50)
# dict1['Dorel'] = 6
# print(dict1['Ana'], dict1['Gigel'], dict1['Dorel'])


# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi

# print('-'*50)
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print(dict1)
# del dict1['Gigel']
# print(dict1)
# dict1['Ionica'] = 9
# print(f'elevii din clasa sunt: {dict1}\n')



# 12.
# Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Afișeaza zile_sapt

# print('-'*50)
# print(zile_sapt)
# zile_sapt.remove('luni')
# print('Am extras ziua de luni si saptamana arata asa: ', zile_sapt)
# zile_sapt.add('luni')
# print('Am introdus ziua de luni si saptamana arata asa: ', zile_sapt)


# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.

# print('-'*50)
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# print('Saptamana are urmatoarele zile: ', zile_sapt)
# weekend = {'sâmbăta', 'duminică'}
# if weekend.issubset(zile_sapt):
#     print("'weekend' este un subset al 'zile_sapt'")
# else:
#     print("Nu exista in set")


# 14. Afișează diferențele dintre aceste 2 seturi.

# print('-'*50)
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# print('Diferenta consta in urmatoarele zile: ', zile_sapt.difference(weekend))


# 15. Afișază intersecția elementelor din aceste 2 seturi.

# print('-'*50)
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# print('zilele comune sunt: ', zile_sapt.intersection(weekend))