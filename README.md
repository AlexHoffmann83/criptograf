
# Criptograf

Um aplicativo simples de criptografia de senhas, com chave personalizada e interface gráfica intuitiva desenvolvida em Python usando Tkinter.

## Funcionalidades

- Criptografa textos usando uma chave definida pelo usuário
- Armazena automaticamente as senhas criptografadas em um arquivo `Senhas.txt`
- Interface amigável com botões de ajuda e confirmação
- Código didático, ideal para estudos de lógica e manipulação de strings

## Requisitos

- Python 3.8 ou superior
- Bibliotecas padrão (`tkinter`, `random`, `textwrap`)

## Como usar

1. Execute o arquivo `Criptograf.py`:

2. Insira o **nome da senha**, **senha original** e **chave personalizada**.

3. Clique em `Criptografar`. O resultado aparecerá na tela e será salvo no arquivo `Senhas.txt`.

## Estrutura do Projeto

```
Criptograf/
├── Criptograf.py
├── requirements.txt
├── README.md
├── dist/
│   ├── Criptograf.exe
│   └── cadeado.ico
└── Senhas.txt  # (gerado automaticamente pelo programa)

```

## Executável

Para quem quiser testar sem instalar o Python, o executável Windows está disponível na pasta [`dist`](./dist).

- Basta baixar o arquivo `Criptograf.exe` e executá-lo.
- O ícone personalizado (`.ico`) também está incluído.
- Nenhuma instalação é necessária.

 Caso o Windows exiba um alerta de segurança, clique em "Mais informações" e depois em "Executar assim mesmo". Isso é comum com arquivos `.exe` não assinados digitalmente.


## Autor

**Alex Hoffmann**  
GitHub: [@AlexHoffmann83](https://github.com/AlexHoffmann83)

---

Este projeto foi desenvolvido como exercício de aprendizado em Python e criptografia básica. Sinta-se à vontade para usar, estudar e sugerir melhorias!
