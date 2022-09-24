from time import sleep

def criptografar():
    #funcao de criptografar

    cripto = input(str("Entre com o texto para criptografa-lo:  "))
    resultado = ''

    for char in cripto:
        unicode = ord(char)
        letra = chr(unicode + 1)
        
        if unicode == 122:
            letra = chr(61)
            
        resultado = resultado + letra
        
    print(f"Entrada de senha: ", cripto)
    print("--------------------------------")
    print("Criptografando ...")
    print("--------------------------------")
    sleep(3)
    print(f"Saída de senha: ", resultado)
    print("--------------------------------")


def descriptografar():
    #funcao de descriptografar

    descripto = str(input("Entre com o texto para descriptografar:  "))
    resultado_inver = ''

    for char in descripto:
        unicode = ord(char)
        letra = chr(unicode - 1)
        
        if unicode == 61:
            letra = chr(122)
        
        resultado_inver = resultado_inver + letra

    print(f"Senha criptografada: ", descripto)
    print("--------------------------------")
    print("descriptografando ...")
    print("--------------------------------")
    sleep(3)
    print(f"Saída de senha: ", resultado_inver)
    print("--------------------------------") 

print('------------------------------------------------')
print("MENU")
print('------------------------------------------------')
print("[1] Para criptografar\n[2] Para descriptografar")
print('------------------------------------------------')
choice = int(input("Digite o número da sua opção:  "))
print('------------------------------------------------')

if choice == 1:
    criptografar()
elif choice == 2:
    descriptografar()
