import matplotlib.pyplot as plt

original = 37.44
optimizado = 0.33

nombres = ["Original", "Optimizado"]
tiempos = [original, optimizado]

plt.bar(nombres, tiempos)

plt.title("Comparación de tiempos de ejecución")
plt.xlabel("Código")
plt.ylabel("Tiempo (segundos)")

plt.savefig("grafico.png")

print("Gráfico guardado correctamente.")