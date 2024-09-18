def exibir_mensagem():
    print("Hello World!")

def exibir_mensagem_2(nome):
    print(f"Seja Bem Vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja Bem Vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Cleiton")
exibir_mensagem_3()
exibir_mensagem_3(nome="Bill")