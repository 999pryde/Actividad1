import os
os.system("cls")

#- programa python que solicita 5 notas
#- guarda las 5 notas en una lista
#- muestra el promedio (debe ser funcion)

lista= []

def solicitar_nota():
    while True:
        try:
            numero = float(input("Ingresar nota: "))
            if numero >= 1 and numero <= 7:
                return numero
        except:
            print("Nota de ser numero")

def calcular_promedio(lista):
    sumatoria = 0
    for i in lista:
        sumatoria+=i
    return sumatoria/len(lista)

#programa principal desde aqui
notas = []
for i in range(5):
    nota = solicitar_nota()
    notas.append(nota)
promedio = calcular_promedio(notas)
print(f"Promedio {promedio}")
