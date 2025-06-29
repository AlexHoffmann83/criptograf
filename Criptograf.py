

def string_to_ascii(chave):
    ascii_values = []              #inicializa a lista
    for character in chave:        #lê cada caracter da string recebida e faz um append na lista transformando para ascii
        ascii_values.append(ord(character))

    return(ascii_values)           #retorna uma lista com cada caracter convertido em ascii ocupando uma posição da lista.



def ascii_to_string(chave): 
    letra = []                     #inicializa a lista
    string = ""                    #inicializa a string
    
    for i in chave:                #para cada posição da lista, transforma o código ascii em caracter atribuindo à "palavra"
        letra.append(chr(i))
        
    for i in letra:                #para cada letra ou símbolo em "letra", vai montando a string na variável "string"
        string += str(i)
        
    return(string)                 #retorna uma string.



#é necessário que a chave tenha no mínimo o mesmo tamanho de caracteres da senha.
#faz isso duplicando a chave até que tenha no mínimo o mesmo tamanho da senha. 
#Não colocar qualquer string ou função para completar a chave, pois alguém que tenha acesso a esse código conseguirá deduzir
#a parte da senha equivalente a esta função pela chave gerada. Se manter a chave em segredo, a senha sempre será segredo
#também.

# SÓ PASSAR LISTAS PARA ESSA FUNÇÃO. NÃO TRATA STRINGS.


def ajustaChaveMenor(senha, chave):
    
    diferenca = len(senha)-len(chave)

    novaChave = chave

    while diferenca > 0:
        novaChave = novaChave+chave #testar novaChave.extend(novaChave), que deve dar o mesmo resultado
        diferenca = len(senha)-len(novaChave)


    return(novaChave)



def ajustaChaveMaior(senha, chave):
    
    diferenca = len(senha)
    novaChave = []
    cont = 0

    while cont < diferenca:
        novaChave.append(chave[cont])
        cont += 1

    return(novaChave)



def criptografa():

#cria uma nova senha criptografada somando os elementos em cada índice da senha original com os elementos de cada índice da chave.
#cria uma posição de controle logo após a soma conforme abaixo:
#se senha original[i] > chave[i]: acrescenta um número aleatório entre 0 e 9 após a posição i da senha da senha criptografada
#se senha orignal[i] < chave[i]: acrescenta uma letra mínuscula da range de "a" a "z" após a posiçao i da senha criptografada

#Depois, na função "descriptografa", executará o seguinte:
#leu número na posição de controle: senhacriptograda + chave - 32
#leu letra na posição de controle: senhacriptograda - chave + 32
#As posições de controle serão as ímpares, visto que a posição zero é senha, a 1 é controle, a 2 é senha, a 3 é controle...

#nota: A tabela ascii começa no 32 como espaço. O número 33 já é caracter. Com a fórmula acima nunca acontecerá de a senha
#ser um espaço ou menor que 32 (inválido).
    
    senha=[]
    chave=[]
    novaSenha=[]

    #recebe valores digitados pelo usuário no tkinter
    #verifiquei que o nome da variável local tem que ser diferente da variável global para funcionar!
    stringNome  = (entry_nome.get())
    stringSenha = (entry_senha.get()) 
    stringChave = (entry_chave.get())
    
    #testa se campo senha ou campo chave ficaram em branco. Nesse caso, não executa a função até que prencha ambos:
    if (len(stringSenha) <1) or (len(stringChave) < 1):
        result.set('"Senha e Chave não podem estar em branco"')
        
    else:
        #transforma as strings de senha e chave em listas com o valor correspondente ascii
        senha=string_to_ascii(stringSenha)
        chave=string_to_ascii(stringChave)
    
    
        tamanhoSenha = len(senha)
        tamanhoChave = len(chave)
        cont = 0
    
    
        #Se tamanho da lista senha > tamanho da lista chave, duplica chave até que fique no mínimo igual a senha.
        if (tamanhoSenha > tamanhoChave):
            chave = ajustaChaveMenor(senha, chave)
    
        #Se tamanho da chave > tamanho da senha, trunca a chave até o limite do número de posições da senha.
        if (tamanhoSenha < tamanhoChave):
            chave = ajustaChaveMaior(senha, chave)
        
        while cont < tamanhoSenha:
        
            #adiciona o embaralhamento de senha + chave dentro da range de 32 (espaço) até qualquer caracter digitável (até 127)
            novaSenha.append(abs(senha[cont]-chave[cont])+32) 

            #se o número absoluto da senha[cont] for maior ou igual que o número absoluto da chave[cont]
            #acrescenta um número aleatório de 0 a 9 na posição seguinte de novaSenha
            if (senha[cont] > chave[cont]) or (senha[cont] == chave[cont]) : 
                novaSenha.append(random.randrange(48,58)) #a range de 48 a 57(inclusive) é equivalente aos nrs de 0 a 9.
            
            #se não, acrescenta um número equivalmente a range do alfabeto de "a" a "Z" minúsculo
            else:
                novaSenha.append(random.randrange(97,123))          
            
            cont += 1
        
        
        
        
        encriptString = ""
        encriptString = ascii_to_string(novaSenha)                        #transforma a lista ascii para uma string de caracteres
        


        #As próximas duas linhas fazem a quebra do texto na posição 50 usando a biblioteca textwrap
        #wrapper = textwrap.TextWrapper(width=10)
        #encriptString = wrapper.fill(text=encriptString)
        
        encriptString = ('"'+encriptString+'"')                           #coloca valor recebido entre aspas duplas   
        
        
        #imprime a string para comprar com valor da tela. Quando terminar, tirar esse comando.
        print(encriptString)

        #retorna uma string com a seguinte sequencia: 
        #nr asccii da senha crip, variável de controle, nr asccii da senha crip, variável de controle, nr asccii da senha crip, variável de controle...
        #a variável de controle fica sempre nas posições ímpares (1, 3, 5...) e seu equivalente asccii é:
        #   - Um número de 0-9 se a senha for maior que chave na posição imediatamente anterior
        #   - Uma letra de "a" a "z" (range 97-123 em ascii)se a senha for menor que a chave na posição imediatamente anterior.
    
    
        limpaTela()

        result.set(str(encriptString)) #Passa para o Label "resultado"


        #Abaixo, função para criar e atualizar o arquivo de senhas:
        import os

        # Salva no arquivo somente se o nome da senha foi preenchido
        if stringNome.strip():
            arquivo_senhas = "Senhas.txt"

            if not os.path.exists(arquivo_senhas):
                with open(arquivo_senhas, "w", encoding="utf-8") as f:
                    f.write(
                        f"{'Nome da senha'.ljust(40)}Senha Criptografada\n-------------------------------         -------------------------------\n")

            with open(arquivo_senhas, "a", encoding="utf-8") as f:
                f.write(f"{stringNome.ljust(40)}{encriptString}\n")


def descriptografa():
    
    
    #recebe valores digitados pelo usuário no tkinter - o nome da variável local tem que ser diferente da variável global para funcionar!
    stringSenha = (entry_senha.get()) 
    stringChave = (entry_chave.get())
    parImpar = (int(len(stringSenha)))
    
    #testa se campo senha ou campo chave ficaram em branco. Nesse caso, não executa a função até que prencha ambos:
    if (len(stringSenha) <1) or (len(stringChave) < 1):
        result.set('"Senha e Chave não podem estar em branco"')

    #testa se a senha tem número ímpar de caracteres e pede senha válida. Senha criptografada sempre vai ter número par,
    #pois é sempre o dobro do tamanho da senha orignal. 
    elif (parImpar%2 == 1):
        result.set('"Digite uma senha válida para descriptografar"')
        
    else:
    
        #transforma as strings de senha e chave em listas com o valor correspondente ascii
        senha=string_to_ascii(stringSenha)
        chave=string_to_ascii(stringChave)
    
        #inicializando variáveis
        descript = []
        chaveNova = []
        senhaTemp = []
    
        tamanhoSenha=len(senha)
        tamanhoChave=len(chave)
        tamanhoSenhaOriginal=(int(tamanhoSenha/2))

        cont = 0

        #Se tamanho da chave < tamanho da senha/2 (senha original), duplica a chave até o tamanho da senha original
        if (tamanhoChave < tamanhoSenhaOriginal):
            while (cont < tamanhoSenhaOriginal): # Vai criar uma senha temporária, só para ficar do tamanho da original e chamar a função.
                senhaTemp.append(senha[cont])
                cont += 1
            
            chave = ajustaChaveMenor(senha, chave) #vai duplicar o tamanho da chave, mas pode passar do tamanho da senha.
            tamanhoChave = len(chave) #atualiza o tamanho da chave, caso a mesma tenha sido alterada no if
    
        cont = 0
        senhaTemp = []
    
        #Se tamanho da chave > tamanho da senha/2 (senha original), trunca a chave no limite do número de posições senha original.
        if (tamanhoChave > tamanhoSenhaOriginal): 
            while (cont < tamanhoSenhaOriginal): # Vai criar uma senha temporária, só para ficar do tamanho da original e chamar a função.
                senhaTemp.append(senha[cont])
                cont += 1
 
            chave = ajustaChaveMaior(senhaTemp, chave) # Vai truncar a chave no tamanho exato da senha original!
        
        
        #atrubui o valor "nulo" para as posições impares da chave cont em uma nova variável para poder ignorar essa posição na 
        #próxima requisição, quando as posições impares da senha serão atribuidas apenas para variaveis de controle na nova
        #chave a ser criptografada.
        for i in chave:
            chaveNova.append(i)
            chaveNova.append("nulo")
    
    
        cont = 0
    
        #Descriptografando a senha!!!
        while (cont < tamanhoSenha):
        
            #se posição de controle da senha tem algum número entre zero e nove (ascii):
            if (senha[cont+1] in range(48, 58)): 
                solucao = (abs(senha[cont]+chaveNova[cont])-32)
        
            #se não, se posição de controle da senha estiver na range de "a" a "z":
            else:
                solucao = (abs(senha[cont]-chaveNova[cont])+32)
            
            descript.append(solucao)                                        #adiciona o resultado correto na lista descript
                            
            cont += 2                                                       #incrementa 2 ao cont para averiguar apenas as posições válidas (pares)
        

        descriptString = ""                                                 #inicaliza a variável
        descriptString = ascii_to_string(descript)                          #transforma a lista ascii para uma string de caracteres
        
        #As próximas duas linhas fazem a quebra do texto na posição 50 usando a biblioteca textwrap
        #wrapper = textwrap.TextWrapper(width=50)
        #descriptString = wrapper.fill(text=descriptString)
        
        descriptString = ('"'+descriptString+'"')                           #coloca valor recebido entre aspas duplas
    
        limpaTela()
    
    
        result.set(str(descriptString))    #Passa para o Label "resultado"
    


# função para limpar as entradas de dados do usuário após ele clicar no botão Criptografar, ou Descriptografar
def limpaTela():
    entry_senha.delete(0,END)
    entry_chave.delete(0,END)
    entry_nome.delete(0, END)
    entry_nome.focus()  # Coloca o cursor automaticamente no campo "Nome da senha"


def copiarResultado():
    texto = result.get()
    if texto.startswith('"') and texto.endswith('"'):
        texto = texto[1:-1]  # Remove as aspas das extremidades
    if texto:
        janela.clipboard_clear()
        janela.clipboard_append(texto)
        janela.update()
        mensagem_copiado.place(x=230, y=245)
        janela.after(2000, lambda: mensagem_copiado.place_forget())


def janela_ajuda():
    janela2 = Toplevel()
    janela2.title("Criptograf")
    largura_janela = 500
    altura_janela = 600

    largura_tela = janela2.winfo_screenwidth()
    altura_tela = janela2.winfo_screenheight()

    pos_x = int((largura_tela - largura_janela) / 2)
    pos_y = int((altura_tela - altura_janela) / 2)

    janela2.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    texto_orientacao= Label(janela2, text='''
                                               🔐 Como usar o Criptograf: 🔐

1. Digite a senha e uma chave de criptografia.
   - A chave pode conter letras, números, espaços ou símbolos.

2. Clique em "Criptografar" para gerar a senha codificada.
   - O resultado aparecerá entre aspas.
   - Atenção: espaços no início ou fim fazem parte da senha!
     (Por isso a senha é salva entre aspas. As aspas não fazem parte da senha).

3. O campo "Nome da senha" é opcional.
   - Quando preenchido, a senha criptografada será salva automaticamente
     no arquivo "Senhas.txt", na mesma pasta do Criptograf.

4. Para recuperar a senha original:
   - Cole a senha criptografada
   - Digite a mesma chave usada antes
   - Clique em "Descriptografar"

⚠️ Importante:
- Sem a chave correta, **não será possível descriptografar.**
- Guarde sua chave com segurança.
- **Não salve a chave junto da senha criptografada.**

📎 Sobre o software:
Este programa é gratuito, sem fins comerciais, e pode ser distribuído livremente.
O autor não se responsabiliza por senhas armazenadas ou perdidas pelo usuário.
''', justify=LEFT)
    texto_orientacao.grid(column=0, row=0, padx=30, pady=30)
    
    botao_voltar = Button(janela2, text="Voltar", command=janela2.destroy, justify=CENTER, bd=3)
    botao_voltar.place(x=210, y=480, width=100, height=40)

    texto_orientacao2= Label(janela2, text='''
                                            Criptograf v 1.0   - by Alex Hoffmann''')
    texto_orientacao2.place(x=150, y=545)
 
    limpaTela()



# Implementando a interface gráfica:

from tkinter import *
import random   #para função de sorteio de valor aleatório para as posições de verificação da senha criptografada na func criptografa.
import textwrap #para função de quebra de linha do texto ao final das funções criptografa e descriptografa

janela = Tk() #Cria a janela principal
janela.title("Criptograf")
largura_janela = 400
altura_janela = 350

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Centraliza parcialmente no topo (ex: 1/3 da largura da tela, topo da tela)
pos_x = int((largura_tela - largura_janela) / 4.5)  # ajusta para não ficar centralizado demais
pos_y = 120  # altura no topo, ajustável

janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")



#GUI

#Criando um objeto do tipo StringVar(), que vai pegar os dados digitados na tela????
result = StringVar()

#widgets

texto_nome = Label(janela, text="Nome da senha:", anchor=W)
entry_nome = Entry(janela)

texto_senha = Label(janela, text="Digite a senha: ", anchor=W)
entry_senha = Entry(janela)

texto_chave = Label(janela, text="Digite a chave: ", anchor=W)
entry_chave = Entry(janela)

botao1 = Button(janela, text="Criptografar", command=criptografa, bd=3) #passando função como parâmetro de outra função(Button). Não passar o parênteses no final da função, pois vai executar na hora, mesmo sem clicar no botão. 
botao2 = Button(janela, text="Descriptografar", command=descriptografa, bd=3) 


resultado = Entry(janela, textvariable=result, bd=2, relief="sunken", state="readonly", readonlybackground="white")

botao3 = Button(janela, text="Ajuda", command=janela_ajuda, bd=3)
botao4 = Button(janela, text="Copiar", command=copiarResultado)


#layout

texto_nome.place(x=10, y=10, width=100, height=20)
entry_nome.place(x=110, y=10, width=280, height=20)

texto_senha.place(x=10, y=50, width=100, height=20)
#texto_senha.grid(column=0, row=0, padx=10, pady=10) #pad é o espaço em cada eixo, para não deixar tudo amontoado. 

entry_senha.place(x=110, y=50, width=280, height=20)
#entry_senha.grid(column=1, row=0, padx=10, pady=10)

texto_chave.place(x=10, y=90, width=100, height=20)
#texto_chave.grid(column=0, row=1, padx=10, pady=10) #pad é o espaço em cada eixo, para não deixar tudo amontoado.

entry_chave.place(x=110, y=90, width=280, height=20)
#entry_chave.grid(column=1, row=1, padx=10, pady=10)

botao1.place(x=10, y=130, width=180, height=40)
#botao1.grid(column=0, row=2, padx=10, pady=10)

botao2.place(x=210, y=130, width=180, height=40)
#botao2.grid(column=1, row=2, padx=10, pady=10)

resultado.place(x=10, y=200, width=310, height=130)
#resultado.grid(column=0, row=3, padx=20, pady=10)

botao3.place(x=330, y=300, width=60, height=30)
#botao3.grid(column=2, row=4, padx=20, pady=10)

botao4.place(x=330, y=260, width=60, height=30)

#Mensagem de texto copiado:
mensagem_copiado = Label(janela, text="✅ Copiado!", fg="green", font=("Arial", 9))
mensagem_copiado.place(x=240, y=265)
mensagem_copiado.place_forget()



janela.bind('<Return>', lambda event: criptografa()) #tecla enter clica no botão de criptografar


#------------------

janela.mainloop()                                   #Deixa a janela em loop

