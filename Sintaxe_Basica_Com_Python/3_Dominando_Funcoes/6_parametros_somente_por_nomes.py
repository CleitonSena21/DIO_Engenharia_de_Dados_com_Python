def criar_carro(*, modelo, ano, placa, marca, motor, combustivel): #Com o * todos os parametros devem ser passador por nome
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="fiat", motor="1.0", combustivel="Gasolina")   
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="fiat", motor="1.0", combustivel="Gasolina") 


def criar_carro(modelo, ano, placa, / marca, *, motor, combustivel): #Com o * no meio deixa o marca com o parametro por nome ou posição opcional
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="fiat", motor="1.0", combustivel="Gasolina")  