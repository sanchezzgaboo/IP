def verificar_parentesis(formula: str)->bool:
    """ Verificar paréntesis
    Parámetros:
      formula (str): Formula matemática que Valeria quiere verificar
    Retorno:
      bool: Determinar si los paréntesis están balanceados
    """
    abiertos = 0
    cerrados = 0
    balanceado = False
    for letra in formula:
        if(letra == "("):
            abiertos += 1
        if(letra == ")" and abiertos >= 1):
            cerrados += 1
    if(abiertos == cerrados):
        balanceado = True
    return balanceado

print(verificar_parentesis("(()(())"))
