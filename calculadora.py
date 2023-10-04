#Calculadora com interface grafica usandando tkinter
import math
import tkinter as tk
from tkinter import messagebox

# Funções de cálculo
def adicao():
    resultado.set(n1.get() + n2.get())

def subtracao():
    resultado.set(n1.get() - n2.get())

def multiplicacao():
    resultado.set(n1.get() * n2.get())

def divisao():
    if n2.get() == 0:
        messagebox.showerror("Erro", "Divisão por zero não é permitida.")
    else:
        resultado.set(n1.get() / n2.get())

def potenciacao():
    resultado.set(n1.get() ** n2.get())

def raiz_quadrada():
    resultado.set(math.sqrt(n1.get()))

def resto():
    resultado.set(n1.get() % n2.get())

# Função para atualizar a operação de acordo com a escolha no menu suspenso
def atualizar_operacao():
    op = operacao.get()
    if op == "Adição (+)":
        adicao()
        operacao_selecionada.set("Operação: +")
    elif op == "Subtração (-)":
        subtracao()
        operacao_selecionada.set("Operação: -")
    elif op == "Multiplicação (*)":
        multiplicacao()
        operacao_selecionada.set("Operação: *")
    elif op == "Divisão (/)":
        divisao()
        operacao_selecionada.set("Operação: /")
    elif op == "Potenciação (^)":
        potenciacao()
        operacao_selecionada.set("Operação: ^")
    elif op == "Raiz Quadrada (√)":
        raiz_quadrada()
        operacao_selecionada.set("Operação: √")
    elif op == "Resto (%)":
        resto()
        operacao_selecionada.set("Operação: %")

# Função para fechar o aplicativo
def fechar():
    janela.destroy()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("400x400")

# Variáveis de controle
n1 = tk.DoubleVar()
n2 = tk.DoubleVar()
resultado = tk.DoubleVar()
operacao = tk.StringVar()  # Usamos StringVar para armazenar as operações
operacao_selecionada = tk.StringVar()  # Variável para mostrar a operação selecionada

# Rótulo e caixas de entrada
label1 = tk.Label(janela, text="Digite o primeiro número:")
label1.pack()
entry1 = tk.Entry(janela, textvariable=n1)
entry1.pack()

label2 = tk.Label(janela, text="Digite o segundo número:")
label2.pack()
entry2 = tk.Entry(janela, textvariable=n2)
entry2.pack()

# Lista de opções de operações com símbolos
operacoes = [
    "Adição (+)",
    "Subtração (-)",
    "Multiplicação (*)",
    "Divisão (/)",
    "Potenciação (^)",
    "Raiz Quadrada (√)",
    "Resto (%)"
]

# Menu suspenso para seleção de operação
label_operacao = tk.Label(janela, text="Selecione a operação:")
label_operacao.pack()
operacao_menu = tk.OptionMenu(janela, operacao, *operacoes)
operacao_menu.pack()

# Botão para calcular
calcular_button = tk.Button(janela, text="Calcular", command=atualizar_operacao)
calcular_button.pack()

# Rótulo para exibir a operação selecionada
label_operacao_selecionada = tk.Label(janela, textvariable=operacao_selecionada)
label_operacao_selecionada.pack()

# Rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="Resultado: ")
resultado_label.pack()
resultado_entry = tk.Entry(janela, textvariable=resultado, state="readonly")
resultado_entry.pack()

# Botão para fechar
fechar_button = tk.Button(janela, text="Fechar", command=fechar)
fechar_button.pack()

janela.mainloop()
