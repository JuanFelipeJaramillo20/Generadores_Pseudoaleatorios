import numpy as np
from Generador_Estandar_Minimo import generador_lcg
from Generador_Lineal_Congruente import generador_glc
from Pruebas import (
    prueba_chi_cuadrado,
    prueba_kolmogorov_smirnov,
    prueba_corridas,
    prueba_series,
    prueba_poker,
)

a = 106
c = 1238
m = 6075
X0 = 12345
N = 10000  # Cantidad de números pseudoaleatorios a generar

# Generar números pseudoaleatorios utilizando el Generador Lineal Congruente (GLC)
valores_glc, periodo_glc = generador_glc(a, c, m, X0, N)

# Generar números pseudoaleatorios utilizando el Generador de Estándar Mínimo (LCG)
valores_lcg, periodo_lcg = generador_lcg(a, m, X0, N)

# Realizar pruebas de Chi-cuadrado y Kolmogorov-Smirnov para GLC
print("Pruebas para GLC:")
resultado_chi_cuadrado_glc = prueba_chi_cuadrado(valores_glc, num_bins=10)
resultado_ks_glc = prueba_kolmogorov_smirnov(valores_glc)

# Realizar pruebas de Chi-cuadrado y Kolmogorov-Smirnov para LCG
print("\nPruebas para LCG:")
resultado_chi_cuadrado_lcg = prueba_chi_cuadrado(valores_lcg, num_bins=10)
resultado_ks_lcg = prueba_kolmogorov_smirnov(valores_lcg)

# Realizar prueba de Corridas para GLC
print("\nPrueba de Corridas para GLC:")
resultado_corridas_glc = prueba_corridas(valores_glc)

# Realizar prueba de Corridas para LCG
print("\nPrueba de Corridas para LCG:")
resultado_corridas_lcg = prueba_corridas(valores_lcg)

# Definir la cantidad de datos a muestrear y el tamaño de la muestra
cantidad_datos_a_muestrear = 10 # Cambia este valor según tus necesidades
tamano_muestra = 10  # Cambia este valor según tus necesidades
muestra_glc = np.random.choice(valores_glc[:cantidad_datos_a_muestrear], size=tamano_muestra, replace=False)
muestra_lcg = np.random.choice(valores_lcg[:cantidad_datos_a_muestrear], size=tamano_muestra, replace=False)

# Realizar prueba de Series para GLC
print("\nPrueba de Series para GLC:")
resultado_series_glc = prueba_series(valores_glc)

# Realizar prueba de Series para LCG
print("\nPrueba de Series para LCG:")
resultado_series_lcg = prueba_series(valores_lcg)

# Realizar prueba de Póker para GLC (3-cartas)
print("\nPrueba de Póker para GLC (3-cartas):")
resultado_poker_glc_3 = prueba_poker(valores_glc, mano_length=3)

# Realizar prueba de Póker para GLC (5-cartas)
print("\nPrueba de Póker para GLC (5-cartas):")
resultado_poker_glc_5 = prueba_poker(valores_glc, mano_length=5)

# Realizar prueba de Póker para LCG (3-cartas)
print("\nPrueba de Póker para LCG (3-cartas):")
resultado_poker_lcg_3 = prueba_poker(valores_lcg, mano_length=3)

# Realizar prueba de Póker para LCG (5-cartas)
print("\nPrueba de Póker para LCG (5-cartas):")
resultado_poker_lcg_5 = prueba_poker(valores_lcg, mano_length=5)

# Recopilar resultados en un diccionario
resultados_pruebas_glc = {
    'chi_cuadrado': resultado_chi_cuadrado_glc,
    'kolmogorov_smirnov': resultado_ks_glc,
    'corridas': resultado_corridas_glc,
    'series': resultado_series_glc,
    'poker_3': resultado_poker_glc_3,
    'poker_5': resultado_poker_glc_5,
}

resultados_pruebas_lcg = {
    'chi_cuadrado': resultado_chi_cuadrado_lcg,
    'kolmogorov_smirnov': resultado_ks_lcg,
    'corridas': resultado_corridas_lcg,
    'series': resultado_series_lcg,
    'poker_3': resultado_poker_lcg_3,
    'poker_5': resultado_poker_lcg_5,
}
        
def evaluar_resultados(resultados, valor_critico=0.05):
    print(resultados)
    for prueba, resultado in resultados.items():
        if resultado is None or resultado == 0:
            print(f"{prueba}: No se pudo evaluar")
        elif isinstance(resultado, dict):
            nombre = resultado.get('nombre', 'Nombre no proporcionado')
            p_value = resultado.get('p_value', 'Valor p no proporcionado')
            mensaje = resultado.get('mensaje', 'Mensaje no proporcionado')

            if p_value != 'Valor p no proporcionado':
                if p_value > valor_critico:
                    mensaje = 'Bueno'
                else:
                    mensaje = 'Malo'

            print(f"{nombre}: {mensaje} (p-value: {p_value})")
        elif isinstance(resultado, list):
            for i, res in enumerate(resultado, start=1):
                if isinstance(res, dict):
                    nombre = res.get('nombre', 'Nombre no proporcionado')
                    p_value = res.get('p_value', 'Valor p no proporcionado')
                    mensaje = res.get('mensaje', 'Mensaje no proporcionado')

                    if p_value != 'Valor p no proporcionado':
                        if p_value > valor_critico:
                            mensaje = 'Bueno'
                        else:
                            mensaje = 'Malo'

                    print(f"Prueba de Póker {i} ({prueba}): {mensaje} (p-value: {p_value})")
                else:
                    print(f"Prueba de Póker {i} ({prueba}): Datos en formato incorrecto")
        else:
            print(f"{prueba}: Datos en formato incorrecto")


# Mostrar resultados de evaluación
print("\nEvaluación del Generador GLC:")
evaluar_resultados(resultados_pruebas_glc)

print("\nEvaluación del Generador LCG:")
evaluar_resultados(resultados_pruebas_lcg)
