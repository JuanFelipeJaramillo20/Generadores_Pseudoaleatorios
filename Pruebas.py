import scipy.stats as stats
import numpy as np

def prueba_chi_cuadrado(datos, num_bins):
        # Realizar la prueba de Chi-cuadrado
    chi_squared, p_value = stats.chisquare(np.histogram(datos, bins=num_bins)[0])
    return {
        'nombre': 'Prueba de Chi-cuadrado',
        'p_value': p_value,
    }
        # Mostrar resultados en una tabla
    # print("Prueba de Chi-cuadrado (X²):")
    # print("Grados de libertad:", num_bins - 1)
    # print("Estadístico de prueba (X²):", chi_squared)
    # print("Valor p:", p_value)
    
def prueba_kolmogorov_smirnov(datos):
    # Realizar la prueba de Kolmogorov-Smirnov
    response = stats.kstest(datos, 'uniform')
    ks_statistic, ks_p_value = stats.kstest(datos, 'uniform')
    return {
        'nombre': 'Prueba de Kolmogorov Smirnov',
        'p_value': ks_p_value,
    }
    # Mostrar resultados en una tabla
    #print("Prueba de Kolmogorov-Smirnov:")
    #print("Estadístico de prueba (D):", ks_statistic)
    #print("Valor p:", ks_p_value)

def prueba_corridas(datos):
    # Calcula las corridas en los datos
    corridas = []
    corrida_actual = datos[0]
    longitud_corrida = 1
    
    for i in range(1, len(datos)):
        if datos[i] != corrida_actual:
            corridas.append(longitud_corrida)
            corrida_actual = datos[i]
            longitud_corrida = 1
        else:
            longitud_corrida += 1
    
    # Agrega la longitud de la última corrida
    corridas.append(longitud_corrida)
    return {
        'nombre': 'Prueba de Corridas',
        'p_value': longitud_corrida,
    }
    # Muestra la longitud de las corridas encontradas
    print("Longitud de las corridas encontradas:", corridas)

def prueba_series(datos):
    # Calcula las frecuencias esperadas (FE) para cada serie
    num_series = len(set(datos))
    fe = len(datos) / num_series
    
    # Calcula la tabla de chi-cuadrado
    chi_cuadrado = sum([(f - fe) ** 2 / fe for f in np.bincount(datos)])
    
    # Muestra la tabla de frecuencias esperadas (FE)
    print("Tabla de Frecuencias Esperadas (FE):")
    for i in range(1, num_series + 1):
        print(f"FE para serie {i}: {fe}")
    

        return {
        'nombre': 'Prueba de Series',
        'p_value': chi_cuadrado,
    }
    # Muestra la tabla de Chi-cuadrado
    print("\nTabla de Chi-cuadrado:")
    print("Valor Chi-cuadrado:", chi_cuadrado)

def prueba_poker(datos, mano_length):
    def contar_ocurrencias(mano):
        ocurrencias = {}
        for carta in mano:
            if carta in ocurrencias:
                ocurrencias[carta] += 1
            else:
                ocurrencias[carta] = 1
        return ocurrencias

    def es_poker(mano):
        ocurrencias = contar_ocurrencias(mano)
        for valor, cantidad in ocurrencias.items():
            if cantidad == 4:
                return "Póker"
        return "Nada"

    def es_full_house(mano):
        ocurrencias = contar_ocurrencias(mano)
        tiene_tres = False
        tiene_dos = False
        for cantidad in ocurrencias.values():
            if cantidad == 3:
                tiene_tres = True
            elif cantidad == 2:
                tiene_dos = True
        if tiene_tres and tiene_dos:
            return "Full House"
        return "Nada"

    # Divide los datos en manos de la longitud deseada
    manos = [datos[i:i + mano_length] for i in range(0, len(datos), mano_length)]

    # Evalúa cada mano de póker y devuelve los resultados
    resultados = []
    nada = 0
    full = 0
    poker = 0
    for i, mano in enumerate(manos, start=1):
        poker_resultado = es_poker(mano)
        full_house_resultado = es_full_house(mano)
        if poker_resultado == "Póker":
            resultados.append(f"Mano {i}: Póker")
            poker += 1
        elif full_house_resultado == "Full House":
            resultados.append(f"Mano {i}: Full House")
            full += 1
        else:
            resultados.append(f"Mano {i}: Nada")
            nada += 1
    

        cantidades = {
        "Nada": nada,
        "Full House": full,
        "Poker": poker
    }
    
    return cantidades  # Devuelve los resultados de las manos de póker


