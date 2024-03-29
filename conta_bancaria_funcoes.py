# parametros precisam ser passados diretos.Ex:deposito(100,10,"")

def deposito(saldo,valor,extrato,/):
    saldo=valor
    extrato=(f"\nDepósito no valor de R$ {valor:.2f}")
    return saldo,extrato

# exemplo saque(*,saldo=saldo,valor=valor):

def saque(*,saldo,valor,extrato,num_saques,limite_saque):
    if num_saques>3:
        print("Você já atingiu o número de saque para o dia")
    elif valor>saldo:
        print("Saldo insuficiente!")
    elif not limite_saque:
        print(f"R$ {valor:.2f} é superior ao limite disponível para saque")
    else:
        saldo-=valor
        extrato=(f"\nSaque no valor de R$ {valor:.2f}")
        return saldo,extrato
    

def extrato(saldo,/,*,extrato):    
    print(extrato)
    print(f"Saldo é de R${saldo:.2f}")


def criaUsuario(listaUsuario):
    cpf=input("Digite o CPF (SOMENTE NÚMEROS): ")
    usuario=buscaUsuario(cpf,listaUsuario)

    if usuario:
        print("Usuário já cadastrado!")
        return

    nome=input("Informe seu nome: ")
    data_nascimento=input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco=input("Informe o endereço (logradouro,nro-bairro-cidade/sigla estado): ")
    listaUsuario.append({"cpf":cpf,"nome":nome,"data_nascimento":data_nascimento,"endereco":endereco})

    print("Usuario cadastrado com sucesso")

def buscaUsuario(cpf,listaUsuario):
    usuario=[user for user in listaUsuario if user["cpf"]==cpf]
    return usuario[0] if usuario else None

def contaCorrente(agencia,numero,usuarios):
    cpf=input("Informe o CPF: ")
    usuario=buscaUsuario(cpf,usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia":agencia,"num_conta":numero,"usuario":usuario}
    else:
        print("Não existe usuário cadastrado")

def listaClientes(lista):
    for c in lista:
        print(f"CPF: {c["cpf"]}")
        print(f"Nome: {c["nome"]}")
        print(f"Endereco: {c["endereco"]}")

def listaContas(lista):
   for conta in lista:
       print(f"Agência: {conta['agencia']}")
       print(f"Conta: {conta["num_conta"]}")
       print(f"Titutar: {conta["usuario"]["nome"]}")


def menu():
    menu = "************************************\n"
    menu += "*[1]-Extrato                       *\n"
    menu += "*[2]-Depósito                      *\n"
    menu += "*[3]-Saque                         *\n"
    menu += "*[4]-Novo cliente                  *\n"
    menu += "*[5]-Nova conta                    *\n"
    menu += "*[6]-Listagem cliente              *\n"
    menu += "*[7]-Listagem conta                *\n"
    menu += "*[8]-Sair do programa              *\n"
    menu += "************************************\n"

    return int(input(menu))



def main():
    saldo=0.00
    NUM_SAQUE=0
    LIMITE_SAQUE=True   
    AGENCIA="0001" 
    historico=""     
    opcao=0   
    usuarios=[]
    contas=[]
    while opcao!=8:
        try:
            opcao=menu()       
        except ValueError:
            print("Escolha inválida!")    
        
        if opcao==1:
            extrato(saldo,extrato=historico)    
         #deposito   
        elif opcao==2:
            valor=0.00
            try:
                valor=float(input("Informe valor para DEPÓSITO\n"))
            except ValueError:
                print("Valor INVÁLIDO!")    

            retorno=deposito(saldo,valor,historico)
            saldo+=float(retorno[0])
            historico+=retorno[1]
            print("Depósito efetuado com sucesso!!")
        #saque
        elif opcao==3:
            valor=0.00
            try:
                valor=float(input("Informe valor para SAQUE\n"))
                if valor>500:
                    LIMITE_SAQUE=False
            except ValueError:
                print("Valor INVÁLIDO!")    
            #saque(*,saldo,valor,extrato,num_saques,limite_saque):
            retorno=saque(saldo=saldo,valor=valor,extrato=historico,num_saques=NUM_SAQUE,limite_saque=LIMITE_SAQUE)
            if retorno:         
                saldo=float(retorno[0])
                historico+=retorno[1]
                NUM_SAQUE+=1
                print("SAQUE efetuado com sucesso!!")

        # criando a lista de usuários
        if opcao==4:
           # Apesar da função não ter um retorno explicito, ela consegue modificar a lista de usuarios.
           # Isso se deve ao fato de estarmos tratando de objetos
           criaUsuario(usuarios)
        
        if opcao==5:
            print('Criando contas')
            num_conta=len(usuarios)+1
            conta=contaCorrente(AGENCIA,num_conta,usuarios)
            if conta:
                contas.append(conta)


        if opcao==6:
            listaClientes(usuarios)

        if opcao==7:
            listaContas(contas)            
            
           

        elif opcao==8:
            print("PROGRAMA finalizado!")        
            

main()    