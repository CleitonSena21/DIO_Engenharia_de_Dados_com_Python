# Desafio de Otimização do Sistema Bancário

Este projeto tem como objetivo aprimorar um sistema bancário desenvolvido anteriormente, refatorando e modularizando o código em Python para torná-lo mais eficiente e fácil de manter. O sistema deve ser capaz de gerenciar operações bancárias básicas, bem como cadastrar usuários e contas bancárias.

## Descrição do Desafio

O desafio consiste em separar as funções existentes de saque, depósito e extrato em funções específicas e criar duas novas funções: uma para cadastrar usuários e outra para cadastrar contas bancárias. O sistema deve ser modularizado para facilitar a manutenção e o entendimento do código.

### Requisitos

1. **Funções de Operações Bancárias**:
   - **Saque**: Recebe argumentos apenas por nome (keyword only). Atualiza o saldo e o extrato da conta, verificando saldo, limite e número de saques.
   - **Depósito**: Recebe argumentos apenas por posição (positional only). Atualiza o saldo e o extrato da conta.
   - **Extrato**: Recebe argumentos por posição e nome (positional only e keyword only). Exibe o extrato da conta.

2. **Novas Funções**:
   - **Criar Usuário**: Armazena usuários em uma lista com informações como nome, data de nascimento, CPF e endereço. O CPF deve ser único.
   - **Criar Conta Corrente**: Armazena contas em uma lista com informações como agência, número da conta e CPF do usuário. O número da conta é sequencial.

### Estrutura do Código

1. **Funções para Operações Bancárias**:
   - `saque(conta, *, valor, limite, numero_saques, limite_saques)`: Realiza um saque da conta, atualizando o saldo e o extrato.
   - `deposito(conta, valor)`: Realiza um depósito na conta, atualizando o saldo e o extrato.
   - `exibir_extrato(conta)`: Exibe o extrato da conta.

2. **Funções para Gerenciar Usuários e Contas**:
   - `criar_usuario(nome, data_nascimento, cpf, endereco)`: Cria um novo usuário, verificando se o CPF já está cadastrado.
   - `criar_conta_corrente(cpf)`: Cria uma nova conta corrente para um usuário existente.
   - `listar_usuarios()`: Lista todos os usuários cadastrados.
   - `listar_contas()`: Lista todas as contas correntes cadastradas.
   - `selecionar_conta()`: Permite ao usuário selecionar uma conta a partir da lista de contas.

3. **Função Principal**:
   - `menu_bancario()`: Exibe o menu do sistema e gerencia a interação do usuário com as operações bancárias.
  
  ### Considerações

- O sistema garante que o CPF dos usuários seja único.
- O número da conta é gerado sequencialmente e inicia em 1.
- Limite de saques diário e valor máximo de saque são configuráveis.