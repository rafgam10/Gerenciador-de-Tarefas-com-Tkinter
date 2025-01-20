from tkinter import *
from ttkbootstrap import Style
import ttkbootstrap as tkk
from utils.constants import *
from utils.function import criar_task

# CONFIGURAÇÃO DA PÁGINA:

root = Tk()
style = Style(theme="superhero")
root.title("Gerenciador de Tarefas")
root.geometry("600x900")

# Campo de entrada para adicionar tarefas
entry_nome_tarefa = tkk.Entry(root, width=50)
entry_nome_tarefa.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Botão para adicionar tarefa
button_add = tkk.Button(root, text="Adicionar - Enter", width=15, command=lambda: criar_task(entry_nome_tarefa, root))
button_add.grid(row=0, column=5, columnspan=8, padx=10, pady=20)

# Separador horizontal
separador = tkk.Separator(root, orient="horizontal")
separador.grid(row=1, column=0, columnspan=20, sticky="ew", padx=10, pady=20)

# Atalhos do Programa
root.bind("<Return>", lambda event: criar_task(entry_nome_tarefa, root))

# Iniciar o loop principal
root.mainloop()
