# Tela de Login usando a biblioteca Flet

from flet import *

def main(page: Page):
    page.title = "Site"    
    entrada_nome = TextField(label="Digite o seu nome")
    entrada_senha = TextField(label="Digite a sua senha")            
    
    def login(e):
        nome = entrada_nome.value
        senha = entrada_senha.value 
        if not entrada_nome.value:
            entrada_nome.error_text = "Por favor, coloque seu nome"
            page.update()
        if not entrada_senha.value:
            entrada_senha.error_text = "Por favor, coloque sua senha"
            page.update()
        
        else:

            print(f"Nome: {nome}\nSenha: {senha}")
        if (entrada_nome.value == 'Ernany') and (entrada_senha.value == '05092008'):
            print('Entrou')
            page.clean()
            page.add(Text(f'Ola {nome}\nSeja bem vindo!'))
    pass

    page.add( entrada_nome,
             entrada_senha,
             ElevatedButton("Login", on_click=lambda e: login(e))) 
    
    page.update()
    
app(target=main)