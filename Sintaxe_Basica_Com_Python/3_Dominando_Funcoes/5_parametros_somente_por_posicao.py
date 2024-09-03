def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): #Argumento antes da barra somente por posição, não pode passar parametros por nomes 
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="fiat", motor="1.0", combustivel="Gasolina") #Válido porque é obrigado a passar o parameto sem o nome antes da barra, após a barra é opcional   
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="fiat", motor="1.0", combustivel="Gasolina") #Inválido porque não se pode passar os nomes dos parametros antes da barra 