import time
import math

inicio = time.time()

primos = []

for n in range(2, 100000):

    es_primo = True

    for i in range(2, int(math.sqrt(n)) + 1):

        if n % i == 0:
            es_primo = False
            break

    if es_primo:
        primos.append(n)

fin = time.time()

print("Cantidad de primos:", len(primos))
print("Tiempo optimizado:", fin - inicio)