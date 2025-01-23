matriz = [[1,0,1,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,1,0,1]]


for fila in range(len(matriz)//2):
    valor_arriba = matriz[fila]
    valor_abajo = matriz[len(matriz) - 1 - fila]
    matriz[fila] = valor_abajo
    matriz[len(matriz) - 1 - fila] = valor_arriba    
    

matriz.extend(matriz)
        
for item in matriz:
    print(item)
        