# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.

# print("\n    Exercitiul 1")
# masini = ["Audi", "Volvo", "BMW", "Mercedes", "Aston Martin", "Lăstun", "Fiat", "Trabant", "Opel"]
# for i in range(len(masini)):
#     if masini[i] == 'Audi':
#         print(f"Masina mea preferata este {masini[i]}")


# ● Fă același lucru cu un for each.
# for marca in masini:
#     if marca == 'BMW':
#         print(f"Mașina mea preferată este: {marca}")

# ● Fă același lucru cu un while.
# i = 0
# while i <= len(masini)-1:
#     if masini[i] == 'Fiat':
#         print(f"Masina mea preferata este {masini[i]}")
#     i += 1



# 2. Aceeași listă:
# Folosește un for else
# În for
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.

# print("\n    Exercitiul 2")
# masini = ["Audi", "Volvo", "BMW", "Mercedes", "Aston Martin", "Lastun", "Fiat", "Trabant", "Opel"]
# for i in range(0, len(masini)):
#     if i == 0 or i == len(masini)-1:
#         continue
#     else:
#         masini[i] = masini[i].upper()
# else:
#     print(masini)


# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

# print("\n    Exercitiul 3")
#
# masini = ["Audi", "Volvo", "BMW", "Mercedes", "Aston Martin", "Lăstun", "Fiat", "Trabant", "Opel"]
# m = input("Introduceti marca masinii de la tastatura (prima litera cu majuscula): \n")
# for i in range(0, len(masini)):
#          if m == masini[i]:
#             print(f"{m} este in lista\n")
#             break
# else:
#     print("Marca introdusa nu este in lista")



# # 4. Aceași listă;
# # Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# # excepția Trabant și Lastun.
# # - Dacă mașina e Trabant sau Lăstun:
# # Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# # else).
# # - Printează S-ar putea să vă placă mașina x.
#
# print("\n    Exercitiul 4")
#
# masini = ["Audi", "Volvo", "BMW", "Mercedes", "Aston Martin", "Lastun", "Fiat", "Trabant", "Opel"]
# for masina in masini:
#     if masina in ("Trabant", "Lastun"):
#         continue
#     print(f"S-ar putea sa va placa masina {masina}")



#
# # 5. Modernizează parcul de mașini:
# # ● Crează o listă goală, masini_vechi.
# # ● Itereaza prin mașini.
# # ● Când găsesti Lăstun sau Trabant:
# # - Salvează aceste mașini în masini_vechi.
# # - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# #
# # ● Printează Modele vechi: x.
# # ● Modele noi: x.
#
# print("\n    Exercitiul 5")
#
# masini_vechi = []
# masini = ["Audi", "Volvo", "BMW", "Mercedes", "Aston Martin", "Lastun", "Fiat", "Trabant", "Opel"]
# for i in range(len(masini)):
#     if masini[i] == 'Lastun' or masini[i] == 'Trabant':
#         masini_vechi.append(masini[i])
#         masini[i] = 'Tesla'
# print(f'Masini vechi: {masini_vechi}')
# print(f'Modele noi: {masini}')




# 6. Având dict:
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.

# print("\n    Exercitiul 6")
#
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
#
# buget = 15000
# masini_de_buget = []
#
# for masina in pret_masini.items():
#     if masina[1] <= 15000:
#         print(f"Pentru o suma sub {buget}, puteti cumpara masina {masina}")
#         masini_de_buget.append(masina)
# print(f"Masini care se incadreaza in buget {buget} sunt {masini_de_buget}")
# masina_dorita = input('Alegeti masina care se incadreaza in buget (prima litera cu majuscule: ')
# for car in masini_de_buget:
#     if car[0] == masina_dorita:
#         print(f"Ati achizitionat masina {car}")


#
# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).

# print("\n   Exercitiul 7")
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# numaratoare = 0
# for element in numere:
#     if element == 3:
#         numaratoare += 1
# print(f"Numarul 3 apare de:   {numaratoare} ori")




# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).

# print("    Exercitiul 8")
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# rezultat = 0
# for numar in numere:
#     rezultat += numar
# print(f"Suma numerelor: {rezultat}")


# # 9. Aceeași listă:
# # ● Iterează prin ea.
# # ● Afișază cel mai mare număr (nu ai voie să folosești max).
# #
#
# print("\n    Exercitiul 9")
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# for i in range(len(numere)-1):
#     if numere[i] > numere[i+1]:
#         numere[i] = numere[i+1]
# .....

# # 10. Aceeași listă:
# # ● Iterează prin ea.
# # ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# # Ex: dacă e 3, să devină -3
# # # ● Afișază noua listă.
#
# print("\n    Exercitiul 10")
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(f" Noua lista (contine numere negative): {numere}")

# nr = int(input("introdu un numar: \n"))
# def is_natural(nr):
#     if nr >= 0:
#         return "Numarul este natural"
#     else:
#         return "Nu este numar natural"
# print(is_natural(nr))

# for i in range(5):
#     txt=input("baga aici: ")
#     try:
#         x=(float(txt)==txt)
#         txt=float(txt)
#     except:
#         print("nu ati introdus un numar")
#     else:
#          if (txt==round(txt) and txt==abs(txt)):
#              print("numar natural")
#          else:
#              print("numar nenatural")
# print("phew")





