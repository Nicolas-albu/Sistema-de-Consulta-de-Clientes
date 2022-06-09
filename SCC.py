
dict_cpf_valor_de_devedores: dict[int, int] = {
    60827511914 : 20.3,
    55942546096 : 40.6,
    52784438805 : 70.99,
    89845841856 : 65.47
}

dict_compradores: dict = {}

def pagarDebito(CPF_do_devedor):
    if CPF_do_devedor in dict_cpf_valor_de_devedores:
        valor_de_debito = dict_cpf_valor_de_devedores[CPF_do_devedor]
    else:
        print(f"Nenhuma dívida a ser paga ao {CPF_do_devedor}.")
        menu()

    print(f"Débito de R$ {valor_de_debito}, ao CPF {CPF_do_devedor}")

    while True:
        try:
            conta_bancaria = int(input("Conta bancária: "))
            valor_pago = float(input("Valor que será pago R$ "))
        except ValueError:
            print("Insira apenas valores númericos inteiros.")
            continue
        except KeyboardInterrupt:
            print("\nSCC encerrado por interrupção.\n")
            exit()
        except Exception:
            print("Infelizmente ocorreu um erro no SCC. Tente Novamente.\n")
            continue

        if valor_de_debito <= valor_pago:
            if CPF_do_devedor in dict_cpf_valor_de_devedores:
                del dict_cpf_valor_de_devedores[CPF_do_devedor]
            
            print(f"A dívida de {CPF_do_devedor} foi quitada.\n")
            menu()
        elif valor_de_debito > valor_pago:
            print("Pagamento não foi aceito, devido o pagamento ser menor que o valor da dívida.\n")
            continue

def realizarVenda():
    while True:
        print("Realizamento de Vendas:\nPor favor, insira o seu CPF.\nObservação: sem caracteres de pontuação, apenas inteiro.\n")
        try:
            cpf_do_cliente = int(input("CPF: "))
        except ValueError:
            print("Insira apenas valores númericos inteiros sem pontuação.\n")
            continue
        except KeyboardInterrupt:
            print("\nSCC encerrado por interrupção.\n")
            exit()
        except Exception:
            print("Infelizmente ocorreu um erro no SCC. Tente Novamente.\n")
            continue
        
        if cpf_do_cliente in dict_cpf_valor_de_devedores:
            print("CPF encontrado em lista de devedor na SCC. Você deverá pagar o débito para continuar.\n")
            pagarDebito(CPF_do_devedor=cpf_do_cliente)
        else:
            dict_compradores[cpf_do_cliente] = valor_do_ingresso
            print(f"Ingresso de R$ {valor_do_ingresso} adicionado ao comprador {cpf_do_cliente}.")
            menu()

def listarDevedores():
    print("CPF dos Devedores:")
    for key, value in dict_cpf_valor_de_devedores:
        print(f"CPF: {key}, Dívida (R$): {value}")
    menu()

def listarCompradores():
    if {} == dict_compradores:
        print("Nenhum CPF de compradores.")
    else:
        print("CPF dos Compradores:")
        for key, value in dict_compradores:
            print(f"CPF: {key}")
    menu()

def valorArrecadado(): 
    global arrecadamento
    arrecadamento = sum(dict_compradores.values())
    print(F"Valor de arrecadamento total R$ {arrecadamento}")
    menu()

def menu(): 
    print("\nMenu do Sistema de Consutlas de Clientes (SCC):")
    print("""1. Realizar venda\n2. Listar devedores\n3. Listar compradores\n4. Pagar débito (devedores)\n5. Valor arrecadado pelo evento\n""")
    
    while True:
        try:
            opcoes_do_menu = int(input("Selecione o número da opção: "))
        except ValueError:
            print("Insira apenas valores númericos de 1 à 5.\n")
            continue
        except KeyboardInterrupt:
            print("\nSCC encerrado por interrupção.\n")
            exit()
        except Exception:
            print("Infelizmente ocorreu um erro no SCC. Tente Novamente.")
            continue

        if opcoes_do_menu not in [1, 2, 3, 4, 5]:
            print("Insira apenas números de opções de 1 à 5.\n")
            continue

        elif opcoes_do_menu == 1:
            realizarVenda()
        elif opcoes_do_menu == 2:
            listarDevedores()
        elif opcoes_do_menu == 3:
            listarCompradores()
        if opcoes_do_menu == 4:
            while True:
                try:
                    cpf_do_cliente = int(input("CPF: "))
                except ValueError:
                    print("Insira apenas valores númericos inteiros.\n")
                    continue
                except KeyboardInterrupt:
                    print("\nSCC encerrado por interrupção.\n")
                    exit()
                except Exception:
                    print("Infelizmente ocorreu um erro no SCC. Tente Novamente.")
                    continue
                break
            
            pagarDebito(CPF_do_devedor=cpf_do_cliente)
        elif opcoes_do_menu == 5:
            valorArrecadado()

def principal():
    print("Sistema de Consulta de Clientes (SCC).\nPara sair das opções, faça CTRL + C.\n")
    global valor_do_ingresso
    while True:
        try:
            valor_do_ingresso = float(input("Valor do ingresso R$ "))
        except ValueError:
            print("Insira apenas valores númericos.\n")
            continue
        except KeyboardInterrupt:
            print("\nSCC encerrado por interrupção.\n")
            exit()
        except Exception:
            print("Infelizmente ocorreu um erro no SCC. Tente Novamente.\n")
            continue

        if valor_do_ingresso >= 10:
            menu()
        else:
            print("Valor de ingresso abaixo de R$ 10.00 não são aceitos.\n")
            continue

if __name__ == "__main__":
    principal()