import nest_asyncio
import asyncio
from pyppeteer import launch
import customtkinter
import numpy as np

nest_asyncio.apply()
global nomes_empresas
nomes_empresas = np.array([1])  
global nomes_vagas
nomes_vagas = np.array([1])
global local_vagas
local_vagas = np.array([1])
bloco = []
global local_baixo
local_baixo = 450
global botão_vagas
botão_vagas = []
paginas = [True, False, False, False, False, False, False, False, False, False, False]

async def acessar_pagina(pg, pesq_vaga):
    await pg.goto("https://www.google.com.br/?hl=pt-BR")
    await pg.waitForSelector('textarea[name="q"]')
    await pg.type('textarea[name="q"]', pesq_vaga)
    await pg.keyboard.press('Enter')
    await asyncio.sleep(5)

async def click_botao_localizacao(pg):
    try:
        await pg.waitForSelector('g-raised-button[jsaction="click:O6N1Pb"]')
        await asyncio.sleep(2)
        await pg.click('g-raised-button[jsaction="click:O6N1Pb"]')
    except:
        print("Não clicou no botão de localização")

async def click_mais_vagas(pg):
    try:
        await pg.waitForSelector('a[class="jRKCUd"]')
        await pg.click('a[class="jRKCUd"]') 
    except:
        print("Não clicou em mais vagas")

async def get_informations(pg, qtd_result):
    for x in range(1, qtd_result + 1):
                pesquisa = await pg.xpath(f'//*[@id="rso"]/div/div/div/div/div[3]/div/div/div/div/infinity-scrolling/div[1]/div[1]/div[{x}]/div[1]/div/div/div/a/span[2]/div[1]/div[1]/div')
                nome = await pg.evaluate("(element) => element.textContent", pesquisa[0])
                empresa = await pg.evaluate("(element) => element.textContent", pesquisa[1])
                local = await pg.evaluate("(element) => element.textContent", pesquisa[2])

                global nomes_vagas
                nomes_vagas = np.append(nomes_vagas, nome)
                print(f"Nome da vaga: {nomes_vagas[x]}")
                global nomes_empresas
                nomes_empresas = np.append(nomes_empresas, empresa)
                print(f"Empresa: {nomes_empresas[x]}")
                global local_vagas
                local_vagas = np.append(local_vagas, local)
                print(f"Local: {local_vagas[x]}")
                print(nomes_vagas.size)



async def pesquisar(vaga, qtd_vaga):
        navegador = await launch(headless=False, executablePath="C:\\Users\\ernan\\Desktop\\drchrome\\chrome.exe")
        pagina = await navegador.newPage()
        await acessar_pagina(pagina, vaga)
        await click_botao_localizacao(pagina)
        await click_mais_vagas(pagina)
        await asyncio.sleep(5)
        await get_informations(pagina, qtd_vaga)
        await navegador.close()
        botão_vagas.append(customtkinter.CTkButton(master=corpo, text="Resultado", command=lambda: trocar_pagina(janela, corpo, paginas, False)))
        botão_vagas[-1].pack(padx=4, pady=4)
        botão_vagas[-1].place(x=25, y=400)

def fazer_pesquisa():
    vaga = pesquisar_vaga.get()
    nvaga = int(numero_vagas.get())
    asyncio.run(pesquisar(vaga, nvaga))


def campo_vaga(cp):
    global pesquisar_vaga
    pesquisar_vaga = customtkinter.CTkEntry(master=cp, placeholder_text="EX: vagas pedreiro", width=200, height=40)
    pesquisar_vaga.pack(padx=10, pady=2)
    pesquisar_vaga.place(x=290, y=210)

    pesquisar_vagatxt = customtkinter.CTkLabel(master=cp, text='Vaga desejada', font=('Arial', 12))
    pesquisar_vagatxt.pack(padx=6, pady=2)
    pesquisar_vagatxt.place(x=290, y=180)

def mostrar_titulo(cp):
    titulo = customtkinter.CTkLabel(master=cp, text='INFOVAGAS', font=('Arial', 48))
    titulo.pack(padx=10, pady=12)

def campo_numero_de_vagas(cp):
    global numero_vagas
    numero_vagas = customtkinter.CTkEntry(master=cp, placeholder_text="1-10", width=200, height=40)
    numero_vagas.pack(padx=8, pady=2)
    numero_vagas.place(x=290, y=300)

    numero_vagastxt = customtkinter.CTkLabel(master=cp, text='Quantidade de resultados', font=('Arial', 12))
    numero_vagastxt.pack(padx=6, pady=2)
    numero_vagastxt.place(x=290, y=270)

def botao_pesquisa(cp):
    botao_pesquisar = customtkinter.CTkButton(master=cp, text="Pesquisar", command=fazer_pesquisa)
    botao_pesquisar.pack(padx=3, pady=2)
    botao_pesquisar.place(x=290, y=400)

def apresentar_resultados(cp, nvagas=0):
        if (nomes_vagas.size > 1):
            local_baixo = 100
            for i in range(1, nomes_vagas.size):
                '''campo_resultado = customtkinter.CTkFrame(master=cp, height=75, width=400)
                campo_resultado.pack(padx=3, pady=4, fill="both", expand=True)
                campo_resultado.place(x=25, y=local_baixo + 100)'''
                vaga = customtkinter.CTkLabel(master=cp, text=f"{nomes_vagas[i]}", font=("Arial", 14))
                vaga.pack(padx=3, pady=4)
                local_baixo = local_baixo + 22
                empresa = customtkinter.CTkLabel(master=cp, text=f"{nomes_empresas[i]}", font=("Arial", 12))
                empresa.pack(padx=3, pady=4)
                local_baixo = local_baixo + 20
                localvaga = customtkinter.CTkLabel(master=cp, text=f"{local_vagas[i].strip()}", font=("Arial", 12))
                localvaga.pack(padx=3, pady=4)
                local_baixo = local_baixo + 40
        else:
            erro = customtkinter.CTkLabel(master=cp, text=f"Erro", font=("Arial", 12))
            erro.pack(padx=1, pady=20)
            erro.place(x=100, y=local_baixo)

def pagina_inicial(cp, t=True):
    
    campo_vaga(cp)
    campo_numero_de_vagas(cp)
    botao_pesquisa(cp)
    print("a")
    if (nomes_vagas.size > 1):
        print("a")
        for i in range(1, nomes_vagas.size):
            botão_vagas.append(customtkinter.CTkButton(master=cp, text="Resultado1"))
            botão_vagas[i].pack(padx=4, pady=4)
            botão_vagas[i].place(x=25, y=100)
            
def trocar_pagina(janela, corpo1, paginas, cond=True,):
    if cond:
        pagina_inicial(corpo1)
    else:
        corpo1.destroy()
        global corpo
        corpo = customtkinter.CTkScrollableFrame(janela, width=700, height=500)
        corpo.pack(pady=20, padx=10, fill="both", expand=True)
        mostrar_titulo(corpo)
        apresentar_resultados(corpo)

def main():
    customtkinter.set_appearance_mode('White')
    customtkinter.set_default_color_theme('green')
    global janela
    janela = customtkinter.CTk()
    janela.geometry('800x600')
    global corpo
    corpo = customtkinter.CTkFrame(master=janela, width=700, height=500)
    corpo.pack(padx=20, pady=10, fill='both', expand=True)
    mostrar_titulo(corpo)
    trocar_pagina(janela, corpo, paginas)


        
    

    janela.mainloop()

main()