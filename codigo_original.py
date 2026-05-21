import time

inicio = time.time()

primos = []

for n in range(2, 10000):
    es_primo = True

    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break

    if es_primo:
        primos.append(n)

fin = time.time()

print("Cantidad de primos:", len(primos))
print("Tiempo de ejecución:", fin - inicio)