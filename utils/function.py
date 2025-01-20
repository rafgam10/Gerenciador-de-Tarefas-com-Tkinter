from ttkbootstrap import ttk
from tkinter import END
from .constants import *

class ModelTask:
    def __init__(self, root, nome_tarefa):
        global linhaN

        # Criação da Task
        self.label_inst = ttk.Label(
            root,
            text=f" {nome_tarefa}",
            font=("Ariel", 16),
            background="#4e5d6c",
            width=20,
            anchor="w",
            relief="solid",
            justify="center"
        )
        self.label_inst.grid(row=linhaN, column=colunaLabelN, padx=5, pady=5)

        self.button_check = ttk.Button(
            root,
            text="Check",
            width=5,
            bootstyle=verde,
            command=self.check_task
        )
        self.button_check.grid(row=linhaN, column=colunaButtonCheckN, padx=5, pady=5)

        self.button_delete = ttk.Button(
            root,
            text=" X ",
            width=5,
            bootstyle=vermelho,
            command=self.delete_task
        )
        self.button_delete.grid(row=linhaN, column=colunaButtonDeleteN, padx=5, pady=5)

    def check_task(self):
        self.label_inst.configure(background="#5cb85c")

    def delete_task(self):
        self.label_inst.destroy()
        self.button_check.destroy()
        self.button_delete.destroy()
        lista_de_task.remove(self)

def criar_task(entry, root):
    global linhaN, lista_de_task

    nome_tarefa = entry.get()
    if nome_tarefa:
        linhaN += 1
        task = ModelTask(root, nome_tarefa)
        lista_de_task.append(task)
        entry.delete(0, END)
