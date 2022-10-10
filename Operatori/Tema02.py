# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.

'''
  In cazul lui IF ELSE sunt intotdeauna doua ramuri :
  prima:   IF (conditie) este indeplinita atunci:
               executa codul
  a doua: ELSE:
              executa codul daca conditia nu este indeplinita
'''

# # 2. Verifică și afișează dacă x este număr natural sau nu.
#
# x = int(input("Introdu un numar intreg: \n")) # numerele naturale sunt numere intregi de la 0 inlcusiv la infinit
# if x >= 0:
#     print(f"{x} este numar natural")
# else:
#     print(f"{x} nu este numar natural")


# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.

# x = int(input("Introdu un numar intreg: \n"))
# if x > 0:
#     print(f"{x} este numar pozitiv")
# elif x < 0:
#     print(f"{x} este numar negativ")
# else:
#     print(f"{x} este numar neutru")

# 4. Verifică și afișează dacă x este între -2 și 13.

# x = int(input("Introdu un numar intreg: \n"))
# if  x < -2 :
#     print("este mai mic de -2")
# elif x < 13:
#     print("este intre -2 si 13")
# else:
#     print("este numar mai mare decat 13")

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.

# x = int(input("Introdu un numar intreg x: \n"))
# y = int(input("Introdu un numar intreg y: \n"))
# z = x - y
# if  z < 5 :
#     print("diferenta este mai mica de 5")
# else:
#     print("diferenta este prea mare")

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.

# x = int(input("Introdu un numar intreg: \n"))
# if not x > 5 :
#     print("nu este in interval")
# elif not x > 27:
#     print("este intre 5 si 27")
# else:
#     print("nu este in interval")

# 7.
# x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
# mare.

# x = int(input("Introdu un numar intreg x: \n"))
# y = int(input("Introdu un numar intreg y: \n"))
#
# if  x < y :
#     print("x este mai mic decat y \n")
# elif x > y:
#     print("x este mai mare decat y \n")
# else:
#     print("x = y")

# 8.
# X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

# x = int(input("Introdu lungimea laturii x: \n"))
# y = int(input("Introdu lungimea laturii y: \n"))
# z = int(input("Introdu lungimea laturii z: \n"))
#
# if  x == y and y == z:
#     print("triunhiul este echilateral \n")
# elif x == y:
#     print("triunhiul este isoscel \n")
# elif x == z:
#     print("triunhiul este isoscel \n")
# elif y == z:
#     print("triunhiul este isoscel \n")
# else:
#     print("triunghiul este unul oarecare")

# 9. Citește o literă de la tastatură
# Verifică și afișează dacă este vocală sau nu

# a = input("Introduceti o litera de la tastatura: \n")
# vocala = ["a", "e", "i", "o", "u"]
# for i in range(0, len(vocala)):
#          if a == vocala[i]:
#             print(f"{a} este o vocala\n")
#             break
# else:
#     print("Ati introdus o consoana")

  ## metoda cu IF


# litera_tastatura = input("Introduceti o litera de la tastatura: \n")
# if litera_tastatura == "a":
#     print(f"Ati introdus vocala {litera_tastatura}\n")
# elif litera_tastatura == "e":
#     print(f"Ati introdus vocala {litera_tastatura}\n")
# elif litera_tastatura == "i":
#     print(f"Ati introdus vocala {litera_tastatura}\n")
# elif litera_tastatura == "o":
#     print(f"Ati introdus vocala {litera_tastatura}\n")
# elif litera_tastatura == "u":
#     print(f"Ati introdus vocala {litera_tastatura}\n")
# else:
#     print(f"Ati introdus o consoana\n")


# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 5 => E
# 4 sau sub => F!

# print(" * - * - * - * - * - * ")
# nota = int(input("Introduceti de la tastatura nota in sistem romanesc: \n"))
# if nota > 9:
#     nota = str("A")
#     print(f"Nota echivaleaza cu calificativul {nota}\n")
# elif nota > 8:
#     nota = str("B")
#     print(f"Nota echivaleaza cu calificativul {nota}\n")
# elif nota > 7:
#     nota = str("C")
#     print(f"Nota echivaleaza cu calificativul {nota}\n")
# elif nota > 6:
#     nota = str("D")
#     print(f"Nota echivaleaza cu calificativul {nota}\n")
# elif nota > 5:
#     nota = str("E")
#     print(f"Nota echivaleaza cu calificativul {nota}\n")
# else:
#      nota <= 4
#      nota = str("F")
#      print(f"Nota echivaleaza cu calificativul {nota}\n")
# print("- Intrebare de incheiere: Care sistem va place mai mult?")
