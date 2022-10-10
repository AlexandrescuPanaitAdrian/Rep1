# #1.Funcție care să calculeze și să returneze suma a două numere
# print("Exercitiul 1")
# print("Introdu doua numere pe care sa le adunam")

# def suma_numerelor(primul_numar, al_doilea_numar:
#      suma = primul_numar + al_doilea_numar
#      return suma
# primul_numar = int(input("   Introdu primul numar:  \n"))
# al_doilea_numar = int(input("   Introdu al doilea numar:  \n"))
# print(f"Suma celor doua numere este: {suma_numerelor(primul_numar, al_doilea_numar)}")


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

# print("   Exercitiul 2\n")
# print(" Testam o functie care sa recunoasca daca numarul introdus este par sau impar")
#
# def testare_par_impar(nr):
#      if nr %2 == 0:
#            print('Numarul introdus este par')
#           return True
#      else:
#            print('Numarul introdus este impar')
#           return False
# nr = int(input(" Introdu numarul testat: "))
# print(testare_par_impar(nr))

#
# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

# print("   Exercitiul 3\n")
# def nr_caractere(nume):
#      nume_fam, prenume, nume_mijlociu = nume.split()
#      lungime_nume = len(nume_fam) + len(prenume) +len(nume_mijlociu)
#      return lungime_nume
#
# nume = input("Introdu numele si prenumele separate de spatii:\n")
# print(f"Numele complet are {nr_catactere(nume)} caractere")

#
# 4. Funcție care returnează aria dreptunghiului
# print("   Exercitiul 4\n")
# def arie_dreptunghi():
#      arie = lungime * latime
#      return arie
# lungime = int(input("Introduceti lungimea laturii: \n"))
# latime = int(input("Introduceti latimea laturii: \n"))
# print(f"Aria dreptunghiului este: {arie_dreptunghi()}")

#
# 5. Funcție care returnează aria cercului
# print("   Exercitiul 5\n")
# def arie_cerc():
#      arie = 2 * 3.14 * r * r
#      return arie
# r = int(input("Introduceti raza cercului: \n"))
# print(f"Aria cercului este: {arie_cerc()}")

#
# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și Talse dacă nu găsește.
# print("   Exercitiul 36\n")
# def true_false():
#     sir_caractere = 'sadaadffgrbmimdueoq'
#     if caracter in sir_caractere:
#         return True
#     else:
#         return False
# caracter = input("Introdu un caracter: \n")
# print(true_false())



# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

# print("   Exercitiul 7\n")
# def mici_maj():
#      cont_mici = 0
#      cont_maj = 0
#      for caracter in sir_caractere:
#           if caracter.islower():
#                cont_mici += 1
#           else:
#                cont_maj += 1
#      print(f"Numarul de caractere UPPERCASE: {cont_maj}")
#      print(f"Numarul de caractere LOWERCASE: {cont_mici}")
#
# sir_caractere = str(input(" Introduceti un sir de caractere mici si majuscule: "))
# print(mici_maj())


# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive

# print("   Exercitiul 8\n")
# def ret_nr_poz():
#     numere_poz = []
#     for nr in lista:
#         if nr > 0:
#             numere_poz.append(nr)
#     return numere_poz
# # lista = (input(" Introduceti o lista cu nr pozitive si negative. Ex.: [0, -2, 22, -11, 38]: ")) nu merge, definesc o lista
# lista = [10, 22, -8, -22, 28, 66, 0, -99]
# print(ret_nr_poz())


# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

print("   Exercitiul 9\n")
def nu_returneaza(x, y):
    if x > y:
        print(f"Primul număr {x} este mai mare decat al doilea nr {y}")
    elif x < y:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    else:
        print('Numerele sunt egale')
x = int(input("Introduceti primul numar: "))
y = int(input("Introduceti al doilea numar: "))
nu_returneaza(x, y)



# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False
# print("   Exercitiul 10\n")
# def



