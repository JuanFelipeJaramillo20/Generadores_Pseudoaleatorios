import random
import matplotlib.pyplot as plt

def generar_lista_aleatoria(size):
    lista_aleatoria = [random.random() for _ in range(size)]
    # Extraer las coordenadas x e y de los valores generados
    x_valores = lista_aleatoria[:-1]  # Usar todos los valores excepto el último
    y_valores = lista_aleatoria[1:]   # Usar todos los valores excepto el primero
    # Crear un gráfico de dispersión con valores generados
    plt.figure(figsize=(12, 4))
    plt.scatter(x_valores, y_valores, marker='o', s=5)
    plt.title('Gráfico de Dispersión de Valores Generados (Valores originales)')
    plt.xlabel('Valor actual (Xn)')
    plt.ylabel('Siguiente valor (Xn+1)')
    plt.show()
    return lista_aleatoria


#size = 10  # size deseado de la lista
#lista_aleatoria = generar_lista_aleatoria(10)
#print(lista_aleatoria)
