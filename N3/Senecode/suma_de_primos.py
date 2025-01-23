def suma_de_primos(n: int) -> int:
    es_normal = False
    primos = 0
    for indice in range(2, n):
        for numeros_hasta in range(2, indice):
            if(indice%numeros_hasta == 0):
                es_normal = True
        if(es_normal):
            es_normal = False
        elif(not es_normal):
            primos += indice
    
    return primos

print(suma_de_primos(37))