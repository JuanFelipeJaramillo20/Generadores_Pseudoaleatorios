import matplotlib.pyplot as plt


def generador_glc(a, c, m, X0, N):
    Xn = X0
    valores_generados = []
    valores_unicos = set()
    periodo = None

    for i in range(N):
        Xn = (a * Xn + c) % m
        valores_generados.append(Xn)
        if Xn in valores_unicos:
            periodo = i
            break

        valores_unicos.add(Xn)

    return valores_generados, periodo


def run_glc(a, c, m, X0, N):
    valores_generados, periodo = generador_glc(a, c, m, X0, N)

    datos_rn = []
    for dato in valores_generados:
        datos_rn.append(dato / m)

    # Mostrar los valores generados y el periodo
    print("Valores generados:", valores_generados)
    print("Periodo:", periodo)

    # Extraer las coordenadas x e y de los valores generados
    x_valores = valores_generados[:-1]  # Usar todos los valores excepto el último
    y_valores = valores_generados[1:]   # Usar todos los valores excepto el primero

    # Crear un gráfico de dispersión con valores generados
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.scatter(x_valores, y_valores, marker='o', s=5)
    plt.title('Gráfico de Dispersión de Valores Generados (Valores originales)')
    plt.xlabel('Valor actual (Xn)')
    plt.ylabel('Siguiente valor (Xn+1)')
    plt.grid(True)

    # Extraer las coordenadas x e y de los valores en datos_rn
    x_valores_rn = datos_rn[:-1]  # Usar todos los valores excepto el último
    y_valores_rn = datos_rn[1:]   # Usar todos los valores excepto el primero

    # Crear un gráfico de dispersión con valores normalizados (datos_rn)
    plt.subplot(1, 2, 2)
    plt.scatter(x_valores_rn, y_valores_rn, marker='o', s=5)
    plt.title('Gráfico de Dispersión de Valores Generados (Valores normalizados)')
    plt.xlabel('Valor actual (Xn)')
    plt.ylabel('Siguiente valor (Xn+1)')
    plt.grid(True)

    # Mostrar ambos gráficos
    plt.tight_layout()
    plt.show()
    return valores_generados, periodo

""" c=127
a= 9
m=128
X0=1 """
