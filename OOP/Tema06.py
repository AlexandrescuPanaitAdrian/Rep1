# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()


# class Cerc:
#
#     #constructor
#     def __init__(self, raza, culoare):
#        self.r = raza
#        self.cul = culoare
#
#     #metode
#     def aria(self):
#        return 3.14 * self.r ** 2
#     def dia(self):
#        return 2 * self.r
#     def circ(self):
#        return 3.14 * self.r * 2
#
#     def proprietati_cerc(self):
#         return(f'\n Proprietatile cercului ==> Raza: {self.r}, Culoarea: {self.cul}, '
#                f'Diametrul: {self.dia()}, Aria: {self.aria()}, Circumferinta: {self.circ()}')
#
# cerc_alb = Cerc(3, 'alb')
# print(cerc_alb.proprietati_cerc())
# cerc_verde = Cerc(1, 'verde')
# print(cerc_verde.proprietati_cerc())
# cerc_rosu = Cerc(2, 'rosu')
# print(cerc_rosu.proprietati_cerc())



# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().


# class Dreptunghi:
#
#     def __init__(self, lungime, latime, culoare):
#         self.lun = lungime
#         self.lat = latime
#         self.culoare = culoare
#
#     def descriere_dreptunghi(self):
#         return (f" Dreptunghiul {self.culoare} are lungimea: {self.lun}, latimea: {self.lat}, "
#                 f"aria: {self.aria()}, perimetrul: {self.perimetru()}")
#
#     def aria(self):
#         return self.lat * self.lun
#     def perimetru(self):
#         return 2 * self.lun + 2* self.lat
#     def schimba_culoare(self, noua_culoare=" "):
#         noua_culoare = input('Introdu noua culoare: ')
#         self.culoare = noua_culoare
#
# drept_alb = Dreptunghi(3, 2, "alb")
# print(drept_alb.descriere_dreptunghi())
# print(f"{drept_alb.schimba_culoare()} Noul dreptunghi este: {drept_alb.descriere_dreptunghi()}")  # apare un "None"


# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)
#
#
# class Angajat:
#
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         print(f"Angajat==> Nume: {self.nume} Prenume: {self.prenume} Salariu: {self.salariu}")
#
#     def nume_complet(self):
#         print(f"Nume complet: {self.nume} {self.prenume}")
#
#     def salariu_lunar(self):
#         print(f"Salariu lunar: {self.salariu}")
#
#     def salariu_anual(self):
#         print(f"Salariul anual: {self.salariu * 12}")
#
#     def marire_salariu(self, procent):
#         self.procent = procent
#         return (self.salariu * ( 100 + self.procent)/100)
#
# marca1 = Angajat("Pompilian", "Ioana", 3000)
# print("Marca nr.1")
# marca1.descrie()
# marca1.nume_complet()
# marca1.salariu_lunar()
# marca1.salariu_anual()
# print(f"Salariu marit: {marca1.marire_salariu(8)}")
# print()



# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)


# print("\n Exercitiul 4")
# class Cont:
#
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#     def afisare_sold(self):
#         print(f"\n Titularul {self.titular_cont} are in contul: {self.iban} suma de: {self.sold} lei")
#
#     def debitare_cont(self):
#         suma = int(input("Introduceti suma pe care doriti sa o retrageti: "))
#         self.sold = self.sold - suma
#         print(f"Ati retras suma: {suma} lei")
#         print(f"Aveti soldul de: {self.sold} lei")
#
#     def creditare_cont(self):
#         suma = int(input("\n Introduceti suma pe care doriti sa o depuneti in cont: "))
#         self.sold = self.sold + suma
#         print(f"Suma depusa este: {suma} lei")
#         print(f"Aveti soldul de: {self.sold} lei")
#
# client_1 = Cont("112233445566", "Popescu Virgil", 8000)
# client_1.afisare_sold()
# client_1.debitare_cont()
# client_1.creditare_cont()
# print()





# ========================================================================
#
# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
#
#
#
# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0
#
#
# 3. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
# printăm detalii suplimentare.
# ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
# adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict