#Script feito por Valber Barbosa


from netmiko import ConnectHandler
import os




#funcao responsavel por executar o comando admin state  down na onu. OPACAO == 1
def down_onu(posicao):#OPACAO == 1




    SSH.send_command(f'configure equipment ont interface {posicao} admin-state down')
    print("comando admin-state down aplicado com sucesso")


#verificar qual esta pedindo autorização e colocar na variavel para configurar
def autorizacao(posicao=str, login=str, password=str, ip_olt=str):#OPACAO == 2
   
    device = {
        'device_type': 'alcatel_aos',
        'host' : ip_olt,
        'username' : login,
        'password' : password,
       
    }


    SSH = ConnectHandler(**device)






    #vai jogar o comando na olt e oque for respodido vai jogar na variavel output
    output = SSH.send_command('show pon unprovision-onu')


    #vai transformar as informaçoes pegar em uma lista
    lista_serial = output.split()
    quantidade_intens = len(lista_serial)
   
    primeiro = 0
    segundo = 1


    for i in range(quantidade_intens):
        segundo = 0 + i
        primeiro = -1 + segundo
       
        if "ALCL" in lista_serial[segundo] and lista_serial[primeiro] in posicao:
            onu = lista_serial[segundo]
            print(f"POSICAO = {lista_serial[primeiro]}")
            onu = list(onu)
            onu.insert(4,":")
            onu = ''.join(onu)
            return onu


#funcao responsavel por executar o comando admin state  up na onu.
def up_onu(posicao, onu):#OPACAO == 3
    SSH.send_command(f'configure equipment ont interface {posicao} admin-state down')
    SSH.send_command(f'configure equipment ont interface {posicao} sernum {onu} admin-state up')
    print(f"ONU = {onu} na POSICAO = {posicao} provisionada com sucesso")


#funcao responsavel por dar up na ultima onu que foi provissionada.
def ultima_onu(posicao):#OPACAO == 4
    SSH.send_command(f'configure equipment ont interface {posicao} admin-state up')
    print("comando admin-state up aplicado com sucesso")


ip_olt = input("Informe o ip da OLT: ")
login = input("Informe o login: ")
password = input("Informe a senha: ")




#
device = {
      'device_type': 'alcatel_sros',
      'host' : ip_olt,
      'username' : login,
      'password' : password,
     
  }
#alcatel_aos
#alcatel_sros




SSH = ConnectHandler(**device)




posicao_onu = input("informe a posicao da onu homologada:")


i = 1  
while i != 0:


    opcao = input(" 1-Para dar admin-state down \n 2-Para verificar se tem pedindo autorização \n 3-Para provisionar \n 4-Dar up na ultima ONU \n 5-Para sair do programa: ")
    os.system('cls')
    match opcao:


        #======================================#
        case '1':
            down_onu(posicao_onu)


        #======================================#
        case '2':
           
            onu_nokia = autorizacao(posicao_onu, login, password, ip_olt)
            if onu_nokia ==None:
                print("nehuma pedindo autorização")
            else:
                print(f"ONU = {onu_nokia} pedindo autorização")


        #======================================#
        case '3':
            up_onu(posicao_onu, onu_nokia)


        #======================================#    
        case '4':
            ultima_onu(posicao_onu)


        #======================================#  
        case '5':
            i = 0



