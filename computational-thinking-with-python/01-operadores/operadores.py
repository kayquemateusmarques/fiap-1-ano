# Lista de exercícios parte 1
# Nível 1 - Operações com int
print("A)",(4 + 10 % 3))                         #A) 5
print("B)",(8 + 3 * 2))                          #B) 14
print("C)",(20 // 3 + 2))                        #C) 8
print("D)",(15 % 4 * 2))                         #D) 6
print("E)",(2 ** 3 + 4))                         #E) 12
print("F)",(18 // 4 * 2))                        #F) 8
print("G)",(10 - 3 * 2 + 5))                     #G) 9

# Nível 2 – Operações com int e float
print("H)",(5 + 2.5 * 2))                        #H) 10.0
print("I)",(10 / 4 + 3))                         #I) 5.5
print("J)",(7.5 + 2 * 3))                        #J) 13.5
print("K)",(20 / 4 + 2.5))                       #K) 7.5
print("L)",(10.0 // 3 + 1))                      #L) 4.0
print("M)",(2.5 ** 2 + 1))                       #M) 7.25
print("N)",(15 % 4 + 2.5))                       #N) 5.5

# Nível 3 – Operações com str
print("O)",("Python" + "3"))                     #O) Python3
print("P)", ("Py" * 3))                          #P) PyPyPy
print("Q)", ("10" + "5"))                        #Q) 105
print("R)", ("A" * 4 + "B"))                     #R) AAAAB
print("S)", ("Python" + "!" * 3))                #S) Python!!!
print("T)", ("=" * 5 + " Python " + "=" * 5))    #T) ===== Python =====

# Lista de exercícios parte 2
# Nível 1 – Cuidado com a precedência!
print("A)",(2 + 3 * 4))                          #A) 14
print("B)",((2 + 3) * 4))                        #B) 20
print("C)",(20 - 8 / 2 * 3))                     #C) 8.0
print("D)",(10 + 15 % 4 * 2))                    #D) 12
print("E)",(2 * 3 ** 2))                         #E) 18
print("F)",((2 * 3) ** 2))                       #F) 36
print("G)",(20 // 3 + 20 % 3))                   #G) 7

# Nível 2 – Divisão, módulo e potência
print("H)",(5 / 2 * 2))                          #H) 5.0
print("I)",(5 // 2 * 2))                         #I) 4
print("J)",(10 / 2 + 3.0))                       #J) 8.0
print("K)",(2 ** 3 ** 2))                        #K) 512
print("L)",(10 % 4 ** 2))                        #L) 10
print("M)",(20 // 6 * 2.0))                      #M) 6.0
print("N)",((15 % 4) ** 2 + 1))                  #N) 2

# Nível 3 – Strings também usam operadores!
print("O)",("2" + "3" * 2))                      #O) 233
print("P)", (("2" + "3") * 2))                   #P) 2323
print("Q)", ("Python" + "!" * 3))                #Q) Python!!!
print("R)", ("A" * 4 + "B"))                     #R) AAAAB
print("S)", ("10" * 2 + "5"))                    #S) 10105

# Nível 4 - Será que funciona?
print("S)", ("10" + 5))                          #S) Não funciona, pois não é possível concatenar str com int
print("T)", ("Python" * 2.5))                    #T) Não funciona, pois o multiplicador precisaria ser um int