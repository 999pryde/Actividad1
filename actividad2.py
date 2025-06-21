import os
os.system("cls")

from funciones import solicitar_nota, calcular_promedio, solicitar_numero
#programa principal desde aqui
notas = []
total_notas = solicitar_nota("Ingresa cantidad de notas: ")
for i in range(total_notas):
    nota = solicitar_nota()
    notas.append()