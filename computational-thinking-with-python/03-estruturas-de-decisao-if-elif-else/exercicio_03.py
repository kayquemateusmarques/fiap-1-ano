import os
os.system("cls")

v_um = float(input("Digite o primeiro valor: "))
v_dois = float(input("Digite o segundo valor: "))
v_tres = float(input("Digite o terceiro valor: "))
if v_um > v_dois and v_um > v_tres:
    print(f"{v_um} é o primeiro e maior valor.")
elif v_dois > v_um and v_dois > v_tres:
    print(f"{v_dois} é o segundo e maior valor.")
else:
    print(f"{v_tres} é o terceiro e maior valor.")