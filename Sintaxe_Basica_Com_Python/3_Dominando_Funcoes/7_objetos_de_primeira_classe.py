def somar(a, b):
    return a + b

def subtracao(a, b):
    return a - b 

def exibir_resultado(a, b, funcao):
    resultado = funcao(a ,b)
    print(f"Oresultado da operação é: {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtracao)



operacao = subtracao
print(operacao(10, 5))

operacao = somar
print(operacao(10, 5))