import re

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}'
    if re.match(padrao, email):
        return True
    return False

def validar_telefone(telefone):
    # O padrão (11) 99999-9999 deve vir por uma mascara do front-end
    padrao = r'^\(\d{2}\) \d{4,5}-\d{4}$'
    if re.match(padrao, telefone):
        return True
    return False

def validar_cpf(cpf):
    padrao = r'^\d{3}.\d{3}.\d{3}-\d{2}$'             #362.402.648-81
    if re.match(padrao, cpf):
        return True
    return False

def validar_cep(cep):   # 04143-030
    padrao = r'^\d{5}-\d{3}$'
    if re.match(padrao, cep):
        return True
    return False


def menu():
    while True:
        print('=== VALIDADOR DE DADOS ===')
        print('1 - Validar Email')
        print('2 - Validar Telefone')
        print('3 - Validar CPF')
        print('4 - Validar CEP')
        print('5 - Sair')

        opcao = input('Selecione uma opção: ')

        if opcao == '1':
            email = input('Digite o email a ser validado: ')
            if validar_email(email):
                print('Email válido.')
            else:
                print('Email inválido.')
        
        elif opcao == '2':
            telefone = input('Digite o Telefone a ser validado no formato (xx) xxxxx-xxxx : ')
            if validar_telefone(telefone):
                print('Telefone válido.')
            else:
                print('Telefone inválido.')
        
        elif opcao == '3':
            cpf = input('Digite o CPF a ser validado no formato xxx.xxx.xxx-xx : ')
            if validar_cpf(cpf):
                print('CPF válido.')
            else:
                print('CPF inválido.')

        elif opcao == '4':
            cep = input('Digite o CEP a ser validado no formato xxxxx-xxx : ')
            if validar_cep(cep):
                print('CEP válido.')
            else:
                print('CEP inválido.')

        elif opcao == '5':
            print('Encerrando Validador')
            break
        
        else:
            print('Opção inválida, selecione uma das opções do menu.')



if __name__ == '__main__':
    menu()
        