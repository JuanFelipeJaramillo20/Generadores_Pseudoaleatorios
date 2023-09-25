import math
import matplotlib.pyplot as plt

def plot_2d_table(table, fe):
    rows = list(table.keys())
    cols = list(table[rows[0]].keys())
    values = [[round(table[row][col],5) for col in cols] for row in rows]
    values2 = [[fe] * len(cols) for _ in range(len(rows))]
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax.matshow(values, cmap="binary")
    ax2.matshow(values2, cmap="binary")

    for i in range(len(rows)):
        for j in range(len(cols)):
            ax.text(j, i, str(values[i][j]), va="center", ha="center", color="red")
            ax2.text(j, i, str(values2[i][j]), va="center", ha="center", color="black")

    ax.set_xticks(range(len(cols)))
    ax.set_xticklabels(cols)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels(rows)
    ax.set_xlabel('Columnas')
    ax.set_ylabel('Filas')
    plt.xlabel('Columnas')
    plt.ylabel('Filas')
    ax.set_title('Frecuencias Obtenidas')
    ax2.set_xticks(range(len(cols)))
    ax2.set_xticklabels(cols)
    ax2.set_yticks(range(len(rows)))
    ax2.set_yticklabels(rows)
    ax2.set_xlabel('Columnas')
    ax2.set_ylabel('Filas')
    ax2.set_title('Frecuencias Esperadas')
    
    plt.tight_layout()
    plt.show()

def prueba_chi_cuadrado(datos, m=1):
    datos_rn = []
    for dato in datos:
        datos_rn.append(dato / m)
    fo = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        '10': 0
    }
    for dato in datos_rn:
        if dato >= 0.0 and dato < 0.1:
            fo['1'] += 1
        elif dato >= 0.1 and dato < 0.2:
            fo['2'] += 1
        elif dato >= 0.2 and dato < 0.3:
            fo['3'] += 1
        elif dato >= 0.3 and dato < 0.4:
            fo['4'] += 1
        elif dato >= 0.4 and dato < 0.5:
            fo['5'] += 1
        elif dato >= 0.5 and dato < 0.6:
            fo['6'] += 1
        elif dato >= 0.6 and dato < 0.7:
            fo['7'] += 1
        elif dato >= 0.7 and dato < 0.8:
            fo['8'] += 1
        elif dato >= 0.8 and dato < 0.9:
            fo['9'] += 1
        elif dato >= 0.9 and dato < 1:
            fo['10'] += 1

    fe = len(datos) / 10
    resultados = {
        '1': (((fe - fo['1'])**2) / fe),
        '2': (((fe - fo['2'])**2) / fe),
        '3': (((fe - fo['3'])**2) / fe),
        '4': (((fe - fo['4'])**2) / fe),
        '5': (((fe - fo['5'])**2) / fe),
        '6': (((fe - fo['6'])**2) / fe),
        '7': (((fe - fo['7'])**2) / fe),
        '8': (((fe - fo['8'])**2) / fe),
        '9': (((fe - fo['9'])**2) / fe),
        '10': (((fe - fo['10'])**2) / fe)
    }

    chi_cuadrado = 0
    for resultado in resultados:
        chi_cuadrado += resultados[resultado]
    
    chi_cuadrado_critico = 16.919
    resultado_string = "El generador pasó la prueba de X²" if chi_cuadrado <= chi_cuadrado_critico else "El generador falló la prueba de X²"
    print('Chi cuadrada',chi_cuadrado,'Chi critica:',chi_cuadrado_critico, resultado_string)
    #print("DATOS RN", datos_rn)

   # Crear la tabla de frecuencias
    intervalos = ['0 - 0.1', '0.1 - 0.2', '0.2 - 0.3', '0.3 - 0.4', '0.4 - 0.5', '0.5 - 0.6', '0.6 - 0.7', '0.7 - 0.8', '0.8 - 0.9', '0.9 - 1', 'Sumatoria']
    frecuencias_obtenidas = [fo[str(i)] for i in range(1, 11)] + [sum(fo.values())]
    frecuencias_esperadas = [fe] * 10 + [len(datos)]
    calculos = [resultados[str(i)] for i in range(1, 11)] + [chi_cuadrado]

    # Crear la tabla de frecuencias en un formato que pueda usarse para el gráfico
    tabla_frecuencias = {
        'Intervalos': intervalos,
        'Frecuencia Obtenida': frecuencias_obtenidas,
        'Frecuencia Esperada': frecuencias_esperadas,
        'Cálculos': calculos
    }

    # Convertir el diccionario a una lista de listas
    tabla_frecuencias_values = [list(tabla_frecuencias.keys())] + list(zip(*tabla_frecuencias.values()))

    # Crear el gráfico de barras de la tabla de frecuencias
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=tabla_frecuencias_values, loc='center', cellLoc='center')

    # Mostrar el gráfico de barras de la tabla de frecuencias
    plt.title('Tabla de Frecuencias')
    plt.show()


#prueba_chi_cuadrado(datos, periodo)
    
def prueba_kolmogorov_smirnov(datos, m=1):
    cantidad_datos = len(datos)
    d_critico = 1.36 / math.sqrt(cantidad_datos)
    datos_rn = []
    for dato in datos:
        datos_rn.append(dato / m)
    
    fo = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        '10': 0
    }

    for dato in datos_rn:
        if dato >= 0.0 and dato < 0.1:
            fo['1'] += 1
        elif dato >= 0.1 and dato < 0.2:
            fo['2'] += 1
        elif dato >= 0.2 and dato < 0.3:
            fo['3'] += 1
        elif dato >= 0.3 and dato < 0.4:
            fo['4'] += 1
        elif dato >= 0.4 and dato < 0.5:
            fo['5'] += 1
        elif dato >= 0.5 and dato < 0.6:
            fo['6'] += 1
        elif dato >= 0.6 and dato < 0.7:
            fo['7'] += 1
        elif dato >= 0.7 and dato < 0.8:
            fo['8'] += 1
        elif dato >= 0.8 and dato < 0.9:
            fo['9'] += 1
        elif dato >= 0.9 and dato < 1:
            fo['10'] += 1

    foa = {
        '1': fo['1'],
        '2': fo['1'] + fo['2'],
        '3': fo['1'] + fo['2'] + fo['3'],
        '4': fo['1'] + fo['2'] + fo['3'] + fo['4'],
        '5': fo['1'] + fo['2'] + fo['3'] + fo['4'] + fo['5'],
        '6': fo['1'] + fo['2'] + fo['3'] + fo['4'] + fo['5'] + fo['6'],
        '7': fo['1'] + fo['2'] + fo['3'] + fo['4'] + fo['5'] + fo['6'] + fo['7'],
        '8': fo['1'] + fo['2'] + fo['3'] + fo['4'] + fo['5'] + fo['6'] + fo['7'] + fo['8'],
        '9': fo['1'] + fo['2'] + fo['3'] + fo['4'] + fo['5'] + fo['6'] + fo['7'] + fo['8'] + fo['9'],
        '10': fo['1'] + fo['2'] + fo['3'] + fo['4'] + fo['5'] + fo['6'] + fo['7'] + fo['8'] + fo['9'] + fo['10']
    }

    pea = {
        '1': 0.1,
        '2': 0.2,
        '3': 0.3,
        '4': 0.4,
        '5': 0.5,
        '6': 0.6,
        '7': 0.7,
        '8': 0.8,
        '9': 0.9,
        '10': 1,
    }

    poa = {
        '1': (fo['1'] / cantidad_datos),
        '2': (fo['1'] + fo['2']) / cantidad_datos,
        '3': (fo['1'] + fo['2'] + fo['3']) / cantidad_datos,
        '4': (fo['1'] + fo['2'] + fo['3'] + fo['4']) / cantidad_datos,
        '5': (fo['1'] + fo['2'] + fo['3'] + fo['4'] + fo['5']) / cantidad_datos,
        '6': (fo['1'] + fo['2'] + fo['3'] + fo['4'] + fo['5'] + fo['6']) / cantidad_datos,
        '7': (fo['1'] + fo['2'] + fo['3'] + fo['4'] + fo['5'] + fo['6'] + fo['7']) / cantidad_datos,
        '8': (fo['1'] + fo['2'] + fo['3'] + fo['4'] + fo['5'] + fo['6'] + fo['7'] + fo['8']) / cantidad_datos,
        '9': (fo['1'] + fo['2'] + fo['3'] + fo['4'] + fo['5'] + fo['6'] + fo['7'] + fo['8'] + fo['9']) / cantidad_datos,
        '10': 1,
    }

    resultados = {
        '1': abs(pea['1'] - poa['1']),
        '2': abs(pea['2'] - poa['2']),
        '3': abs(pea['3'] - poa['3']),
        '4': abs(pea['4'] - poa['4']),
        '5': abs(pea['5'] - poa['5']),
        '6': abs(pea['6'] - poa['6']),
        '7': abs(pea['7'] - poa['7']),
        '8': abs(pea['8'] - poa['8']),
        '9': abs(pea['9'] - poa['9']),
        '10': abs(pea['10'] - poa['10']),
    }

    d_total = 0

    for resultado in resultados:
        d_total += resultados[resultado]

    resultado_string = "El generador pasó la prueba de Kolmogorov-Smirnov" if d_total <= d_critico else "El generador falló la prueba de Kolmogorov-Smirnov"
    print("VALOR CRITICO:", d_critico)
    print("VALOR OBTENIDO:", d_total)
    print(resultado_string)

    # Crear la tabla de frecuencias para el gráfico
    intervalos = ['0 - 0.1', '0.1 - 0.2', '0.2 - 0.3', '0.3 - 0.4', '0.4 - 0.5', '0.5 - 0.6', '0.6 - 0.7', '0.7 - 0.8', '0.8 - 0.9', '0.9 - 1', 'Sumatoria']
    fo_values = [fo[str(i)] for i in range(1, 11)] + [sum(fo.values())]
    poa_values = [poa[str(i)] for i in range(1, 11)] + [1]

    # Asegúrate de que colLabels tenga la misma longitud que la cantidad de columnas en tabla_frecuencias
    colLabels = ['Intervalos', 'Frecuencia Observada', 'Frecuencia Acumulada Esperada']

    # Crear el gráfico de barras de la tabla de frecuencias
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('tight')
    ax.axis('off')
    tabla_frecuencias = [colLabels] + list(zip(intervalos, fo_values, poa_values))
    ax.table(cellText=tabla_frecuencias, loc='center', cellLoc='center', colLabels=colLabels)

    # Mostrar el gráfico de barras de la tabla de frecuencias
    plt.title('Tabla de Frecuencias para Kolmogorov-Smirnov')
    plt.show()
#prueba_kolmogorov_smirnov(datos, 128)

def prueba_corridas(datos, m=1):
    datos_rn = []
    cantidad_datos = len(datos)
    for dato in datos:
        datos_rn.append(dato / m)
    comportamiento = ['*']
    for index, dato in enumerate(datos_rn):
        if index >= 1:
            caso_actual = '+' if datos_rn[index - 1] < dato else '-'
            comportamiento.append(caso_actual)

    corridas_count = 0
    current_run = comportamiento[0]
    run_lengths = []  # Lista para almacenar las longitudes de las corridas
    aux_corridas_count = 0
    for caso_actual in comportamiento[1:]:
        if caso_actual != current_run:
            corridas_count += 1
            aux_corridas_count += 1
            current_run = caso_actual
            run_lengths.append(aux_corridas_count)  # Agregar la longitud de la corrida a la lista
            aux_corridas_count = 0
        else:
            aux_corridas_count += 1
            

    run_lengths.append(aux_corridas_count)  # Agregar la última corrida

    ua = (((2 * cantidad_datos) - 1) / 3)
    oa = (((16 * cantidad_datos) - 29) / 90)
    zobs = ((corridas_count - ua) / math.sqrt(oa))
    valor_critico = 1.96
    resultado_string = "El generador pasó la prueba de corridas" if ((valor_critico * -1) <= zobs and (valor_critico) >= zobs) else "El generador no pasó la prueba de corridas"

    # Contador de corridas por longitud
    run_length_counts = {}
    for length in run_lengths:
        if length in run_length_counts:
            run_length_counts[length] += 1
        else:
            run_length_counts[length] = 1

    print("Contador de Corridas por Longitud:")
    for length, count in run_length_counts.items():
        print(f"Longitud {length}: {count} veces")

    print("Z Observado:", zobs)
    print("Valor Crítico:", valor_critico)
    print(resultado_string)

#prueba_corridas(datos,periodo)  

def prueba_series(datos, m=1):
    datos_rn = []
    for dato in datos:
        datos_rn.append(dato / m)

    # Create a list of tuples
    tuple_list = [(datos_rn[i], datos_rn[i + 1]) for i in range(0, len(datos_rn), 2)]
    row_intervals = ['0.0 - 0.2', '0.2 - 0.4', '0.4 - 0.6', '0.6 - 0.8', '0.8 - 1.0']
    column_intervals = ['0.0 - 0.2', '0.2 - 0.4', '0.4 - 0.6', '0.6 - 0.8', '0.8 - 1.0']
    frequency_table = {}
    frequency_values = {}
    for row_interval in row_intervals:
        frequency_table[row_interval] = {}
        frequency_values[row_interval] = {}
        for col_interval in column_intervals:
            frequency_table[row_interval][col_interval] = 0
            frequency_values[row_interval][col_interval] = 0

    for datum in tuple_list:
        value1, value2 = datum
        value1_interval = -1
        value2_interval = -1

        if value1 >= 0.0 and value1 < 0.2:
            value1_interval = '0.0 - 0.2'
        elif value1 >= 0.2 and value1 < 0.4:
            value1_interval = '0.2 - 0.4'
        elif value1 >= 0.4 and value1 < 0.6:
            value1_interval = '0.4 - 0.6'
        elif value1 >= 0.6 and value1 < 0.8:
            value1_interval = '0.6 - 0.8'
        elif value1 >= 0.8 and value1 < 1.0:
            value1_interval = '0.8 - 1.0'

        if value2 >= 0.0 and value2 < 0.2:
            value2_interval = '0.0 - 0.2'
        elif value2 >= 0.2 and value2 < 0.4:
            value2_interval = '0.2 - 0.4'
        elif value2 >= 0.4 and value2 < 0.6:
            value2_interval = '0.4 - 0.6'
        elif value2 >= 0.6 and value2 < 0.8:
            value2_interval = '0.6 - 0.8'
        elif value2 >= 0.8 and value2 < 1.0:
            value2_interval = '0.8 - 1.0'

        frequency_table[value1_interval][value2_interval] += 1
        
    fe = len(tuple_list)/25
    #ENTONCES ES 9,488

    print("FRECUENCIA ESPERADA",fe)
    chi_cuadrado_calculado = 0
    for row_interval in row_intervals:
        for col_interval in column_intervals:
            observed_value = frequency_table[row_interval][col_interval]
            test_value = (((fe - observed_value)** 2) / fe)
            chi_cuadrado_calculado += test_value
            frequency_values[row_interval][col_interval] = test_value
    # Print the list of tuples
    #print("datos originales", datos_rn)
    #print("tuplas", tuple_list)
    resultado_string = "El generador pasó la prueba de Series" if chi_cuadrado_calculado <= 36.42 else "El generador falló la prueba de Series"
    print("tabla de frecuencias", frequency_table)
    print("tabla de valores", frequency_values)
    print('Chi cuadrado calculado:', chi_cuadrado_calculado, "valor limite:", '36.42', resultado_string)
    plot_2d_table(frequency_table, fe)
    plot_2d_table(frequency_values, 0)

#prueba_series(datos, periodo)

def prueba_poker(datos, mano_length, m=1):
    """CASOS POSIBLES
     - Los cinco dígitos son diferentes
     - Hay exactamente un par
     - Hay dos pares diferentes
     - Tres dígitos iguales
     - Tres dígitos iguales y un par
     - Cuatro dígitos iguales
     - Cinco dígitos iguales"""
    
    cantidad_datos = len(datos)
    
    datos_rn = []
    cantidad_datos = len(datos)
    for dato in datos:
        datos_rn.append(dato / m)

    manos = [datos_rn[i:i + mano_length] for i in range(0, len(datos_rn), mano_length)]

    if mano_length == 5:

        probabilidades = {
            "pachuca": 0.3024,
            "par": 0.5040,
            "dos pares": 0.1080,
            "tercia": 0.0720,
            "full": 0.0090,
            "poker": 0.0045,
            "quintilla": 0.0001
        }

        fe = {
            "pachuca": probabilidades["pachuca"] * cantidad_datos,
            "par": probabilidades["par"] * cantidad_datos,
            "dos pares": probabilidades["dos pares"] * cantidad_datos,
            "tercia": probabilidades["tercia"] * cantidad_datos,
            "full": probabilidades["full"] * cantidad_datos,
            "poker": probabilidades["poker"] * cantidad_datos,
            "quintilla": probabilidades["quintilla"] * cantidad_datos
        }

        def contar_ocurrencias(mano):
            ocurrencias = {}
            hand_str = str(mano)
            decimal_part = hand_str.split('.')[1]  # Get the decimal part
            first_5_digits = decimal_part[:5]  # Consider only the first 5 digits after the decimal point
            for digit in first_5_digits:
                if digit in ocurrencias:
                    ocurrencias[digit] += 1
                else:
                    ocurrencias[digit] = 1
            return ocurrencias


        fo = {
            "pachuca": 0,
            "par": 0,
            "dos pares": 0,
            "tercia": 0,
            "full": 0,
            "poker": 0,
            "quintilla": 0
        }

        def determinar_categoria(mano):
            ocurrencias = contar_ocurrencias(mano)
            valores = list(ocurrencias.values())
            valores.sort()

            if valores == [1, 1, 1, 1, 1]:
                fo['pachuca'] += 1
            elif valores == [1, 1, 1, 2]:
                fo['par'] += 1
            elif valores == [1, 2, 2]:
                fo['dos pares'] += 1
            elif valores == [1, 1, 3]:
                fo['tercia'] += 1
            elif valores == [2, 3]:
                fo['full'] += 1
            elif valores == [1, 4]:
                fo['poker'] += 1
            elif valores == [5]:
                fo['quintilla'] += 1
            else:
                return "Nada"

        for mano in manos:
            for jugada in mano:
                determinar_categoria(jugada)

        resultados = {
            "pachuca": (((fe['pachuca'] - fo['pachuca'])** 2) / fe['pachuca']),
            "par": (((fe['par'] - fo['par'])** 2) / fe['par']),
            "dos pares": (((fe['dos pares'] - fo['dos pares'])** 2) / fe['dos pares']),
            "tercia": (((fe['tercia'] - fo['tercia'])** 2) / fe['tercia']),
            "full": (((fe['full'] - fo['full'])** 2) / fe['full']),
            "poker": (((fe['poker'] - fo['poker'])** 2) / fe['poker']),
            "quintilla": (((fe['quintilla'] - fo['quintilla'])** 2) / fe['quintilla'])
        }
        valor_critico = 12.592
        chi_cuadrado_calculado = 0
        for resultado in resultados:
            chi_cuadrado_calculado += resultados[resultado]
        resultado_string = "El generador pasó la prueba de Poker de 5 cartas" if chi_cuadrado_calculado <= valor_critico else "El generador falló la prueba de Poker de 5 cartas"
        #print("FRECUENCIAS:", fo)
        print("Chi Cuadrado", chi_cuadrado_calculado, resultado_string)

       # Calculate and print the table
        table_data = {
            "Categoria": ["Pachuca", "Par", "Dos Pares", "Tercia", "Full", "Poker", "Quintilla"],
            "Probabilidad": [probabilidades["pachuca"], probabilidades["par"], probabilidades["dos pares"],
                            probabilidades["tercia"], probabilidades["full"], probabilidades["poker"], probabilidades["quintilla"]],
            "Frecuencia Esperada (FE)": [fe["pachuca"], fe["par"], fe["dos pares"], fe["tercia"], fe["full"], fe["poker"], fe["quintilla"]],
            "Frecuencia Observada (FO)": [fo["pachuca"], fo["par"], fo["dos pares"], fo["tercia"], fo["full"], fo["poker"], fo["quintilla"]],
            "Chi Cuadrado": [resultados["pachuca"], resultados["par"], resultados["dos pares"],
                            resultados["tercia"], resultados["full"], resultados["poker"], resultados["quintilla"]],
        }

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.axis('tight')
        ax.axis('off')
        
        ax.table(cellText=[list(map(str, row)) for row in zip(*list(table_data.values()))],
                colLabels=list(table_data.keys()),  # Convert dict_keys to a list
                cellLoc='center',
                loc='center',
                colColours=["lightgray"] * len(table_data.keys()))
        
        plt.title('Tabla de Frecuencias para Prueba de Poker')
        plt.show()

    elif mano_length == 3:
        probabilidades = {
        "pachuca": 0.72,
        "par": 0.27,
        "tercia": 0.01,
        }

        fe = {
            "pachuca": probabilidades["pachuca"] * cantidad_datos,
            "par": probabilidades["par"] * cantidad_datos,
            "tercia": probabilidades["tercia"] * cantidad_datos,
        }

        def contar_ocurrencias(mano):
            ocurrencias = {}
            hand_str = str(mano)
            decimal_part = hand_str.split('.')[1]  # Get the decimal part
            first_3_digits = decimal_part[:3]  # Consider only the first 3 digits after the decimal point
            for digit in first_3_digits:
                if digit in ocurrencias:
                    ocurrencias[digit] += 1
                else:
                    ocurrencias[digit] = 1
            return ocurrencias

        fo = {
            "pachuca": 0,
            "par": 0,
            "tercia": 0,
        }

        def determinar_categoria(mano):
            ocurrencias = contar_ocurrencias(mano)
            valores = list(ocurrencias.values())
            valores.sort()

            if valores == [1, 1, 1]:
                fo['pachuca'] += 1
            elif valores == [1, 2]:
                fo['par'] += 1
            elif valores == [3]:
                fo['tercia'] += 1
            else:
                return "Nada"

        manos = [datos_rn[i:i + mano_length] for i in range(0, len(datos_rn), mano_length)]

        for mano in manos:
            for jugada in mano:
                determinar_categoria(jugada)

        resultados = {
            "pachuca": (((fe['pachuca'] - fo['pachuca'])**2) / fe['pachuca']),
            "par": (((fe['par'] - fo['par'])**2) / fe['par']),
            "tercia": (((fe['tercia'] - fo['tercia'])**2) / fe['tercia']),
        }
        valor_critico = 5.991  # Valor crítico para alfa = 0.05 y 2 grados de libertad
        chi_cuadrado_calculado = 0
        for resultado in resultados:
            chi_cuadrado_calculado += resultados[resultado]
        resultado_string = "El generador pasó la prueba de Poker de 3 cartas" if chi_cuadrado_calculado <= valor_critico else "El generador falló la prueba de Poker de 3 cartas"
        #print("FRECUENCIAS:", fo)
        print("Chi Cuadrado", chi_cuadrado_calculado, resultado_string)
        # Calculate and print the table
        table_data = {
            "Categoria": ["Pachuca", "Par", "Tercia"],
            "Probabilidad": [probabilidades["pachuca"], probabilidades["par"], probabilidades["tercia"]],
            "Frecuencia Esperada (FE)": [fe["pachuca"], fe["par"], fe["tercia"]],
            "Frecuencia Observada (FO)": [fo["pachuca"], fo["par"], fo["tercia"]],
            "Chi Cuadrado": [resultados["pachuca"], resultados["par"], resultados["tercia"]],
        }

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.axis('tight')
        ax.axis('off')
        
        ax.table(cellText=[list(map(str, row)) for row in zip(*list(table_data.values()))],
                colLabels=list(table_data.keys()),  # Convert dict_keys to a list
                cellLoc='center',
                loc='center',
                colColours=["lightgray"] * len(table_data.keys()))
        
        plt.title('Tabla de Frecuencias para Prueba de Poker')
        plt.show()

#prueba_poker(datos, 5, periodo)
#prueba_poker(datos_poker, 3, 1)