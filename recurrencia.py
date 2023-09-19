def encontrar_periodo(X0, a, c, m):
    valor_actual = X0
    iteraciones = 0
    historico = []
    while True:
        valor_actual = (a * valor_actual ) % m
        if valor_actual in historico:
            return iteraciones
        iteraciones += 1
        if iteraciones <= 5:
            historico.append(valor_actual)

        if valor_actual == X0:
            return iteraciones

X0 = 5
a = 12
c = 5
m = 21

#iteraciones = encontrar_periodo(X0, a, c, m)

#print("Iteraciones totales antes de que el valor actual sea igual a la semilla:", iteraciones)

def encontrar_periodo_factorizado(X0, a, m):
    q = m // a
    r = m % a
    valor_actual = X0
    iteraciones = 0
    historico = []
    while True:
        valor_actual = (a * (valor_actual % q) - r * (valor_actual // q)) % m
        if valor_actual in historico:
            return iteraciones
        iteraciones += 1
        if iteraciones <= 5:
            historico.append(valor_actual)
        print(valor_actual)
        if valor_actual == X0:
            return iteraciones

X0 = 5
a = 12
m = 21

iteraciones = encontrar_periodo_factorizado(X0, a, m)

print("Iteraciones totales antes de que el valor actual sea igual a la semilla:", iteraciones)
