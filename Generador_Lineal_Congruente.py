def generador_glc(a, c, m, X0, N):
    # Inicializa el valor actual
    Xn = X0
    
    # Inicializa una lista para almacenar los valores generados
    valores_generados = []
    
    # Inicializa el contador de iteraciones
    periodo = 0
    
    for _ in range(N):
        # Calcula el siguiente valor en la secuencia
        Xn = (a * Xn + c) % m
        
        # Incrementa el contador de iteraciones
        periodo += 1
        
        # Almacena el valor generado
        valores_generados.append(Xn)
    
    return valores_generados, periodo

# Generar números pseudoaleatorios y calcular el periodo
c=127
a= 9
m=128
X0=1
valores_generados, periodo = generador_glc(a, c, m, X0, 200)

# Mostrar los valores generados y el periodo
print("Valores generados:", valores_generados)
print("Periodo:", periodo)
